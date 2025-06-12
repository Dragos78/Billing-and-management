import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QLabel, QLineEdit, QWidget,
                             QPushButton, QDialog)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, Slot
import psycopg2

from Messages import log_in_dialog_boxes
from not_repet_code import connect_database


class LogIn(QMainWindow):

	def __init__(self):
		super().__init__()
		self.main_win_window = None
		self.forgot_password_dialog = None  # Initializeaza dialogul ca None
		self.register_window = None # Initializeaza dialogul ca None
		self.setGeometry(550, 200, 500, 250)
		self.setWindowTitle("Log-in")
		self.setMinimumSize(500, 250)
		self.setWindowIcon(QIcon("../static/my_logo.png"))

		self.grid = QGridLayout()
		self.grid.setSpacing(20)

		self.label_title = QLabel("Please log in:")
		self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.grid.addWidget(self.label_title, 1, 0, 1, 4)

		self.e_mail_label = QLabel("E-mail : ")
		self.e_mail_label.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.grid.addWidget(self.e_mail_label, 2, 0)

		self.e_mail_entry = QLineEdit()
		self.e_mail_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.grid.addWidget(self.e_mail_entry, 2, 1, 1, 2)

		self.password_label = QLabel("Password : ")
		self.password_label.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.grid.addWidget(self.password_label, 3, 0)

		self.password_entry = QLineEdit()
		self.password_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
		self.grid.addWidget(self.password_entry, 3, 1, 1, 2)

		self.log_in_button = QPushButton("Log-in")
		self.log_in_button.setCheckable(True)
		self.log_in_button.clicked.connect(self.log_in_pressed)
		self.grid.addWidget(self.log_in_button, 4, 1, 1, 2)

		self.forgot_pass = QPushButton("Forgot password?")
		self.forgot_pass.setCheckable(True)
		self.forgot_pass.setToolTip("If you forgot password, click on me!")
		self.forgot_pass.setStyleSheet("border:none; background-color:transparent")
		self.forgot_pass.clicked.connect(self.forgot_password_pressed)
		self.grid.addWidget(self.forgot_pass, 5, 0)

		self.register = QPushButton("Register")
		self.register.setCheckable(True)
		self.register.setStyleSheet("border:none; background-color:transparent")


		self.register.clicked.connect(self.register_pressed)
		self.grid.addWidget(self.register, 5, 1, 1, 2)


		from not_repet_code.logo_and_contact_detail import logo_image_and_contact_detail
		self.logo = logo_image_and_contact_detail()
		self.logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
		self.grid.addWidget(self.logo, 5, 3)

		widget = QWidget()
		widget.setLayout(self.grid)
		self.setCentralWidget(widget)

		self.fereastra_forgot_password = None

	@staticmethod
	def check_e_mail_exist(e_mail):
		connection = psycopg2.connect(host="localhost", dbname="FirstApp", user="postgres", password="admin",
		                              port=5432)
		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(*) FROM users WHERE e_mail=%s", (e_mail,))
		count = cursor.fetchone()[0]
		cursor.close()
		connection.close()
		print(count)
		return count > 0

	@staticmethod
	def check_password_exist(get_e_mail):
		try:
			connection = connect_database.get_db_connection()

			cursor = connection.cursor()

			cursor.execute('''
                SELECT password, e_mail
                FROM users
                WHERE e_mail=%s
            ''', (get_e_mail,))

			credential = cursor.fetchone()
			cursor.close()
			connection.close()

			if credential is None:
				raise TypeError("❌ Nu există utilizator cu această adresă de e-mail.")

			return credential

		except psycopg2.errors.UndefinedTable:
			print("⚠️ Tabela 'users' nu există în baza de date. Verifică dacă a fost creată.")
			return None

		except psycopg2.OperationalError as e:
			print(f"🚫 Conexiunea la baza de date a eșuat: {e}")
			return None

		except Exception as e:
			print(f"💥 Eroare neașteptată: {e}")
			return None

	def log_in_pressed(self):
		get_e_mail = self.e_mail_entry.text()
		get_password = self.password_entry.text()

		if get_e_mail == "":
			log_in_dialog_boxes.e_mail_empty(self)
		elif get_password == "":
			log_in_dialog_boxes.password_empty(self)
		else:
			try:
				credential = self.check_password_exist(get_e_mail)
				str_get_e_mail = credential[1]
				str_password = credential[0]

				if str_get_e_mail == get_e_mail and str_password == get_password:
					log_in_dialog_boxes.credential_successfully(self)
					self.close()
					from main_win import MainWin
					self.main_win_window = MainWin()
					self.main_win_window.show()
					self.main_win_window.showMaximized()

				else:
					log_in_dialog_boxes.credential_error(self)

			except TypeError:
				log_in_dialog_boxes.not_in_database(self)

	@Slot(bool)
	def register_pressed(self):
		from register_window import Register
		self.register_window = Register()
		self.register_window.show()
		self.close()

	@Slot(bool)
	def forgot_password_pressed(self):
		from forgot_password_window import ForgotPassword
		self.fereastra_forgot_password = ForgotPassword()
		self.fereastra_forgot_password.show()
		self.close()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = LogIn()
	window.show()
	app.exec()