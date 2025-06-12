import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget
from Tab_uri.Invoice.AddInvoice.add_invoice import AddInvoice
from Tab_uri.Invoice.ReleaseInvoice.relese_invoice import ReleaseInvoice


class Invoice(QMainWindow):
	def __init__(self):
		super().__init__()

		self.showMaximized()

		self.tabs = QTabWidget()
		self.setCentralWidget(self.tabs)

		self.tab_add_invoice = AddInvoice()
		self.tabs.addTab(self.tab_add_invoice, "Add Invoice")

		self.tab_release_invoice = ReleaseInvoice()
		self.tabs.addTab(self.tab_release_invoice, "Release Invoice")






if __name__ == "__main__":
	app = QApplication()
	windows = Invoice()
	windows.show()
	sys.exit(app.exec())
