def last_order(self):
	# aici este codul pt a genera si afisa numarul de comanda cand se deschide fereastra

	order_type = self.combo_box_order_type.currentText()  # Se iau datele din order type OE sau OI

	# primul element al numarului de comanda:
	order_number_first_elem = order_type

	# mal doilea element al numarului de comanda

	connection = get_db_connection()
	cursor = connection.cursor()

	cursor.execute("""
	CREATE TABLE IF NOT EXISTS orders (
	id SERIAL PRIMARY KEY ,
	order_number VARCHAR (12),
	supplier_name VARCHAR (50),
	supplier_email VARCHAR (50),
	material VARCHAR (50),
	amount VARCHAR (9),
	description VARCHAR (150),
	date TIMESTAMP NOT NULL DEFAULT NOW());
	""")

	cursor.execute("SELECT COUNT(*) FROM orders WHERE order_number IS NOT NULL")
	count = cursor.fetchone()[0]

	if count > 0:
		cursor.execute("SELECT * FROM orders WHERE order_number IS NOT NULL ORDER BY id DESC LIMIT 1")
		last_row = cursor.fetchone()
		print(f"{last_row} - ultimul rand")
	connection.commit()
	cursor.close()
	connection.close()

	# al treilea element al numarului de comanda
	qdate = QtCore.QDate.currentDate()
	pydate = str(qdate.toPython())
	date = pydate[8:] + pydate[5] + pydate[6] + pydate[:4]
	order_num_third_elem = date  # al treile element al nr-lui de ordina

	self.lbl_view_order_number.setText(f"{order_number_first_elem}/{order_num_third_elem}")

