
def validate_name(supplier_name):
	if supplier_name == "":
		return False
	elif len(supplier_name) >= 50:
		return False
	return True


def validate_registration_number(self):
	registration_number = self.supplier_field.register_number_input.text()
	supp_trade_register = self.supplier_field.register_number_input.text()
	if supp_trade_register == "":
		add_supplier_messages.supp_trade_register_empty(self)
		return False

	if len(registration_number) < 14:
		add_supplier_messages.registration_length_smaller(self)
		return False

	if len(registration_number) > 14:
		add_supplier_messages.registration_length_bigger(self)
		return False

	prefix = registration_number[0].upper()
	number_part = registration_number[1:]

	if not prefix.isalpha():
		add_supplier_messages.code_letter(self)
		return False

	if not number_part.isnumeric():
		add_supplier_messages.code_number(self)
		return False

	valid_prefixes = ["J", "F", "C"]
	if prefix not in valid_prefixes:
		add_supplier_messages.cod_began(self)
		return False

	if len(number_part) != 13:
		print(len(number_part))
		add_supplier_messages.registration_wrong_length(self)
		return False

	return True


def validate_year(self):
	year = date.today().year
	supp_year = self.supplier_field.register_year_input.text()
	try:
		if supp_year == "":
			add_supplier_messages.supp_year_empty(self)
		if not len(supp_year) == 4:
			add_supplier_messages.supp_year_length(self)
		supp_year = int(self.supplier_field.register_year_input.text())
		if supp_year > year:
			add_supplier_messages.validate_year_message(self)

	except ValueError:
		add_supplier_messages.invalid_year_format(self)
		return False

	return True


def validate_cif(self):
	supp_cif = self.supplier_field.cui_cif_input.text()
	supp_cif_letter = supp_cif[:2]
	supp_cif_number = supp_cif[2:]
	supp_cif = supp_cif_letter.upper() + supp_cif_number

	if supp_cif == "":
		add_supplier_messages.supp_cif_empty(self)
		return False

	if not supp_cif_letter.isalpha():
		add_supplier_messages.supp_cif_letter(self)
		return False
	if not supp_cif_number.isnumeric():
		add_supplier_messages.supp_cif_number(self)
		return False
	if len(supp_cif) > 12:
		add_supplier_messages.supp_cif_length(self)
		return False
	return True


def validate_iban(self):
	supp_iban = self.supplier_field.iban_code_input.text()

	supp_iban_length = len(supp_iban)

	if supp_iban == "":
		add_supplier_messages.supp_iban_empty(self)
		return False

	if not 14 <= supp_iban_length <= 34:
		add_supplier_messages.supp_iban_length(self)
		return False

	country_code = supp_iban[:2]
	first_2_numbers = supp_iban[2:4]
	bank_code = supp_iban[4:8]
	ended_number = supp_iban[8:]

	if (not country_code.isalpha() or not first_2_numbers.isnumeric() or not bank_code.isalpha()
			or not ended_number.isnumeric()):
		add_supplier_messages.validate_iban(self)
		return False

	return True


def validate_headquarter(self):
	supp_headquarter = self.supplier_field.headquarters_input.text()
	if supp_headquarter == "":
		add_supplier_messages.supp_headquarter_empty(self)
		return False
	elif len(supp_headquarter) > 30:
		add_supplier_messages.supp_headquarter_length(self)
		return False
	return True


def validate_county(self):
	supp_county = self.supplier_field.county_input.text()
	if supp_county == "":
		add_supplier_messages.supp_county_empty(self)
		return False
	if len(supp_county) > 50:
		add_supplier_messages.supp_county_length(self)
		return False
	return True


def validate_capital(self):
	supp_social_capital = self.supplier_field.social_capital_input.text()
	if supp_social_capital == "":
		add_supplier_messages.social_capital_empty(self)
		return False
	if not supp_social_capital.isnumeric():
		add_supplier_messages.social_capital_number(self)
		return False
	if len(supp_social_capital) > 10:
		add_supplier_messages.social_capital_len(self)
		return False
	return True


def validate_bank(self):
	supp_bank = self.supplier_field.supplier_bank_input.text()
	if supp_bank == "":
		add_supplier_messages.supp_bank_empty(self)
		return False
	if len(supp_bank) >= 34:
		add_supplier_messages.supp_bank_len(self)
		return False
	return True


def validate_email(self):
	supp_email = self.supplier_field.supplier_email_input.text()

	if supp_email == "":
		add_supplier_messages.supp_email_empty(self)
		return False

	str_supp_email = str(supp_email)
	if len(str_supp_email) > 30:
		add_supplier_messages.supp_email_len(self)
		return False
	return True

