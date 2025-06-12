from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Qt

def logo_image_and_contact_detail():
	logo_label = QLabel()
	logo = QPixmap("../static/my_logo40x40.png")
	logo_label.setPixmap(logo)
	logo_label.setStyleSheet("background-color: transparent;")

	logo_label.setToolTip("        by Niculae Dragos, \n"
	                    "               contact at: \n "
	                    " niculaedragos@gmail.com")
	logo_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
	return logo_label

# TODO de importat acest fisier in toate locurile unde avem logo