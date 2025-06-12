from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Qt

def help_search_supplier():
# Information about search proces
	info_lbl = QLabel()
	info = QPixmap("../../static/question-mark_40x40.png")
	info_lbl.setPixmap(info)
	info_lbl.setStyleSheet("background-color: transparent;")
	info_lbl.setToolTip("                                                                          \n"
	                         "                        Information about search criteria :              \n"
	                         "          If you do not enter any criteria and press on 'Search' button \n"
	                         "          all record from database are displayed to result table     \n"
	                         "       1. You cand enter any criteria and press 'Search' button. \n"
	                         "       2. You make doubleclick on desired position in finding table result. \n"
	                         "       3. Modify the desired field you want and press save. \n"
	                         "       4. If you want to delete a record from the database, after double-clicking \n"
	                         "          on the result displayed in the results table, press the 'Delete' button. \n"
	                         "              Be careful , after record deleted you cannot undo the process. \n "
	                         "                                                                          \n")

	info_lbl.setAlignment((Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom))
	return info_lbl