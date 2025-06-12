from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class Prezentare(QWidget):
    def __init__(self):
        super().__init__()
        self.principal_grid = QGridLayout()

        from not_repet_code.logo_and_contact_detail import logo_image_and_contact_detail
        self.logo = logo_image_and_contact_detail()
        self.logo.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.principal_grid.addWidget(self.logo, 0, 0)

        self.title = QLabel("Pagina in lucru!!!")
        self.title.setStyleSheet("""
        font: 15px;
        """)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.principal_grid.addWidget(self.title, 0, 1)


        self.setLayout(self.principal_grid)

# Exemplar de rulare (doar dacă vrei să rulezi codul):
# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     window = Prezentare()
#     window.show()
#     sys.exit(app.exec())
