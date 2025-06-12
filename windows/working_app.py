import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QLabel, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon

from not_repet_code.logo_and_contact_detail import logo_image_and_contact_detail


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.log_in_window = None
		self.register_window = None
		self.setWindowTitle("My App")
		self.setGeometry(600, 200, 300, 300)
		self.setWindowIcon(QIcon("../static/my_logo.png"))

		self.layout = QGridLayout()

		self.question = QLabel("Please Register or Log-in")
		self.question.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.layout.addWidget(self.question,3, 2, 1, 4)

		self.register_button = QPushButton("Register")
		self.register_button.setCheckable(True) # schimba culoarea butonului cand este apasat
		self.register_button.clicked.connect(self.register_is_pressed) # conectarea cu functia de deschiderea a ferestrei de inregistrare
		self.layout.addWidget(self.register_button, 4, 3)

		self.log_in_button = QPushButton("Log-in")
		self.log_in_button.setCheckable(True) # schimba culoarea butonului cand este apasat
		self.log_in_button.clicked.connect(self.log_in_pressed) # conectarea cu functia de deschidere a ferestrei
		self.layout.addWidget(self.log_in_button, 4, 4)

		from not_repet_code.logo_and_contact_detail import logo_image_and_contact_detail
		self.logo = logo_image_and_contact_detail()
		self.layout.addWidget(self.logo, 5, 5, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

		widget = QWidget()
		widget.setLayout(self.layout)
		self.setCentralWidget(widget)

	def register_is_pressed(self):
		from register_window import Register
		self.register_window = Register()
		self.register_window.closeEvent = self.on_register_close
		self.register_window.show()
		self.close()

	def log_in_pressed(self):
		from log_in_window import LogIn
		self.log_in_window = LogIn()
		self.log_in_window.show()
		self.close()

	def on_register_close(self, event):
		from log_in_window import LogIn
		self.log_in_window = LogIn()
		self.log_in_window.show()
		self.close()
		event.accept()



if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())