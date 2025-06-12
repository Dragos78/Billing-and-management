from PySide6.QtWidgets import QMessageBox

from Messages import register_dialog_boxes

def pass_and_code(self):
	QMessageBox.information(self, "Successfully", "The e-mail with security code has been sent!")

def invalid_email(self):
	QMessageBox.warning(self, "Error", "E-mail incorect")
	
def pass_empty(self):
	QMessageBox.information(self, "Attention", "Password cannot be empty!")

def conf_pass_empty(self):
	QMessageBox.information(self,  "Attention", "Confirm password cannot be empty!")

def password_no_not_match(self):
	QMessageBox.warning(self, "Attention", "The password do not match!")

def code_error(self):
	QMessageBox.warning(self, "Error", "The code entered does not match with the code received via email.")

def code_time(self):
	QMessageBox.warning(self, "Error", "The code is not valid, more than 3 minutes have passed!")

def successfully_saved(self):
	QMessageBox.information(self, "Congratulation", "The password was changed!")
