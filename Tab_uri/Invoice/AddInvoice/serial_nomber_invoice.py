import sys
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout
from PySide6.QtGui import Qt

class TitleInvoice(QWidget):
	def __init__(self):
		super().__init__()

		layout_central = QGridLayout()

		lbl_title = QLabel("FISCAL INVOICE")
		lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)
		lbl_title.setStyleSheet(""" font: 'Arial Rounded MT Bold'; 
		font-size: 24pt;
		font-weigh:900;
		""")
		layout_central.addWidget(lbl_title, 0, 1, 1, 2)

		lbl_serial = QLabel("Serial : ")
		layout_central.addWidget(lbl_serial, 1, 1)

		self.entry_serial = QLineEdit()
		self.entry_serial.setFixedSize(130, 25)
		layout_central.addWidget(self.entry_serial, 1, 2)

		lbl_number = QLabel("Number: ")
		layout_central.addWidget(lbl_number, 2, 1)

		self.entry_number = QLineEdit()
		self.entry_number.setFixedSize(130, 25)
		layout_central.addWidget(self.entry_number, 2, 2)

		lbl_date_time = QLabel("Date ( dd.mm.yyyy ) : ")
		lbl_date_time.setFixedSize(130, 25)
		layout_central.addWidget(lbl_date_time, 3, 1)

		self.entry_date_time = QLineEdit()
		self.entry_date_time.setFixedSize(130, 25)
		layout_central.addWidget(self.entry_date_time, 3, 2)

		self.setLayout(layout_central)

