from PySide6.QtWidgets import QFrame
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtCore import Qt


class A4Page(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(900, 1300)
        self.watermark = QPixmap("../company_logo/company_logo.png").scaled(
            300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.opacity = 0.15  # foarte estompat

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setOpacity(self.opacity)

        # Calculează poziția pentru a centra imaginea pe pagină
        x = (self.width() - self.watermark.width()) // 2
        y = (self.height() - self.watermark.height()) // 2
        painter.drawPixmap(x, y, self.watermark)
        painter.end()
