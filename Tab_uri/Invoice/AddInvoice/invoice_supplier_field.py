import sys

from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QDialog)
from PySide6.QtGui import Qt, QIcon, QFont


class SupplierCompanyField(QDialog):
	def __init__(self):
		super().__init__()

		layout_main = QGridLayout()

		self.lbl_supplier_company_name = QLabel("Name: ")
		self.lbl_supplier_company_name.setFont(QFont("Arial", 8))
		layout_main.addWidget(self.lbl_supplier_company_name, 0,0)


		self.exit_supplier_company_name_field = QLabel("")
		self.exit_supplier_company_name_field.setFixedSize(182,18)
		layout_main.addWidget(self.exit_supplier_company_name_field, 0, 1)

		self.lbl_supplier_company_cif = QLabel("CIF:")
		self.lbl_supplier_company_cif.setFont(QFont("Arial", 8))
		layout_main.addWidget(self.lbl_supplier_company_cif, 1, 0)

		self.entry_supplier_company_cif_field = QLineEdit()
		self.entry_supplier_company_cif_field.setFixedSize(182, 18)
		layout_main.addWidget(self.entry_supplier_company_cif_field, 1, 1)

		self.lbl_supplier_company_reg_number = QLabel("Ser.No.Trade Reg.: ")
		self.lbl_supplier_company_reg_number.setFont(QFont("Arial", 8))
		layout_main.addWidget(self.lbl_supplier_company_reg_number, 2, 0)

		self.exit_supplier_company_reg_number_field = QLabel("")
		self.exit_supplier_company_reg_number_field.setFixedSize(182, 18)
		layout_main.addWidget(self.exit_supplier_company_reg_number_field, 2,1)

		self.lbl_supplier_company_headquarter = QLabel("Headquarter: ")
		self.lbl_supplier_company_headquarter.setFont(QFont("Arial", 8))
		layout_main.addWidget(self.lbl_supplier_company_headquarter, 3, 0)

		self.exit_supplier_company_headquarter_field = QLabel("")
		self.exit_supplier_company_headquarter_field.setFixedSize(182, 18)
		layout_main.addWidget(self.exit_supplier_company_headquarter_field, 3, 1)

		self.lbl_supplier_company_county = QLabel("County: ")
		self.lbl_supplier_company_county.setFont(QFont("Arial", 8))
		layout_main.addWidget(self.lbl_supplier_company_county, 4, 0)

		self.exit_supplier_company_county_field = QLabel("")
		self.exit_supplier_company_county_field.setFixedSize(182, 18)
		layout_main.addWidget(self.exit_supplier_company_county_field, 4, 1)

		self.lbl_supplier_company_iban = QLabel("IBAN: ")
		self.lbl_supplier_company_iban.setFont(QFont("Arial", 8))
		layout_main.addWidget(self.lbl_supplier_company_iban, 5, 0)

		self.exit_supplier_company_iban_field = QLabel("")
		self.exit_supplier_company_iban_field.setFixedSize(182, 18)
		layout_main.addWidget(self.exit_supplier_company_iban_field, 5, 1)

		self.lbl_supplier_company_social_capital = QLabel("Social capital: ")
		self.lbl_supplier_company_social_capital.setFont(QFont("Arial", 8))
		layout_main.addWidget(self.lbl_supplier_company_social_capital, 6, 0)

		self.exit_supplier_company_social_capital_field = QLabel("")
		self.exit_supplier_company_social_capital_field.setFixedSize(182, 18)
		layout_main.addWidget(self.exit_supplier_company_social_capital_field, 6, 1)

		self.lbl_supplier_company_bank = QLabel("Bank: ")
		self.lbl_supplier_company_bank.setFont(QFont("Arial", 8))
		layout_main.addWidget(self.lbl_supplier_company_bank, 7, 0)

		self.exit_supplier_company_bank_field = QLabel("")
		self.exit_supplier_company_bank_field.setFixedSize(182, 18)
		layout_main.addWidget(self.exit_supplier_company_bank_field, 7, 1)

		self.setLayout(layout_main)

