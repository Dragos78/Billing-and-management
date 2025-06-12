from PySide6.QtWidgets import QMessageBox

def cif_exist(self):
	QMessageBox.warning(self, "Error.", "No company with this CIF in database")

def invoice_duplicate(self):
	QMessageBox.warning(self,"Error.", "Invoice serial number already exist!")