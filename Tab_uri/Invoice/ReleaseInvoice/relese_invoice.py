from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton,
    QScrollArea
)
from PySide6.QtGui import Qt
from Tab_uri.Invoice.ReleaseInvoice.release_invoice_supplier_field import SupplierCompanyField
from Tab_uri.Invoice.AddInvoice.your_company_logo import your_company_logo
from Tab_uri.Invoice.AddInvoice.invoice_your_company_field import YourCompanyField
from Tab_uri.Invoice.AddInvoice.serial_nomber_invoice import TitleInvoice
from Tab_uri.Invoice.AddInvoice.a4_page_watermark import A4Page

from ussed_table.invoice_product_table import product_table


class ReleaseInvoice(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()

#TODO de modificat adica dispar datele companiei care cumpara, logo-ul si de facut combobox pt furnizor

        # ======== Scroll Area pentru coală A4 + conținut ========
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        # Widget container pentru scroll
        container = QWidget()
        scroll.setWidget(container)

        # Layout vertical pentru containerul scrolabil
        container_layout = QVBoxLayout(container)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # ======== Pagina A4 ca chenar ======== 1123)
        a4_page = A4Page()
        a4_page.setFixedSize(900, 1300)  # Dimensiune A4 la 96 DPI
        a4_page.setStyleSheet("QFrame {  background-color: transparent; }")

        # Layout intern pentru pagina A4
        page_layout = QVBoxLayout(a4_page)

        page_layout.setContentsMargins(10, 0, 10, 0)

        # Antet factură
        layout_antet = QHBoxLayout()

        self.supplier_field = SupplierCompanyField()
        self.supplier_field.setFixedWidth(300)
        self.supplier_field.setFixedHeight(190)
        layout_antet.addWidget(self.supplier_field)

        self.your_logo = your_company_logo()
        self.your_logo.setFixedSize(150, 150)  # Dimensiuni mai mici pentru logo
        self.your_logo.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        layout_antet.addWidget(self.your_logo)

        self.your_company_field = YourCompanyField()
        self.your_company_field.setFixedWidth(300)
        self.your_company_field.setFixedHeight(190)
        layout_antet.addWidget(self.your_company_field)

        page_layout.addLayout(layout_antet)

        # Titlu factură
        self.title = TitleInvoice()
        self.title.setFixedHeight(160)
        self.title.setFixedWidth(300)


        layout_title = QVBoxLayout()
        layout_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_title.addWidget(self.title)

        page_layout.addLayout(layout_title)

        layout_vat_and_table_label = QGridLayout()
        layout_vat_and_table_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_vat_and_table_label.setContentsMargins(16, 0, 30, 0)
        layout_vat_and_table_label.setSpacing(0)


        lbl_vat = QLabel("Cota TVA: 19%")
        lbl_vat.setFixedHeight(23)
        layout_vat_and_table_label.addWidget(lbl_vat, 0, 0, 1, 2)

        lbl_nr_crt = QLabel("Ite.No")
        lbl_nr_crt.setFixedWidth(45)
        lbl_nr_crt.setFixedHeight(23)
        lbl_nr_crt.setStyleSheet("border: 1px solid black;")
        layout_vat_and_table_label.addWidget(lbl_nr_crt, 1, 0)

        lbl_denumire_produs = QLabel("Name of products or services")
        lbl_denumire_produs.setFixedWidth(298)
        lbl_denumire_produs.setFixedHeight(23)
        lbl_denumire_produs.setStyleSheet("border: 1px solid black;")
        lbl_denumire_produs.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_vat_and_table_label.addWidget(lbl_denumire_produs, 1, 1)

        lbl_um = QLabel("U.M.")
        lbl_um .setFixedWidth(45)
        lbl_um.setFixedHeight(23)
        lbl_um.setStyleSheet("border: 1px solid black;")
        lbl_um.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_vat_and_table_label.addWidget(lbl_um, 1, 2)

        lbl_quantity = QLabel("Quantity")
        lbl_quantity.setFixedWidth(65)
        lbl_quantity.setFixedHeight(23)
        lbl_quantity.setStyleSheet("border: 1px solid black")
        lbl_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_vat_and_table_label.addWidget(lbl_quantity, 1, 3)

        lbl_unit_price = QLabel("Unit price")
        lbl_unit_price.setFixedWidth(80)
        lbl_unit_price.setFixedHeight(23)
        lbl_unit_price.setStyleSheet("border: 1px solid black")
        lbl_unit_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_vat_and_table_label.addWidget(lbl_unit_price, 1, 4)

        lbl_value = QLabel("Value")
        lbl_value.setFixedWidth(145)
        lbl_value.setFixedHeight(23)
        lbl_value.setStyleSheet("border: 1px solid black")
        lbl_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_vat_and_table_label.addWidget(lbl_value, 1, 5)

        lbl_vat = QLabel("VAT")
        lbl_vat.setFixedWidth(150)
        lbl_vat.setFixedHeight(23)
        lbl_vat.setStyleSheet("border: 1px solid black")
        lbl_vat.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_vat_and_table_label.addWidget(lbl_vat, 1, 6)

        page_layout.addLayout(layout_vat_and_table_label)



        # Tabel produse
        table = product_table()
        table.setFixedSize(850, 700)
        table.verticalHeader().setVisible(False)
        page_layout.addWidget(table, alignment=Qt.AlignmentFlag.AlignCenter)

        layout_footer = QGridLayout()
        layout_footer.setSpacing(0)
        layout_footer.setContentsMargins(13, 0, 25, 0)

        lbl_signature = QLabel("Signature and  \n"
                               "stamp of the supplier:")
        lbl_signature.setStyleSheet("border: 1px solid black")
        lbl_signature.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout_footer.addWidget(lbl_signature, 0, 0, 2, 1)

        lbl_delegat = QLabel("Delegat name: \n"
                             "Delegat ID: \n"
                             "Signature: ")
        lbl_delegat.setStyleSheet("border: 1px solid black")
        lbl_delegat.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout_footer.addWidget(lbl_delegat, 0, 1, 2, 1)

        lbl_total = QLabel("TOTAL:")
        lbl_total.setStyleSheet("border: 1px solid black")
        lbl_total.setAlignment(Qt.AlignmentFlag.AlignRight)
        lbl_total.setFixedWidth(230)
        layout_footer.addWidget(lbl_total, 0, 2)


        lbl_total_value = QLabel("")
        lbl_total_value.setStyleSheet("border: 1px solid black")
        layout_footer.addWidget(lbl_total_value, 0, 3)

        lbl_total_vat = QLabel("")
        lbl_total_vat.setStyleSheet("border: 1px solid black")
        layout_footer.addWidget(lbl_total_vat, 0, 4)

        lbl_general_total = QLabel("GENERAL TOTAL: ")
        lbl_general_total.setStyleSheet("border: 1px solid black")
        lbl_general_total.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout_footer.addWidget(lbl_general_total, 1, 2)

        lbl_general_total_result = QLabel("")
        lbl_general_total_result.setStyleSheet("border: 1px solid black")
        layout_footer.addWidget(lbl_general_total_result, 1, 3, 1, 2)


        page_layout.addLayout(layout_footer)

        # Buton salvare în pagina A4
        layout_btn = QHBoxLayout()
        self.btn_save = QPushButton("Save")
        self.btn_save.setFixedSize(150, 25)
        layout_btn.addStretch()
        layout_btn.addWidget(self.btn_save)
        layout_btn.addStretch()
        page_layout.addLayout(layout_btn)

        lbl_empty = QLabel("   ")
        layout_btn.addWidget(lbl_empty)


        # Adaugă pagina A4 în layoutul containerului
        container_layout.addWidget(a4_page, alignment=Qt.AlignmentFlag.AlignCenter)

        # ======== Layout principal pentru fereastră ========
        layout_main = QVBoxLayout(self)
        layout_main.addWidget(scroll)
