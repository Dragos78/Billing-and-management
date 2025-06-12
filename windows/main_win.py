import sys

from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget
from PySide6.QtWidgets import QStatusBar
from Tab_uri.prezentare import Prezentare
from Tab_uri.Aquisition.acquisitions import Acquisition
from Tab_uri.Invoice.invoice import Invoice
from Tab_uri.Invoice.AddInvoice import your_company_data
from Tab_uri.Orders.orders import OrdersTab


class MainWin(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Main window")
		self.setWindowIcon(QIcon("../static/my_logo.png"))
		self.setMinimumSize(1240, 800)
		self.showMaximized()



		# Create MenuBar
		menu_bar = self.menuBar()
		file_menu = menu_bar.addMenu("File")

		#Create File menu
		exit_action = file_menu.addAction("Exit")
		exit_action.triggered.connect(self.close)

		#Create Edit meniu
		edit_menu = menu_bar.addMenu("Edit")
		company_data_action = edit_menu.addAction("Setting company data")
		company_data_action.triggered.connect(self.open_company_data_dialog)

		# definirea Taburilor
		self.tabs = QTabWidget()
		self.setCentralWidget(self.tabs)

		# adaugare Tab prezentare
		self.tab_prezentare = Prezentare()
		self.tabs.addTab(self.tab_prezentare, "Prezentare")

		self.tab_acquisition = Acquisition()
		self.tabs.addTab(self.tab_acquisition, "Acquisition")

		self.tab_orders = OrdersTab()
		self.tabs.addTab(self.tab_orders, "Orders")

		self.tab_invoice = Invoice()
		self.tabs.addTab(self.tab_invoice, "Invoice")

		# self.tabs.currentChanged.connect(self.tabs_changed) # aici se ia semnalul de schimbare a tabului si se conecteaza la functia care nu este creata

	# @Slot(int)
	# def tabs_changed(self, index):
	# 	if index == 0:
	# 		pass
	# 		# print("tab1 a fost activat")
	#
	# 	elif index == 1:
	# 		pass
	# 		# print("tab2 a fost activat")
	#
	# 	elif index == 2:
	# 		pass
	# 		# print("tab3 a fost activat")
	# 		# self.tab_orders.on_tab_activated()
	# 	elif index == 3:
	# 		pass
	# 		# print("tab4 a fost activat")

		# return index

	def open_company_data_dialog(self):
		data = your_company_data.YourCompanyData()
		data.exec()
		
		# Create StatusBar
		status_bar = QStatusBar()
		status_bar.showMessage("Dragos")

		status_bar.setStyleSheet("""
		font: 15px;
		""")
		self.setStatusBar(status_bar)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWin()
	window.show()
	sys.exit(app.exec())
