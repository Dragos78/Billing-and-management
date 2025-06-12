from PySide6.QtWidgets import QMessageBox

# name
def supp_name_empty(self):
	QMessageBox.warning(self, "Error on name", "Supplier name cannot be empty!")

def supp_name_length(self):
	QMessageBox.information(self, "Attention", "The name length cannot be longer than 50 characters.")

def invalid_name_format(self):
	QMessageBox.warning(self, "Error - name", "Invalid name format!")

# trade register
def supp_trade_register_empty(self):
	QMessageBox.warning(self, "Error", "Supplier trade register cannot be empty!")

def supp_reg_number_length(self):
	QMessageBox.information(self, "Attention", "The registration number length cannot be longer than 14 characters.")

# validate registration number
def cod_began(self):
	QMessageBox.information(self, "Registration number", "The code must start with one of the letters: J, F or C ")

def registration_length_smaller(self):
	QMessageBox.information(self, "Too short", "Registration number is to short")

def registration_length_bigger(self):
	QMessageBox.information(self, "Too long", "Registration number is to long")

def registration_wrong_length(self):
	QMessageBox.information(self, "Registration number", "The number entered in register number field is smaller or bigger then legal")

def	code_number(self):
	QMessageBox.information(self, "registration number", "The number entered in register number field must contain just number")
def registration_number_exists(self):
	QMessageBox.warning(self, "Error - register", "Registration number exist in database!")
def code_letter(self):
	QMessageBox.information(self, "Code Letter registration number", "The code must start with a letter")

# validate year
def supp_year_empty(self):
	QMessageBox.warning(self, "Error year", "Supplier year of registration cannot be empty!")

def supp_year_length(self):
	QMessageBox.information(self, "Attention year", "The year length cannot be more or less than 4 digits.")

def validate_year_message(self):
	QMessageBox.warning(self, "Error year", " The year you entered dont be more then current year")

def invalid_year_format(self):
	QMessageBox.information(self, "Attention Year", "The year format is not ok")



# cif
def supp_cif_empty(self):
	QMessageBox.warning(self, "Error CIF", "Supplier CIF cannot be empty!")

def supp_cif_length(self):
	QMessageBox.information(self, "Attention CIF", "CUI length cannot be longer than 12 characters.")

def supp_cif_letter(self):
	QMessageBox.warning(self, "Error-CIF", "Prefix must be letter")

def cif_exists(self):
	QMessageBox.warning(self, "Error CIF", "CIF number exists in database")

def supp_cif_number(self):
	QMessageBox.warning(self, "Error-CIF", "CIF is not conform!")

# headquarter
def supp_headquarter_empty(self):
	QMessageBox.warning(self, "Error headquarter", "Supplier Headquarter cannot be empty!")

def supp_headquarter_length(self):
	QMessageBox.information(self, "Attention headquarter", "Headquarter length cannot be longer than 30 characters.")

# county
def supp_county_empty(self):
	QMessageBox.warning(self, "Error - county", "Supplier county cannot be empty!")

def supp_county_length(self):
	QMessageBox.information(self, "Attention county", "County length cannot be longer than 50 characters.")

# social capital
def social_capital_empty(self):
	QMessageBox.warning(self, "Error - capital", "Social capital can`t be empty!")
def social_capital_number(self):
	QMessageBox.warning(self, "Error - capital", "Social capital must be number")

def social_capital_len(self):
	QMessageBox.warning(self, "Error - capital", "The length not be more 10 character")
# iban
def supp_iban_empty(self):
	QMessageBox.warning(self, "Error - IBAN", "Supplier iban cannot be empty!")

def supp_iban_length(self):
	QMessageBox.information(self, "Attention - IBAN", "IBAN length do not respect the legal format.")

def iban_exist(self):
	QMessageBox.warning(self, "Error - IBAN", "Registration number exists in database.")


def validate_iban(self):
	QMessageBox.information(self, "Attention - IBAN", "The IBAN do nor respect the legal format")


# bank
def supp_bank_empty(self):
	QMessageBox.warning(self, "Error Bank", "Supplier Bank cannot be empty!")

def supp_bank_len(self):
	QMessageBox.warning(self, "Error Social Capital", "Is to long")


# email
def supp_email_empty(self):
	QMessageBox.warning(self, "Error email", "Supplier email is empty. "
	                                   "You cannot send the order if you do not fill in, the supplier's email address")
def supp_email_len(self):
	QMessageBox.warning(self, "Error - email", "Length can`t be mor than 30 character.")
# save
def save_succes(self):
	QMessageBox.information(self, "Succes - save", "Data was saved successfully!")





