# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:08:36 2025

@author: Dixit
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,QLabel,QPushButton,QCheckBox
,QCheckBox,QButtonGroup,QHBoxLayout,QVBoxLayout)
from PyQt5.QtGui import QFont

class DisplaySurvey(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
    def InitializeUI(self):
        self.setGeometry(100,100,400,230)
        self.setWindowTitle('4.2 - Survey GUI')
        self.displayWidgets()
        self.show()
    def displayWidgets(self):
        title=QLabel("Restaurant Name")
        title.setFont(QFont('Arial',17))
        question=QLabel("How would you rate your service today ?")
        
        title_h_box=QHBoxLayout()
        title_h_box.addStretch()
        title_h_box.addWidget(title)
        title_h_box.addStretch()
        rating=["Not Satisfied","Average","Satisfied"]
        
        ratings_h_box=QHBoxLayout()
        ratings_h_box.setSpacing(60)
        
        ratings_h_box.addStretch()
        cb_h_box=QHBoxLayout()
        cb_h_box.setSpacing(100)
        scale_bg=QButtonGroup(self)
        for cb in range(len(rating)):
            scale_cb=QCheckBox(str(cb),self)
            cb_h_box.addWidget(scale_cb)
            scale_bg.addButton(scale_cb)
        cb_h_box.addStretch()
        
        scale_bg.buttonClicked.connect(self.checkboxClicked)
        
        close_button=QPushButton("Close",self)
        close_button.clicked.connect(self.close)
        
        
        v_box=QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(ratings_h_box)
        v_box.addStretch(2)
        v_box.addWidget(close_button)
        self.setLayout(v_box)
    def checkboxClicked(self,cb):
        print(f"{cb.text()} Selected")
if __name__=="__main__":
    
 app=QApplication(sys.argv)
 window=DisplaySurvey()
 sys.exit(app.exec_())
        
        