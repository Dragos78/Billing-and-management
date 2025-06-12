import sys
import datetime
from PySide6.QtCore import QDate, Slot
from PySide6 import QtCore
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QGridLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit
                               , QPushButton)
from PySide6.QtGui import Qt
from not_repet_code.connect_database import get_db_connection


class AddOrders(QWidget):
	def __init__(self):
		super().__init__()
		self.showMaximized()


		layout_main = QVBoxLayout()

		layout_create_orders = QVBoxLayout()
		layout_create_orders.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

		# aici se poate crea si trimite comanda

		lbl_title = QLabel("Create and send order")
		lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		layout_create_orders.addWidget(lbl_title)

		lbl_empty = QLabel("")
		layout_create_orders.addWidget(lbl_empty)

		# aici sunt elementele din formularul de creare comanda

		layout_create_orders_element = QGridLayout()

		lbl_order_type = QLabel("Order type:")
		# lbl_order_type.setFixedWidth(250)
		layout_create_orders_element.addWidget(lbl_order_type, 0, 1)

		self.combo_box_order_type = QComboBox()
		combo_box_order_type_item = ["OE", "OI"]
		self.combo_box_order_type.addItems(combo_box_order_type_item)
		self.combo_box_order_type.setFixedWidth(60)
		self.combo_box_order_type.currentIndexChanged.connect(self.combo_box_order_type_changed)
		layout_create_orders_element.addWidget(self.combo_box_order_type, 0, 2)

		self.lbl_chosen_type = QLabel()
		self.lbl_chosen_type.setFixedWidth(500)
		self.lbl_chosen_type.setAlignment(Qt.AlignmentFlag.AlignCenter)
		layout_create_orders_element.addWidget(self.lbl_chosen_type, 0, 3)

		lbl_order_number = QLabel("Order number: ")
		layout_create_orders_element.addWidget(lbl_order_number, 1, 0)

		self.lbl_view_order_number = QLabel("Test")
		self.lbl_view_order_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
		layout_create_orders_element.addWidget(self.lbl_view_order_number, 1, 1)

		lbl_empty = QLabel()
		layout_create_orders_element.addWidget(lbl_empty, 2, 1)

		lbl_supplier_name = QLabel("Supplier name:")
		layout_create_orders_element.addWidget(lbl_supplier_name, 3, 1)

		self.supplier_name_chosen = QComboBox()
		supplier_name_combo = self.supplier_combo()
		self.supplier_name_chosen.addItems(supplier_name_combo)
		layout_create_orders_element.addWidget(self.supplier_name_chosen, 3, 2)

		lbl_ord_material = QLabel("Material: ")
		layout_create_orders_element.addWidget(lbl_ord_material, 4, 1)

		self.entry_ord_material = QLineEdit()
		self.entry_ord_material.setFixedWidth(500)
		self.entry_ord_material.setPlaceholderText("Material name, code product")
		layout_create_orders_element.addWidget(self.entry_ord_material, 4, 2)

		lbl_material_amount = QLabel("Amount:")
		layout_create_orders_element.addWidget(lbl_material_amount, 5, 1)

		self.entry_amount_material = QLineEdit()
		self.entry_amount_material.setFixedWidth(150)
		self.entry_amount_material.setAlignment(Qt.AlignmentFlag.AlignCenter)
		layout_create_orders_element.addWidget(self.entry_amount_material, 5, 2)

		lbl_material_description = QLabel("Description:")
		layout_create_orders_element.addWidget(lbl_material_description, 6, 1)

		self.entry_description_material = QLineEdit()
		self.entry_description_material.setFixedWidth(500)
		layout_create_orders_element.addWidget(self.entry_description_material, 6, 2)



		self.print = QPushButton("print")
		self.print.clicked.connect(self.supplier_combo)
		self.print.clicked.connect(self.afiseaza)
		layout_create_orders_element.addWidget(self.print, 7, 1)

# TODO de continuat cu construirea formularului de comanda si aranjarea in pagina
		#TODO de pus logoul pe pagina si pe pagina de vizualizare comenzi


		layout_create_orders.addLayout(layout_create_orders_element)


		layout_view_orders = QHBoxLayout()
		#aici o sa fie un table unde se va vedea statusul comenzilor
		# s-a mutat in tabul order




		layout_main.addLayout(layout_create_orders)
		layout_main.addLayout(layout_view_orders)
		self.setLayout(layout_main)

		self.combo_box_order_type_changed()

	@staticmethod
	def supplier_combo():
		connection = get_db_connection()
		cursor = connection.cursor()
		cursor.execute("""
		SELECT supp_name
		FROM SUPPLIER
		ORDER BY supp_name ASC
				         """)
		supplier_name_list = cursor.fetchall()
		supplier_name_combo = [row[0] for row in supplier_name_list]

		cursor.close()
		connection.close()
		return supplier_name_combo

#TODO sa nu uit sa fac validarile campurilor

	def combo_box_order_type_changed(self):
		combo_text = self.combo_box_order_type.currentText()
		if combo_text == "OE":
			self.lbl_chosen_type.setText("External order (to supplier)")
		else:
			self.lbl_chosen_type.setText("Internal order (from Teamleader)")

		self.on_tab_activated()

	def on_tab_activated(self):

		order_type = self.combo_box_order_type.currentText()  # OE sau OI
		order_number_first_elem = order_type

		# Data în format DDMMYYYY
		qdate = QtCore.QDate.currentDate()
		pydate = str(qdate.toPython())  # ex: '2025-06-03'
		order_num_third_elem = pydate[8:] + pydate[5] + pydate[6] + pydate[:4]  # ex: '03062025'

		# Obținem ultimul număr de comandă din baza de date
		connection = get_db_connection()
		cursor = connection.cursor()

		cursor.execute("""
	        CREATE TABLE IF NOT EXISTS orders (
	            id SERIAL PRIMARY KEY,
	            order_number VARCHAR(20),
	            order_status VARCHAR(10),
	            supplier_name VARCHAR(50),
	            material VARCHAR(50),
	            amount VARCHAR(9),
	            description VARCHAR(150),
	            date TIMESTAMP NOT NULL DEFAULT NOW()
	        );
	    """)

		cursor.execute("""
	        SELECT order_number 
	        FROM orders 
	        ORDER BY id DESC 
	        LIMIT 1
	    """)
		last_row = cursor.fetchone()

		connection.commit()
		cursor.close()
		connection.close()

		# Calculăm al doilea element (incrementul)
		if last_row is None or last_row[0] is None:
			int_order_num_second_elem = 1
		else:
			last_order_number = last_row[0]
			# Extragem cifrele de pe poziția 3 până la 6
			int_order_num_second_elem = int(last_order_number[3:6]) + 1

		# Formatare cu zerouri la început
		order_num_second_elem_str = str(int_order_num_second_elem).zfill(3)

		# Construim numărul de comandă complet
		order_number = f"{order_number_first_elem}/{order_num_second_elem_str}/{order_num_third_elem}"

		# Afișăm în interfață
		self.lbl_view_order_number.setText(order_number)
		# print(f"Număr comandă generat: {order_number}")

	def afiseaza(self):
		furnizorul_ales = self.supplier_name_chosen.currentText()
		print(furnizorul_ales)

