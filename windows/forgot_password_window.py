import sys
import psycopg2

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from e_mail_py import email_sent
import random
import time
from Messages import forgot_pass_messagebox
from not_repet_code import connect_database


class ForgotPassword(QMainWindow):
	def __init__(self):
		super().__init__()


		self.log_in_window = None
		self.setWindowTitle("Forgot Password")
		self.setGeometry(600, 200, 300, 400)
		self.setMinimumSize(300, 400)
		self.setWindowIcon(QIcon("../static/my_logo.png"))

		self.security_code = None
		self.time_code_generate = None

		self.main_grid = QGridLayout()
		self.main_grid.setSpacing(20)

		self.label_title = QLabel("Reset the password : ")
		self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.main_grid.addWidget(self.label_title, 0,0, 1, 2)

		self.label_email = QLabel("E-mail : ")
		self.label_email.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.main_grid.addWidget(self.label_email, 1, 0)

		self.e_mail_entry = QLineEdit()
		self.e_mail_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.e_mail_entry.setPlaceholderText("e-mail")
		self.main_grid.addWidget(self.e_mail_entry, 1, 1)

		self.code_label = QLabel("Security code : ")
		self.code_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.main_grid.addWidget(self.code_label, 2, 0)
		self.code_label.setHidden(True)

		self.code_entry = QLineEdit()
		self.code_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.code_entry.setPlaceholderText("security code")
		self.main_grid.addWidget(self.code_entry, 2, 1)
		self.code_entry.setHidden(True)

		self.new_password_label = QLabel("New password : ")
		self.new_password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.main_grid.addWidget(self.new_password_label, 3, 0)
		self.new_password_label.setHidden(True)

		self.new_password_entry = QLineEdit()
		self.new_password_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.new_password_entry.setPlaceholderText("new password")
		self.new_password_entry.setEchoMode(QLineEdit.EchoMode.Password)
		self.main_grid.addWidget(self.new_password_entry, 3, 1)
		self.new_password_entry.setHidden(True)

		self.confirm_password_label = QLabel("Confirm password : ")
		self.confirm_password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.main_grid.addWidget(self.confirm_password_label, 4, 0)
		self.confirm_password_label.setHidden(True)

		self.confirm_password_entry = QLineEdit()
		self.confirm_password_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.confirm_password_entry.setPlaceholderText("confirm password")
		self.confirm_password_entry.setEchoMode(QLineEdit.EchoMode.Password)
		self.main_grid.addWidget(self.confirm_password_entry, 4, 1)
		self.confirm_password_entry.setHidden(True)

		self.submit_button = QPushButton(" Submit ")
		self.submit_button.setCheckable(True)
		self.submit_button.clicked.connect(self.submit_pressed)
		self.main_grid.addWidget(self.submit_button, 5, 0, 1, 2)

		self.save_button = QPushButton("  Save  ")
		self.save_button.setCheckable(True)
		self.save_button.clicked.connect(self.save_button_pressed)
		self.main_grid.addWidget(self.save_button, 7, 0, 1, 2)
		self.save_button.setHidden(True)

		self.question_help_label = QLabel()
		self.question_help = QPixmap(QPixmap("../static/question-mark_40x40.png"))
		self.question_help_label.setPixmap(self.question_help)
		self.question_help_label.setToolTip("                  To reset password              \n"
		                                    "1. Enter valid e-mail address.\n"
		                                    "2. verify you email, do`nt forget to check spam,\n"
		                                    "   you receive an e-mail with security code.\n"
		                                    "3. Enter security code from e-mai.\n"
		                                    "4. Enter new password.\n"
		                                    "5. Confirm new password.\n"
		                                    "6. Press 'save' button.")
		self.question_help_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
		self.main_grid.addWidget(self.question_help_label)

		from not_repet_code.logo_and_contact_detail import logo_image_and_contact_detail
		self.logo = logo_image_and_contact_detail()
		self.logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
		self.main_grid.addWidget(self.logo)

		widget = QWidget()
		widget.setLayout(self.main_grid)
		self.setCentralWidget(widget)

	def submit_pressed(self):
		email_receiver = self.e_mail_entry.text()

		connection = connect_database.get_db_connection()
		cursor = connection.cursor()

		cursor.execute('''
					SELECT *
					FROM users
					WHERE e_mail LIKE %s
					''', (email_receiver,))
		row = cursor.fetchone()
		cursor.close()
		connection.close()

		email_valid = row[4]

		if email_receiver != email_valid:
			forgot_pass_messagebox.invalid_email(self)
		else:
			self.security_code = random.randint(100000, 999999)  # Generate a 6-digit security code
			self.time_code_generate = time.time()
			email_sent(email_receiver, self.security_code)  # Send the email with security code

			forgot_pass_messagebox.pass_and_code(self)

			self.code_label.setHidden(False)
			self.code_entry.setHidden(False)
			self.new_password_label.setHidden(False)
			self.new_password_entry.setHidden(False)
			self.confirm_password_label.setHidden(False)
			self.confirm_password_entry.setHidden(False)
			self.save_button.setHidden(False)

			self.submit_button.setDisabled(True)

	def save_button_pressed(self):

		security_code_luat = self.code_entry.text()

		if security_code_luat != str(self.security_code):
			forgot_pass_messagebox.code_error(self)
		elif time.time() - self.time_code_generate >= 180:
			forgot_pass_messagebox.code_time(self)
		else:
			new_pass = self.new_password_entry.text()
			conf_new_pass = self.confirm_password_entry.text()
			if new_pass == "":
				forgot_pass_messagebox.pass_empty(self)
			elif conf_new_pass == "":
				forgot_pass_messagebox.conf_pass_empty(self)
			elif new_pass != conf_new_pass:
				forgot_pass_messagebox.password_no_not_match(self)
			else:
				connection = connect_database.get_db_connection()
				cursor = connection.cursor()
				update_sql = '''
					UPDATE users
					SET password = %s
					WHERE e_mail = %s			
				'''
				password = self.new_password_entry.text()
				e_mail = self.e_mail_entry.text()
				cursor.execute(update_sql, (password, e_mail))
				connection.commit()
				cursor.close()
				connection.close()
				forgot_pass_messagebox.successfully_saved(self)
				self.close()
				from log_in_window import LogIn
				self.log_in_window = LogIn()
				self.log_in_window.show()

	def closeEvent(self, event):
		from log_in_window import LogIn
		self.log_in_window = LogIn()
		self.log_in_window.show()
		event.accept()



if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = ForgotPassword()
	window.show()
	sys.exit(app.exec())