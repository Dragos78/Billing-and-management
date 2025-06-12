import sys
from operator import index

from PySide6.QtCore import Slot

from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QHBoxLayout, QGridLayout

from Tab_uri.Orders.add_orders import AddOrders


class OrdersTab(QMainWindow):
	def __init__(self):
		super().__init__()
		self.showMaximized()

		self.tab = QTabWidget()
		self.setCentralWidget(self.tab)


		self.tab_view = QTabWidget()
		self.tab.addTab(self.tab_view, "View")


		self.tab_add_order = AddOrders()
		self.tab.addTab(self.tab_add_order, "Add order")

		self.tab.currentChanged.connect(self.in_tab_orders_changed)


	#TODO aici se creaza tabelul unde se vad toate comenzile




	@Slot(int)
	def in_tab_orders_changed(self, index):
		if index == 0:
			pass
		elif index == 1:
			self.tab_add_order.on_tab_activated()
			print("A fost activat")
		return index




if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = OrdersTab()
	window.show()
	sys.exit(app.exec())

