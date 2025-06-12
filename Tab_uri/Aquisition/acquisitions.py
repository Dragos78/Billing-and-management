import sys
from PySide6.QtWidgets import (
	QApplication, QMainWindow, QTabWidget
)
from Tab_uri.Aquisition.addsupplier import AddSupplier
from Tab_uri.Aquisition.search_supplier import SearchSupplier


class Acquisition(QMainWindow):
	def __init__(self):
		super().__init__()

		self.showMaximized()  # Se deschide maximizată

		# definirea taburilor
		self.tabs = QTabWidget()
		self.setCentralWidget(self.tabs)

		# adaugarea tabului AddSupplier
		self.tab_add_supplier = AddSupplier()
		self.tabs.addTab(self.tab_add_supplier, "Add Supplier")

		# adaugarea tabului search supplier
		self.tab_search_supplier = SearchSupplier()
		self.tabs.addTab(self.tab_search_supplier, "Search supplier")

		self.tabs.currentChanged.connect(self.on_tab_changed)

	def on_tab_changed(self, index):
		if self.tabs.widget(index) is not self.tab_search_supplier:
			self.tab_search_supplier.table_result.clearContents()
			self.tab_search_supplier.clear_all_data()





if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Acquisition()
	window.show()
	sys.exit(app.exec())
