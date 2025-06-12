import sys
import psycopg2
import re

from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, \
	QLineEdit, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from Messages import register_dialog_boxes
from not_repet_code.connect_database import get_db_connection


class Register(QMainWindow):
	def __init__(self):
		super().__init__()
		self.log_in_win = None
		self.setGeometry(400, 200, 700, 330)
		self.setWindowTitle("Register")
		self.setMinimumSize(700, 330)
		self.setWindowIcon(QIcon("../static/my_logo.png"))

		self.principal_grig = QGridLayout()
		self.principal_grig.setSpacing(20)

		self.title = QLabel("Please complete all fields")
		self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.principal_grig.addWidget(self.title, 0, 1, 1, 5)

		self.user_type_label = QLabel("Select user type : ")
		self.user_type_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.principal_grig.addWidget(self.user_type_label, 1, 1)

		self.user_type = QComboBox()
		self.user_type.addItem("Administrator")
		self.user_type.addItem("User")
		self.user_type.setCurrentIndex(-1)
		self.principal_grig.addWidget(self.user_type, 1, 2)

		self.first_name_label = QLabel("First name :")
		self.first_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.principal_grig.addWidget(self.first_name_label, 2, 1)

		self.first_name_entry = QLineEdit()
		self.first_name_entry.setAlignment(Qt.AlignmentFlag.AlignLeft)
		self.first_name_entry.setPlaceholderText("First name")
		self.first_name_entry.returnPressed.connect(self.save_button_pressed)
		self.principal_grig.addWidget(self.first_name_entry, 2, 2)

		self.last_name_label = QLabel("Last name :")
		self.last_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.principal_grig.addWidget(self.last_name_label, 2, 4)

		self.last_name_entry = QLineEdit()
		self.last_name_entry.setAlignment(Qt.AlignmentFlag.AlignLeft)
		self.last_name_entry.setPlaceholderText("Last name")
		self.last_name_entry.returnPressed.connect(self.save_button_pressed)
		self.principal_grig.addWidget(self.last_name_entry, 2, 5)

		self.e_mail_label = QLabel("E-mail:")
		self.e_mail_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.principal_grig.addWidget(self.e_mail_label, 3, 1)

		self.e_mail_entry = QLineEdit()
		self.e_mail_entry.setPlaceholderText("e-mail")
		self.e_mail_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.principal_grig.addWidget(self.e_mail_entry, 3, 2, 1, 3)

		self.password_label = QLabel("Password :")
		self.password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.principal_grig.addWidget(self.password_label, 4, 1)

		self.password_entry = QLineEdit()
		self.password_entry.setAlignment(Qt.AlignmentFlag.AlignLeft)
		self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
		self.password_entry.setToolTip(" The password must contain: \n"
									   "1. At least One Capital Letter.\n"
									   "2. At least One Numeric.\n"
									   "3. At least One Special Character.\n"
									   "4. Minimum length should be 8 characters.\n"
									   "5. Maximum length should be 30 characters.")
		self.password_entry.returnPressed.connect(self.save_button_pressed)
		self.principal_grig.addWidget(self.password_entry, 4, 2)

		self.password_confirm_label = QLabel("Confirm password :")
		self.password_confirm_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
		self.principal_grig.addWidget(self.password_confirm_label, 4, 4)

		self.password_confirm_entry = QLineEdit()
		self.password_confirm_entry.setAlignment(Qt.AlignmentFlag.AlignLeft)
		self.password_confirm_entry.setEchoMode(QLineEdit.EchoMode.Password)
		self.password_confirm_entry.returnPressed.connect(self.save_button_pressed)
		self.principal_grig.addWidget(self.password_confirm_entry, 4, 5)

		self.save_button = QPushButton("Save")
		self.save_button.setCheckable(True)
		self.save_button.setFixedSize(70, 30)
		self.principal_grig.addWidget(self.save_button, 5, 3)
		self.save_button.clicked.connect(self.save_button_pressed)

		from not_repet_code.logo_and_contact_detail import logo_image_and_contact_detail
		self.logo = logo_image_and_contact_detail()
		self.logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
		self.principal_grig.addWidget(self.logo, 6, 5)

		widget = QWidget()
		widget.setLayout(self.principal_grig)
		self.setCentralWidget(widget)

	@staticmethod
	def check_email_exists(e_mail):
		# Conectare la baza de date

		connection = get_db_connection()
		cursor = connection.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS users (
				id SERIAL PRIMARY KEY,
				chooses_user VARCHAR (50),
				first_name VARCHAR (255),
				last_name VARCHAR (255),
				e_mail VARCHAR (255),
				password VARCHAR (50),
				date TIMESTAMP NOT NULL DEFAULT NOW()
				);
				""")

		cursor.execute("""SELECT * FROM users WHERE e_mail LIKE %s""", (e_mail,))
		row = cursor.fetchone()

		cursor.close()
		connection.close()

		if row is not None:
			return True
		else:
			return False

	@staticmethod
	def validate_password(password):
		# Verifică dacă parola îndeplinește condițiile
		if len(password) < 8:
			return False
		if len(password) > 30:
			return False
		if not re.search(r"[A-Z]", password):  # Cel puțin o literă mare
			return False
		if not re.search(r"\d", password):  # Cel puțin o cifră
			return False
		if not re.search(r"[~!@#$%^&*()_+={}[\]:;\"'<>,.?/]", password):  # Cel puțin un caracter special
			return False
		return True

	def save_button_pressed(self):
		chooses_user = self.user_type.currentText()
		first_name = self.first_name_entry.text()
		last_name = self.last_name_entry.text()
		e_mail = self.e_mail_entry.text()
		password = self.password_entry.text()
		confirmed_password = self.password_confirm_entry.text()

		if chooses_user == "":
			register_dialog_boxes.user_type_empty(self)
		elif first_name == "":
			register_dialog_boxes.first_name_empty(self)
		elif last_name == "":
			register_dialog_boxes.last_name_empty(self)
		elif e_mail == "":
			register_dialog_boxes.e_mail_empty(self)
		elif not validate_e_mail(e_mail):
			register_dialog_boxes.e_mail_validator(self)
		elif password == "":
			register_dialog_boxes.password_empty(self)
		elif not self.validate_password(password):
			register_dialog_boxes.password_complexity(self)
		elif confirmed_password == "":
			register_dialog_boxes.confirm_password_empty(self)
		elif password != confirmed_password:
			register_dialog_boxes.password_check(self)
		elif self.check_email_exists(e_mail):
			register_dialog_boxes.email_exists(self)
		else:
			connection = get_db_connection()

			cursor = connection.cursor()
			# Crearea tabelului dacă nu există deja
			cursor.execute("""CREATE TABLE IF NOT EXISTS users (
				id SERIAL PRIMARY KEY,
				chooses_user VARCHAR (50),
				first_name VARCHAR (255),
				last_name VARCHAR (255),
				e_mail VARCHAR (255),
				password VARCHAR (50),
				date TIMESTAMP NOT NULL DEFAULT NOW()
				);
				""")
			# # Execută interogarea de inserare
			insert_script = """ 
				INSERT INTO users (chooses_user, first_name, last_name, e_mail, password) 
				VALUES (%s, %s, %s, %s, %s) 
				"""
			insert_value = chooses_user, first_name, last_name, e_mail, password
			cursor.execute(insert_script, insert_value)

			# Confirmă și închide conexiunea
			connection.commit()
			cursor.close()
			connection.close()

			# Afișează un mesaj de succes
			register_dialog_boxes.successfully_info(self)
			self.close()
			from log_in_window import LogIn
			self.log_in_win = LogIn()
			self.log_in_win.show()

	def closeEvent(self, event):
		from log_in_window import LogIn
		self.log_in_win = LogIn()
		self.log_in_win.show()
		event.accept()

def validate_e_mail(email):
	if not re.search(r"@", email):  # e-mailul trebuie sa contina "@" ca sa fie valid
		return False
	if "." in email:  # e-mailul trebuie sa contina "." ca sa fie valid
		return True
	else:
		return False


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Register()
	window.show()
	sys.exit(app.exec())
