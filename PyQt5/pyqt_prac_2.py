# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:32:05 2025

@author: Dixit
"""
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton
import sys
class ButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializedUI()
    def initializedUI (self):
        self.setGeometry(100,100,200,150)
        self.setWindowTitle("QPushButton Widget")
        self.displayButton()
        self.show()
    def displayButton(self):
        name_label=QLabel(self)
        name_label.setText("Don't push the button")
        name_label.move(60,30)
        button=QPushButton('Push Me',self)
        button.clicked.connect(self.buttonClicked)
        button.move(80,70)
    def buttonClicked(self):
        print("The window has been closed")
        self.close()

if __name__=='__main__' :
  app=QApplication(sys.argv)
  window=ButtonWindow()
  sys.exit(app.exec_())        
