from PySide6.QtWidgets import QMessageBox

def e_mail_empty(self):
	QMessageBox.warning(self, "Error!", "E-mail cannot be empty!")

def password_empty(self):
	QMessageBox.warning(self, "Error!", "Password cannot be empty!")

def not_in_database(self):
	QMessageBox.warning(self, "Error", "Credential are not in database, please register")

def credential_error(self):
	QMessageBox.warning(self, "Error!", "User name or password are wrong or please register")

def credential_successfully(self):
	QMessageBox.information(self, "Congratulation", "You are login, please enjoy")
