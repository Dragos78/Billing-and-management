from PySide6.QtWidgets import QMessageBox

def successfully_load_logo(self):
	QMessageBox.information(self, "Succes", "The logo has been uploaded!")

def no_image_selected(self):
	QMessageBox.information(self, "Error", "No image selected.")

def saved_successfully(self):
	QMessageBox.information(self, "Congratulation!", "The data has been saved!")