import sys
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from  PySide6.QtCore import Qt

def your_company_logo():
	logo = QLabel()

	your_logo = QPixmap("../company_logo/company_logo.png")

	resized_your_logo = your_logo.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)

	logo.setPixmap(resized_your_logo)

	return logo