import shutil
import os

from PySide6.QtWidgets import (QLabel, QGridLayout, QDialog,
                               QPushButton, QFileDialog)
from PySide6.QtGui import Qt, QIcon
from not_repet_code.logo_and_contact_detail import logo_image_and_contact_detail
from Messages import company_data_message
from not_repet_code import connect_database
from Tab_uri.Invoice.AddInvoice.add_invoice import YourCompanyField


class YourCompanyData(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Your company data")
		self.setWindowIcon(QIcon("../../../static/my_logo.png"))

		layout_main = QGridLayout()

		self.your_company_field = YourCompanyField()
		layout_main.addWidget(self.your_company_field)

		self.btn_load_your_company_logo = QPushButton("Load your logo")
		self.btn_load_your_company_logo.clicked.connect(self.load_logo_pressed)
		layout_main.addWidget(self.btn_load_your_company_logo, 9, 0, 1, 2)

		self.lbl_logo_load = QLabel("")
		layout_main.addWidget(self.lbl_logo_load, 10, 0)

		self.btn_save_company_data = QPushButton("Save")
		self.btn_save_company_data.clicked.connect(self.save_btn_pressed)
		layout_main.addWidget(self.btn_save_company_data, 11, 0, 1, 2)

		lbl_empty = QLabel("     ")
		layout_main.addWidget(lbl_empty, 12, 0, 1, 2)

		my_logo = logo_image_and_contact_detail()
		my_logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
		layout_main.addWidget(my_logo, 13, 1)

		self.setLayout(layout_main)

	def load_logo_pressed(self):

		source_file,_=QFileDialog.getOpenFileName(self, "Chose file", "", "*.png")

		if source_file:
			fixed_folder = "D:/Python/Autodidact/PyQt/13_03_2023/company_logo"

			if not os.path.exists(fixed_folder):
				os.makedirs(fixed_folder)

			# fixed_file_name = "company_logo.png"

			_, ext = os.path.splitext(source_file)
			fixed_file_name_with_ext = f"company_logo{ext}"

			target_path = os.path.join(fixed_folder, fixed_file_name_with_ext)

			shutil.copy(source_file, target_path)
			company_data_message.successfully_load_logo(self)
			print(f"Imaginea a fost salvata cu succes ca:{target_path}")

		else:
			company_data_message.no_image_selected(self)
			print("Nu ai selectat nici o imagine")

		self.lbl_logo_load.setText(f"Selected file: {source_file}")
		self.lbl_logo_load.setAlignment(Qt.AlignmentFlag.AlignCenter)

	def save_btn_pressed(self):
		entry_company_name = self.entry_company_name_field.text()
		entry_company_cif_field = self.entry_company_cif_field.text()
		entry_company_reg_number_field = self.entry_company_reg_number_field.text()
		entry_company_headquarter_field = self.entry_company_headquarter_field.text()
		entry_company_county_field = self.entry_company_county_field.text()
		entry_company_iban_field = self.entry_company_iban_field.text()
		entry_company_social_capital_field = self.entry_company_social_capital_field.text()
		entry_company_bank_field = self.entry_company_bank_field.text()

		# connect database

		connection = connect_database.get_db_connection()

		cursor = connection.cursor()

		cursor.execute ("""
		CREATE TABLE IF NOT EXISTS company_data (
		company_name VARCHAR (50),
		company_cif VARCHAR (10),
		company_reg_number VARCHAR (14),
		company_headquarter VARCHAR (200),
		company_county VARCHAR (50),
		company_iban VARCHAR (34),
		company_social_capital VARCHAR (10),
		company_bank VARCHAR (50)
		);
		""")

		insert_script = """ INSERT INTO company_data 
		(company_name, company_cif, company_reg_number, company_headquarter, company_county, 
		company_iban, company_social_capital, company_bank)
		VALUES
		(%s, %s, %s, %s, %s, %s, %s, %s)
		"""
		insert_value = (entry_company_name, entry_company_cif_field, entry_company_reg_number_field,
		                entry_company_headquarter_field, entry_company_county_field, entry_company_iban_field,
		                entry_company_social_capital_field, entry_company_bank_field)

		cursor.execute(insert_script, insert_value)

		connection.commit()
		cursor.close()
		connection.close()

		company_data_message.saved_successfully(self)

		self.close()


