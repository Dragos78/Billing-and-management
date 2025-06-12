from datetime import date

from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Qt
import psycopg2

from Messages import add_supplier_messages
from not_repet_code.supplier_widget import SupplierWidget
from not_repet_code.connect_database import get_db_connection
from not_repet_code.logo_and_contact_detail import logo_image_and_contact_detail



class AddSupplier(QWidget):
    def __init__(self):
        super().__init__()
        self.supplier_field = SupplierWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.supplier_field)

        self.save_btn = QPushButton("Save")
        self.save_btn.setFixedSize(70, 20)
        self.save_btn.clicked.connect(self.save_button_pressed)

        center_layout = QHBoxLayout()
        center_layout.addStretch()
        center_layout.addWidget(self.save_btn)
        center_layout.addStretch()

        layout.addLayout(center_layout)

        self.logo = logo_image_and_contact_detail()
        self.logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.logo)

        self.setLayout(layout)


    @staticmethod
    def conn():
        return get_db_connection()

    def ensure_table_exists(self):
        conn = self.conn()

        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS supplier (
                supp_id SERIAL PRIMARY KEY,
                supp_name VARCHAR(50),
                supp_trade_register VARCHAR(14),
                supp_year NUMERIC(4),
                supp_cif VARCHAR(12),
                supp_headquarter VARCHAR(30),
                supp_county VARCHAR(50),
                supp_social_capital NUMERIC(10),
                supp_iban VARCHAR(34),
                supp_bank VARCHAR(20),
                supp_email VARCHAR(30)
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()

    def validate_name(self):
        try:
            supp_name = self.supplier_field.supplier_name_input.text()

            if supp_name == "":
                add_supplier_messages.supp_name_empty(self)
                return False

            elif len(supp_name) > 50:
                add_supplier_messages.supp_name_length(self)
                return False

            return True

        except ValueError:
            add_supplier_messages.invalid_name_format(self)
            return False

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

    def check_registration_number_exists(self, supp_trade_register):
        self.ensure_table_exists()

        conn = self.conn()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM supplier WHERE supp_trade_register = %s
        """, (supp_trade_register,))
        exists = cursor.fetchone() is not None

        cursor.close()
        conn.close()
        return exists

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

    def check_supp_cif_exists(self, supp_cif):
        self.ensure_table_exists()

        conn = self.conn()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM supplier WHERE supp_cif = %s
        """, (supp_cif,))
        exists = cursor.fetchone() is not None

        cursor.close()
        conn.close()
        return exists

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

        if supp_email =="":
            add_supplier_messages.supp_email_empty(self)
            return False

        str_supp_email = str(supp_email)
        if len(str_supp_email) > 30:
            add_supplier_messages.supp_email_len(self)
            return False
        return True

    def save_button_pressed(self):

        supp_name = self.supplier_field.supplier_name_input.text()
        supp_trade_register = self.supplier_field.register_number_input.text()
        supp_year = self.supplier_field.register_year_input.text()
        supp_cif = self.supplier_field.cui_cif_input.text()
        supp_headquarter = self.supplier_field.headquarters_input.text()
        supp_county = self.supplier_field.county_input.text()
        supp_social_capital = self.supplier_field.social_capital_input.text()
        supp_iban = self.supplier_field.iban_code_input.text()
        supp_bank = self.supplier_field.supplier_bank_input.text()
        supp_email = self.supplier_field.supplier_email_input.text()

        # mesajele se trimit din functie
        if not self.validate_name():
            return
        elif not self.validate_registration_number():
            return
        elif not self.validate_year():
            return
        elif not self.validate_cif():
            return
        elif not self.validate_headquarter():
            return
        elif not self.validate_county():
            return
        elif not self.validate_capital():
            return
        elif not self.validate_iban():
            return
        elif not self.validate_bank():
            return
        elif not self.validate_email():
            return
        elif self.check_registration_number_exists(supp_trade_register):
            add_supplier_messages.registration_number_exists(self)
            return

        elif self.check_supp_cif_exists(supp_cif):
            add_supplier_messages.cif_exists(self)
            return
        else:
            self.ensure_table_exists()
            conn = self.conn()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO supplier (
                    supp_name, supp_trade_register, supp_year,
                    supp_cif, supp_headquarter, supp_county,
                    supp_social_capital, supp_iban, supp_bank,
                    supp_email
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                supp_name, supp_trade_register, supp_year,
                supp_cif, supp_headquarter, supp_county,
                supp_social_capital, supp_iban, supp_bank,
                supp_email
            ))
            conn.commit()
            cursor.close()
            conn.close()

            add_supplier_messages.save_succes(self)
            self.supplier_field.clear_qline_edit_content()



