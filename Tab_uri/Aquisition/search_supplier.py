from PySide6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QGridLayout, QHBoxLayout, QTableWidgetItem, QLabel, QMessageBox)
from PySide6.QtCore import Qt
from not_repet_code.supplier_widget import SupplierWidget
from not_repet_code.connect_database import get_db_connection
from ussed_table.supplier_table import table_result
from Messages import search_supplier_message
from datetime import date


class SearchSupplier(QWidget):
	def __init__(self):
		super().__init__()
		self.supplier_field = SupplierWidget()
		self.table_result = table_result()  # trebuie să fie o instanță de QTableWidget
		self.table_result.verticalHeader().setVisible(False)
		self.table_result.setMinimumSize(1385, 250)

		layout_supplier = QVBoxLayout()
		layout_supplier.addWidget(self.supplier_field)

		empty_lbl = QLabel("    ")

		layout_table = QHBoxLayout()
		layout_table.addStretch()
		layout_table.addWidget(self.table_result)
		layout_table.addStretch()
		layout_supplier.addLayout(layout_table)
		layout_supplier.addWidget(empty_lbl)

		self.search_btn = QPushButton("Search")
		self.search_btn.setFixedSize(80, 25)
		self.search_btn.clicked.connect(self.search_btn_pressed)

		self.modify_btn = QPushButton("Modify")
		self.modify_btn.setFixedSize(80, 25)
		self.modify_btn.clicked.connect(self.modify_btn_pressed)

		self.delete_btn = QPushButton("Delete")
		self.delete_btn.setFixedSize(80, 25)
		self.delete_btn.clicked.connect(self.delete_btn_pressed)


		# Layout pentru centrare butoane
		layout_btn = QHBoxLayout()
		layout_btn.addStretch()
		layout_btn.addWidget(self.search_btn)
		layout_btn.addWidget(self.modify_btn)
		layout_btn.addWidget(self.delete_btn)
		layout_btn.addStretch()

		layout_supplier.addLayout(layout_btn)

		layout_info_logo = QGridLayout()

		# Information about search proces

		from Tab_uri.Aquisition.info_search_supplier import help_search_supplier
		self.inform = help_search_supplier()
		self.inform.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)

		# Logo și detalii contact

		from not_repet_code.logo_and_contact_detail import logo_image_and_contact_detail
		self.logo = logo_image_and_contact_detail()
		self.logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

		layout_info_logo.addWidget(self.inform, 0, 0)
		layout_info_logo.setColumnStretch(0, 1)
		layout_info_logo.setColumnStretch(1, 1)
		layout_info_logo.addWidget(self.logo, 0, 1)

		layout_supplier.addLayout(layout_info_logo)
		self.setLayout(layout_supplier)

		# Conectare dublu-click
		self.table_result.cellDoubleClicked.connect(self.table_row_double_clicked)

	def search_btn_pressed(self):

		supp_name = self.supplier_field.supplier_name_input.text().strip()
		supp_trade_register = self.supplier_field.register_number_input.text().strip()
		supp_year = self.supplier_field.register_year_input.text().strip()
		supp_cif = self.supplier_field.cui_cif_input.text().strip()
		supp_headquarter = self.supplier_field.headquarters_input.text().strip()
		supp_county = self.supplier_field.county_input.text().strip()
		supp_social_capital = self.supplier_field.social_capital_input.text().strip()
		supp_iban = self.supplier_field.iban_code_input.text().strip()
		supp_bank = self.supplier_field.supplier_bank_input.text().strip()
		supp_email = self.supplier_field.supplier_email_input.text().strip()


		try:
			conn = get_db_connection()
			cursor = conn.cursor()

			# Selectăm DOAR coloanele dorite, nu toate cu *
			query = """
                SELECT supp_id, supp_name, supp_trade_register, supp_year, supp_cif, supp_headquarter, supp_county, 
                supp_social_capital, supp_iban, supp_bank, supp_email
                FROM supplier
                WHERE 1=1
            """
			params = []

			if supp_name:
				query += " AND supp_name LIKE %s"
				params.append('%' + supp_name + '%')

			if supp_trade_register:
				query += " AND supp_trade_register LIKE %s"
				params.append('%' + supp_trade_register + '%')

			if supp_year:
				query += " AND supp_year LIKE %s"
				params.append('%' + supp_year + '%')

			if supp_cif:
				query += " AND supp_cif LIKE %s"
				params.append('%' + supp_cif + '%')

			if supp_headquarter:
				query += " AND supp_headquarter LIKE %s"
				params.append('%' + supp_headquarter + '%')

			if supp_county:
				query += " AND supp_county LIKE %s"
				params.append('%' + supp_county + '%')

			if supp_social_capital:
				query += " AND supp_social_capital LIKE %s"
				params.append('%' + supp_social_capital + '%')

			if supp_iban:
				query += " AND supp_iban LIKE %s"
				params.append('%' + supp_iban + '%')

			if supp_bank:
				query += " AND supp_bank LIKE %s"
				params.append('%' + supp_bank + '%')

			if supp_email:
				query += " AND supp_email LIKE %s"
				params.append('%' + supp_email + '%')


			cursor.execute(query, params)
			rows = cursor.fetchall()


			custom_headers = ["Nr.Crt.", "Name", "Trade register", "Year", "CIF", "Headquarter",
			                  "County", "Social capital", "IBAN", "Bank", "Email"]
			self.load_data_to_table(rows, custom_headers)
			self.table_result.sortItems(1, Qt.SortOrder.AscendingOrder)

		except Exception as e:
			print(f"Eroare la interogarea bazei de date: {e}")

		finally:
			if cursor:
				cursor.close()
			if conn:
				conn.close()

	def load_data_to_table(self, rows, headers):
		self.table_result.clear()
		self.table_result.setRowCount(len(rows))
		self.table_result.setHorizontalHeaderLabels(headers)

		for row_idx, row_data in enumerate(rows):
			for col_idx, value in enumerate(row_data):
				item = QTableWidgetItem(str(value))
				item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
				self.table_result.setItem(row_idx, col_idx, item)

	def table_row_double_clicked(self, row):
		# Ai grijă să potrivești indecsi cu structura tabelului tău!
		self.supplier_field.supplier_name_input.setText(self.table_result.item(row, 1).text())
		self.supplier_field.supplier_name_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.supplier_field.register_number_input.setText(self.table_result.item(row, 2).text())
		self.supplier_field.register_number_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.supplier_field.register_year_input.setText(self.table_result.item(row, 3).text())
		self.supplier_field.register_year_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.supplier_field.cui_cif_input.setText(self.table_result.item(row, 4).text())
		self.supplier_field.headquarters_input.setText(self.table_result.item(row, 5).text())
		self.supplier_field.county_input.setText(self.table_result.item(row, 6).text())
		self.supplier_field.social_capital_input.setText(self.table_result.item(row, 7).text())
		self.supplier_field.iban_code_input.setText(self.table_result.item(row, 8).text())
		self.supplier_field.supplier_bank_input.setText(self.table_result.item(row, 9).text())
		self.supplier_field.supplier_email_input.setText(self.table_result.item(row, 10).text())


	def clear_all_data(self):
		self.supplier_field.supplier_name_input.clear()
		self.supplier_field.register_number_input.clear()
		self.supplier_field.register_year_input.clear()
		self.supplier_field.cui_cif_input.clear()
		self.supplier_field.headquarters_input.clear()
		self.supplier_field.county_input.clear()
		self.supplier_field.social_capital_input.clear()
		self.supplier_field.iban_code_input.clear()
		self.supplier_field.supplier_bank_input.clear()
		self.supplier_field.supplier_email_input.clear()

	def modify_btn_pressed(self):

		select_row = self.table_result.currentRow()

		if select_row == -1:
			print("nici un rand selectat")
			search_supplier_message.nothing_selected(self)
			return False

		supplier_id = self.table_result.item(select_row, 0).text()

		supplier_name = self.supplier_field.supplier_name_input.text().strip()

		if not supplier_name:
			search_supplier_message.name_empty(self)
			return False
		if len(supplier_name) >= 50:
			search_supplier_message.name_len(self)
			return False

		supplier_register_number = self.supplier_field.register_number_input.text().strip()

		if supplier_register_number == "":
			search_supplier_message.trade_register_empty(self)
			return False
		if len(supplier_register_number) < 14:
			search_supplier_message.registration_len_smaller(self)
			return False
		if len(supplier_register_number) > 14:
			search_supplier_message.registration_len_bigger(self)
			return False
		prefix = supplier_register_number[0].upper()
		number_part = supplier_register_number[1:]
		if not prefix.isalpha():
			search_supplier_message.code_let(self)
			return False
		if not number_part.isnumeric():
			search_supplier_message.code_num(self)
			return False
		valid_prefixes = ["J", "F", "C"]
		if prefix not in valid_prefixes:
			search_supplier_message.cod_beg(self)
			return False
		if len(number_part) != 13:
			print(len(number_part))
			search_supplier_message.registr_wrong_len(self)
			return False

		supplier_year = self.supplier_field.register_year_input.text().strip()

		year = date.today().year
		try:
			if supplier_year == "":
				search_supplier_message.year_empty(self)
				return False
			if not len(supplier_year) == 4:
				search_supplier_message.year_len(self)
				return False
			supp_year = int(self.supplier_field.register_year_input.text())
			if supp_year > year:
				search_supplier_message.year_valid(self)
				return False

		except ValueError:
			search_supplier_message.year_format(self)
			return False

		supplier_cif = self.supplier_field.cui_cif_input.text().strip()

		supp_cif_letter = supplier_cif[:2]
		supp_cif_number = supplier_cif[2:]
		supp_cif = supp_cif_letter.upper() + supp_cif_number

		if supplier_cif == "":
			search_supplier_message.cif_empty(self)
			return False

		if not supp_cif_letter.isalpha():
			search_supplier_message.cif_letter(self)
			return False
		if not supp_cif_number.isnumeric():
			search_supplier_message.cif_number(self)
			return False
		if len(supp_cif) > 12:
			search_supplier_message.cif_length(self)
			return False

		supplier_headquarter = self.supplier_field.headquarters_input.text().strip()

		if supplier_headquarter == "":
			search_supplier_message.headquarter_empty(self)
			return False
		elif len(supplier_headquarter) > 30:
			search_supplier_message.headquarter_len(self)
			return False

		supplier_county = self.supplier_field.county_input.text().strip()

		if supplier_county == "":
			search_supplier_message.county_empty(self)
			return False
		if len(supplier_county) > 50:
			search_supplier_message.county_len(self)
			return False

		supplier_social_capital = self.supplier_field.social_capital_input.text().strip()

		if supplier_social_capital == "":
			search_supplier_message.capital_empty(self)
			return False
		if not supplier_social_capital.isnumeric():
			search_supplier_message.capital_number(self)
			return False
		if len(supplier_social_capital) > 10:
			search_supplier_message.capital_len(self)
			return False

		supplier_iban = self.supplier_field.iban_code_input.text().strip()

		supp_iban_length = len(supplier_iban)

		if supplier_iban == "":
			search_supplier_message.iban_empty(self)
			return False

		if not 14 <= supp_iban_length <= 34:
			search_supplier_message.iban_len(self)
			return False

		country_code = supplier_iban[:2]
		first_2_numbers = supplier_iban[2:4]
		bank_code = supplier_iban[4:8]
		ended_number = supplier_iban[8:]

		if (not country_code.isalpha() or not first_2_numbers.isnumeric() or not bank_code.isalpha()
				or not ended_number.isnumeric()):
			search_supplier_message.valid_iban(self)
			return False

		supplier_bank = self.supplier_field.supplier_bank_input.text().strip()

		if supplier_bank == "":
			search_supplier_message.bank_empty(self)
			return False
		if len(supplier_bank) >= 34:
			search_supplier_message.bank_len(self)
			return False

		supplier_email = self.supplier_field.supplier_email_input.text().strip()

		if supplier_email == "":
			search_supplier_message.email_empty(self)
			return False

		str_supp_email = str(supplier_email)

		if len(str_supp_email) > 30:
			search_supplier_message.email_len(self)
			return False

		conn = get_db_connection()

		cursor = conn.cursor()
		script_update_row = ("""
        UPDATE supplier
        SET 
                supp_name = %s, 
                supp_trade_register = %s,
                supp_year = %s,
                supp_cif = %s, 
                supp_headquarter = %s,
                supp_county = %s,
                supp_social_capital = %s, 
                supp_iban = %s, 
                supp_bank = %s,
                supp_email = %s
        WHERE
                supp_id = %s
                """)
		data_to_update_row = (supplier_name, supplier_register_number, supplier_year, supplier_cif, supplier_headquarter,
		                      supplier_county, supplier_social_capital, supplier_iban, supplier_bank, supplier_email,
		                      supplier_id)

		cursor.execute(script_update_row, data_to_update_row)

		conn.commit()

		conn.close()

		search_supplier_message.successfully_saved(self)

		self.table_result.clear()
		self.clear_all_data()

	def delete_btn_pressed(self):

		selected_row = self.table_result.currentRow()

		if selected_row == -1:
			search_supplier_message.nothing_selected(self)
			return

		confirm = QMessageBox.question(self, "Please confirm!", "Are you sure?",
		            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

		if confirm != QMessageBox.StandardButton.Yes:
			return

		supplier_id = self.table_result.item(selected_row, 0).text()

		conn = get_db_connection()
		cursor = conn.cursor()

		script_to_delete = ("""
        DELETE FROM supplier
        WHERE supp_id = %s
        """ )

		cursor.execute(script_to_delete, supplier_id)

		conn.commit()
		cursor.close()

		conn.close()

		search_supplier_message.successfully_deleted(self)

		self.table_result.clear()
		self.clear_all_data()




