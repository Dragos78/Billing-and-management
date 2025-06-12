from PySide6.QtWidgets import QTableWidget

def table_result():
	tabel = QTableWidget()
	tabel.setRowCount(5)
	tabel.setColumnCount(11)
	tabel.setHorizontalHeaderLabels([
		"Nr.Crt.", "Name", "Trade register", "Year", "CIF", "Headquarter",
		"County", "Social capital", "IBAN", "Bank", "Email"])
	tabel.setColumnWidth(0, 50)
	tabel.setColumnWidth(1, 227)
	tabel.setColumnWidth(2, 125)
	tabel.setColumnWidth(3, 40)
	tabel.setColumnWidth(4, 80)
	tabel.setColumnWidth(5, 135)
	tabel.setColumnWidth(6, 120)
	tabel.setColumnWidth(7, 75)
	tabel.setColumnWidth(8, 200)
	tabel.setColumnWidth(9, 120)
	tabel.setColumnWidth(10, 200)

	return tabel