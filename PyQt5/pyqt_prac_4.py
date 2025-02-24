# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:07:06 2025

@author: Dixit
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QCheckBox,QLabel
from PyQt5.QtCore import Qt

class CheckBoxWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializedUI()
    def initializedUI(self):
            self.setGeometry(100,100,250,250)
            self.setWindowTitle("Qcheckbox Widget")
            self.displayCheckBoxes()
            self.show()
    def displayCheckBoxes(self):
        header_label =QLabel(self)
        header_label.setText("Which shifts can you work ?")
        header_label.setWordWrap(True)
        header_label.move(10,10)
        header_label.resize(230,60)
        
        morning_cb=QCheckBox("Morning [8 AM -2 PM]",self)
        morning_cb.move(20,80)
        
        morning_cb.stateChanged.connect(self.printToterminal)
        after_cb =QCheckBox("Afternoon [1 PM -8 PM")
        after_cb.move(20,100)
        after_cb.stateChanged.connect(self.printToterminal)
        night_cb=QCheckBox("Night [7 PM - 3 AM]",self)
        night_cb.move(20,120)
        night_cb.stateChanged.connect(self.printToterminal)
    def printToterminal(self,state):
        sender = self.sender()
        if state == Qt.Checked :
            print(f"{sender.text} selected")
        else :
            print(f"{sender.text} Deselected")

if __name__=="__main__" :
   app=QApplication(sys.argv)
   window =CheckBoxWindow()
   sys.exit(app.exec_())
            
          