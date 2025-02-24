# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:49:13 2025

@author: Dixit
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton

from PyQt5.QtCore import Qt

class Entry(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,200)
        self.setWindowTitle('QLineEdit Widget')
        self.displayWidgets()
        self.show()
    def displayWidgets(self):
        QLabel("Please Enter your name below",self).move(100,10)
        name_label=QLabel("Name : ",self)
        name_label.move(70,50)
        self.name_entry=QLineEdit(self)
        self.name_entry.setAlignment(Qt.AlignLeft)
        self.name_entry.move(130,50)
        self.name_entry.resize(200,20)
        self.clear_button=QPushButton('Clear',self)
        self.clear_button.clicked.connect(self.clearEntries)
        
        self.clear_button.move(160,110)
    def clearEntries(self):
        sender=self.sender()
        if sender.text() == "Clear" :
            self.name_entry.clear()

if __name__=="__main__":
 app=QApplication(sys.argv)
 window=Entry()
 sys.exit(app.exec_())            
        