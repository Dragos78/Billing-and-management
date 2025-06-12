from PySide6.QtWidgets import QTableWidget

def product_table():
	table = QTableWidget()

	table.setRowCount(27)
	table.setColumnCount(7)
	table.setHorizontalHeaderLabels(["0", "1", "2", "3",
	                                 "4", "5", "6"])
	table.setColumnWidth(0, 45)
	table.setColumnWidth(1, 298)
	table.setColumnWidth(2, 45)
	table.setColumnWidth(3, 65)
	table.setColumnWidth(4, 80)
	table.setColumnWidth(5, 150)
	table.setColumnWidth(6, 150)

	return table

