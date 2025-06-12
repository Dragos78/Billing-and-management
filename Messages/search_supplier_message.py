from PySide6.QtWidgets import QMessageBox

def nothing_selected(self):
	QMessageBox.warning(self, "Error", "Nothing was selected")

def successfully_saved(self):
	QMessageBox.information(self, "Congratulation", "The change has been saved.")

def successfully_deleted(self):
	QMessageBox.information(self, "Congratulation", "The record was been deleted.")

# validate name
def name_empty(self):
	QMessageBox.warning(self, "Error name", "Name can`t be empty!" )
def name_len(self):
	QMessageBox.warning(self, "Error name", "Name can`t have more then 50 character.")

# validate register_number
def trade_register_empty(self):
	QMessageBox.warning(self, "Error reg. num.", "Register number can`t be empty")
def registration_len_smaller(self):
	QMessageBox.warning(self, "Error reg. num.", "Register number is to short!")
def registration_len_bigger(self):
	QMessageBox.warning(self, "Error reg. num.", "Register number is to bigger!")
def code_let(self):
	QMessageBox.warning(self, "Error reg. num.", "Register number prefix must be letter!")
def code_num(self):
	QMessageBox.warning(self, "Error reg. num.", "The number entered in register number field must contain just number")
def cod_beg(self):
	QMessageBox.information(self, "Registration number", "The code must start with one of the letters: J, F or C ")
def registr_wrong_len(self):
	QMessageBox.information(self, "Registration number", "The number entered in register number field is smaller or bigger then legal")

# validate date
def year_empty(self):
	QMessageBox.warning(self, "Error year", "Year can`t be empty")
def year_len(self):
	QMessageBox.warning(self,"Error year", "The year length must have 4 character!")
def year_valid(self):
	QMessageBox.warning(self, "Error year", " The year you entered dont be more then current year")
def year_format(self):
	QMessageBox.information(self, "Attention Year", "The year format is not ok")
def year_number(self):
	QMessageBox.warning(self, "Error year", "The year format must be just number.")

# validate CIF
def cif_empty(self):
	QMessageBox.warning(self, "Error cif", "CIF can`t be empty.")
def cif_letter(self):
	QMessageBox.warning(self, "Error cif", "Cif prefix must be just letter.")
def cif_number(self):
	QMessageBox.warning(self, "Error cif", "Cfi number must bo just number")
def cif_length(self):
	QMessageBox.warning(self, "Error cif", "CIF length can`t excede 12 character.")

# validate headquarter
def headquarter_empty(self):
	QMessageBox.warning(self, "Error headquarter", "Headquarter can`t be empty.")
def headquarter_len(self):
	QMessageBox.warning(self, "Error headquarter", "Headquarter length can`t excede 30 character.")

# validate county
def county_empty(self):
	QMessageBox.warning(self, "Error county", "County can`t be empty.")
def county_len(self):
	QMessageBox.warning(self, "Error county", "County length can`t excede 50 character.")

# validate social capital
def capital_empty(self):
	QMessageBox.warning(self, "Error capital", "Social capital can`t be empty.")
def capital_number(self):
	QMessageBox.warning(self, "Error capital", "Social capital must be just number.")
def capital_len(self):
	QMessageBox.warning(self, "Error capital", "Social capital length can`t excede 10 character.")

# validate iban
def iban_empty(self):
	QMessageBox.warning(self, "Error IBAN", "Iban can`t be empty.")
def iban_len(self):
	QMessageBox.warning(self, "Error IBAN", "Iban length must be between 14 and 24 character.")
def valid_iban(self):
	QMessageBox.warning(self, "Attention - IBAN", "The IBAN do nor respect the legal format")

# validate bank
def bank_empty(self):
	QMessageBox.warning(self, "Error Bank", "Bank can`t be empty.")
def bank_len(self):
	QMessageBox.warning(self, "Error BANK", "Bank length can`t excede 34 character.")

# validate Email
def email_empty(self):
	QMessageBox.warning(self, "Error Email", "Email can`t be empty.")
def email_len(self):
	QMessageBox.warning(self, "Error Email", "Email length can`t excede 34 character.")



