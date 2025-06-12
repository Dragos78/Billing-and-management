import sys
from PySide6.QtWidgets import (
	QLabel, QLineEdit, QWidget,
	QPushButton, QVBoxLayout, QGridLayout
)
from PySide6.QtCore import Qt

class SupplierWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.dict_qline_edit = {} # se creaza dictionarul care contine toate widgeeturile de qlinedit pt  a putea fi curatate dupa apasate butonului save

		self.setWindowTitle("Add Supplier")
		self.showMaximized()

		provider_layout = QGridLayout()

		lbl_title = QLabel("Enter supplier details:")
		provider_layout.addWidget(lbl_title, 0, 4, 1, 5)

		lbl_empty_space_left0 = QLabel("          ")
		lbl_empty_space_left0.setFixedSize(450, 20)
		# lbl_empty_space_left0.setStyleSheet("border: 1px solid red; color: red;")
		provider_layout.addWidget(lbl_empty_space_left0, 2, 0)

		lbl_empty_space_left1 = QLabel("          ")
		lbl_empty_space_left1.setFixedSize(70, 20)
		#         lbl_empty_space_left1.setStyleSheet("border: 1px solid red; color: red;")
		provider_layout.addWidget(lbl_empty_space_left1, 2, 2)

		lbl_empty_space_center = QLabel("          ")
		lbl_empty_space_center.setFixedSize(70, 20)
		#         lbl_empty_space_center.setStyleSheet("border: 1px solid red; color: red;")
		provider_layout.addWidget(lbl_empty_space_center, 2, 4)

		lbl_empty_space_right0 = QLabel("          ")
		lbl_empty_space_right0.setFixedSize(70, 20)
		#         lbl_empty_space_right0.setStyleSheet("border: 1px solid red; color: red;")
		provider_layout.addWidget(lbl_empty_space_right0, 2, 6)

		lbl_empty_space_right1 = QLabel("          ")
		lbl_empty_space_right1.setFixedSize(450, 20)
		# lbl_empty_space_right1.setStyleSheet("border: 1px solid red; color: red;")
		provider_layout.addWidget(lbl_empty_space_right1, 2, 8)

		self.lbl_supplier_name = QLabel("Supplier name:")
		self.lbl_supplier_name.setFixedSize(200, 20)
		provider_layout.addWidget(self.lbl_supplier_name, 1, 1, 1, 2)

		self.supplier_name_input = QLineEdit()
		self.supplier_name_input.setPlaceholderText("Supplier Name,  50 character.")
		provider_layout.addWidget(self.supplier_name_input, 1, 3, 1, 5)
		self.dict_qline_edit[0] = self.supplier_name_input

		self.lbl_register_number = QLabel("Num.tr.register:")
		self.lbl_register_number.setMinimumSize(100, 20)
		provider_layout.addWidget(self.lbl_register_number, 2, 1)

		self.register_number_input = QLineEdit()
		self.register_number_input.setPlaceholderText("Serial number in the trade register, max 14.")
		self.register_number_input.setMinimumSize(200, 20)
		provider_layout.addWidget(self.register_number_input, 2, 3)
		self.dict_qline_edit[1] = self.register_number_input

		self.lbl_register_year = QLabel("Year register:")
		self.lbl_register_year.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.lbl_register_year.setMinimumSize(100, 20)
		self.lbl_register_year.setFixedSize(200, 20)
		provider_layout.addWidget(self.lbl_register_year, 2, 5)

		self.register_year_input = QLineEdit()
		self.register_year_input.setPlaceholderText("Year of registration")
		self.register_year_input.setMinimumSize(100, 20)
		self.register_year_input.setFixedSize(150, 20)
		provider_layout.addWidget(self.register_year_input, 2, 7)
		self.dict_qline_edit[2] = self.register_year_input

		self.lbl_supplier_cui_cif = QLabel("CUI / CIF:")
		self.lbl_supplier_cui_cif.setFixedSize(200, 20)
		provider_layout.addWidget(self.lbl_supplier_cui_cif, 3, 1, 1, 2)

		self.cui_cif_input = QLineEdit()
		self.cui_cif_input.setPlaceholderText("CUI / CIF , maximum 12 character.")
		provider_layout.addWidget(self.cui_cif_input, 3, 3, 1, 5)
		self.dict_qline_edit[3] = self.cui_cif_input

		self.lbl_headquarter = QLabel("Headquarters:")
		self.lbl_headquarter.setFixedSize(200, 20)
		provider_layout.addWidget(self.lbl_headquarter, 4, 1, 1, 2)

		self.headquarters_input = QLineEdit()
		self.headquarters_input.setPlaceholderText("Headquarters, , maxim 30 character")
		provider_layout.addWidget(self.headquarters_input, 4, 3, 1, 5)
		self.dict_qline_edit[4] = self.headquarters_input

		self.lbl_county = QLabel("County:")
		self.lbl_county.setFixedSize(200, 20)
		provider_layout.addWidget(self.lbl_county, 5, 1, 1, 2)

		self.county_input = QLineEdit()
		self.county_input.setPlaceholderText("County, maxim 50 character")
		provider_layout.addWidget(self.county_input, 5, 3, 1, 5)
		self.dict_qline_edit[5] = self.county_input

		self.lbl_social_capital = QLabel("Social capital:")
		self.lbl_social_capital.setFixedSize(200, 20)
		provider_layout.addWidget(self.lbl_social_capital, 6, 1, 1, 2)

		self.social_capital_input = QLineEdit()
		self.social_capital_input.setPlaceholderText("Social capital")
		provider_layout.addWidget(self.social_capital_input, 6, 3, 1, 5)
		self.dict_qline_edit[6] = self.social_capital_input

		self.lbl_iban_code = QLabel("Iban code:")
		self.lbl_iban_code.setFixedSize(200, 20)
		provider_layout.addWidget(self.lbl_iban_code, 7, 1, 1, 2)

		self.iban_code_input = QLineEdit()
		self.iban_code_input.setPlaceholderText("Iban code, maximum 24 character.")
		provider_layout.addWidget(self.iban_code_input, 7, 3, 1, 5)
		self.dict_qline_edit[7] = self.iban_code_input

		self.lbl_supplier_bank = QLabel("Bank:")
		self.lbl_supplier_bank.setFixedSize(200, 20)
		provider_layout.addWidget(self.lbl_supplier_bank, 8, 1, 1, 2)

		self.supplier_bank_input = QLineEdit()
		self.supplier_bank_input.setPlaceholderText("Supplier bank, maximum 20 character.")
		provider_layout.addWidget(self.supplier_bank_input, 8, 3, 1, 5)
		self.dict_qline_edit[8] = self.supplier_bank_input

		self.lbl_supplier_email = QLabel("Email: ")
		provider_layout.addWidget(self.lbl_supplier_email, 9 , 1)

		self.supplier_email_input = QLineEdit()
		self.supplier_email_input.setPlaceholderText("For sending orders, maximum 30 character.")
		provider_layout.addWidget(self.supplier_email_input, 9, 3, 1, 5)
		self.dict_qline_edit[9] = self.supplier_email_input

		self.empty_row = QLabel("      ")
		self.empty_row.setFixedSize(200, 60)
		provider_layout.addWidget(self.empty_row, 10, 1, 1, 2)

		self.setLayout(provider_layout)

	def clear_qline_edit_content(self):
		for key in self.dict_qline_edit.keys():
			self.dict_qline_edit[key].clear()