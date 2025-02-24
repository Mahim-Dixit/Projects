import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer,Qt
from datetime import datetime

class Analog_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Analog Clock")
        
        # Set up a timer to update the clock every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)  # Call self.update() every second
        self.timer.start(1000)  # Timer interval: 1000 ms = 1 second
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smoother graphics

        # Draw the background
        painter.setBrush(QColor("Yellow"))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

        # Translate to the center of the widget
        center = self.rect().center()
        painter.translate(center.x(), center.y())

        # Draw the clock face
        self.tic(painter)

        # Get the current time
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second

        # Draw the clock hands
        self.draw_hand(painter, hour * 30 + minute * 0.5, 50, 8, QColor("#13293D"))  # Hour hand
        self.draw_hand(painter, minute * 6, 80, 6, QColor("#16324F"))  # Minute hand
        self.draw_hand(painter, second * 6, 90, 4, QColor("#3e92cc"))  # Second hand

    def tic(self, painter):
        painter.setPen(QColor("#29528f"))
        for i in range(60):
            if i % 5 == 0:  # Draw longer tics for hours
                painter.drawLine(0, -90, 0, -110)
            else:  # Draw shorter tics for minutes
                painter.drawLine(0, -95, 0, -100)
            painter.rotate(6)

    def draw_hand(self, painter, angle, length, width, color):
        painter.setPen(color)
        painter.setBrush(color)
        painter.save()  # Save the current state of the painter
        painter.rotate(angle)  # Rotate to the correct angle
        painter.drawRect(-width // 2, -length, width, length)  # Draw the hand
        painter.restore()  # Restore the painter's state

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Analog_clock()
    sys.exit(app.exec_())
         

