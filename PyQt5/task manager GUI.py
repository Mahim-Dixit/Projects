# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:05:14 2025

@author: Dixit
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
import clock

font_id=QFontDatabase.addApplicationFont("BlackOpsOne-Regular.ttf")
if font_id == -1:
    print("Failed to load font. Using fallback font.")
    font_family = "Arial"  # Fallback font
else:
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

class DisplayTask(QWidget):
    def __init__(self,task_string):
        super().__init__()
        
        self.initializeUI(task_string)
    def initializeUI(self,task_string):
        self.setGeometry(0,0,1000,50)
        self.form=QFormLayout(self)
        self.form.addRow(QCheckBox(f"{task_string}",self))
        self.show()

class CreateTask(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setGeometry(0,0,1000,50)
        self.form=QFormLayout(self)
        self.line=QLineEdit("Enter Task",self)
        self.form.addRow(self.line)
        self.show()

        
    
        


class DisplayerTask(QWidget):
   def __init__(self):
       super().__init__()
       
       self.initializeUI()
   def initializeUI(self):
       
       
       self.hbox=QHBoxLayout(self)
       self.calender=QCalendarWidget()
       
       self.calender.setFixedSize(300,300)
       self.hbox.setAlignment(Qt.AlignTop)
       
       self.hbox.addWidget(self.calender,alignment=Qt.AlignLeft)
       self.vbox=QVBoxLayout()
       self.vbox.setAlignment(Qt.AlignTop)
       self.hbox.addLayout(self.vbox)
       self.show()
       
   def showtask(self):
       self.vbox.addWidget(self.task)
   
       
       
       

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setGeometry(0,0,800,800)
        self.showMaximized()
        self.setWindowTitle("Task Manager GUI")
        self.setObjectName("MainScreen")
        widget=QWidget(self)
        vbox=QVBoxLayout(widget)
       
        self.displayer=DisplayerTask()
        self.clock=clock.Analog_clock()
        self.clock.setStyleSheet("background-color: yellow;")
        self.clock.setMinimumSize(300, 300)
        
        self.create=CreateTask()
        vbox.addWidget(self.displayer)
        vbox.addWidget(self.clock,alignment=Qt.AlignLeft)
        vbox.addWidget(self.create)
        self.setCentralWidget(widget)
        self.create.line.returnPressed.connect(self.create_task)
        self.show()
    def create_task(self):
        
        task=self.create.line.text()
        self.task=DisplayTask(task)
        self.displayer.vbox.addWidget(self.task)
        self.create.line.clear()
    
     




















if __name__=="__main__":
   app=QApplication([])
   app.setStyleSheet(f"""
                     MainScreen{{background-image: url('bgimage.png')}}
                     
                     QLineEdit , QCheckBox {{background-color:Yellow;
                               
                               font-family :"{font_family}";
                               font-size : 21px;}}
                     QCalendarWidget {{
                         background-color:"Yellow";
                         font-family : "{font_family} ";
                         font-size:21px;}}
                     QCalendarWidget QToolButton{{
                         background-color:"Yellow";
                         }}
                     QCheckBox::indicator {{ width : 50px;height :50px;
                                              border  : 2px solid Black ;
                                              border-radius : 25px ;}}
                     QCheckBox::indicator:checked {{ width : 50px;height :50px;
                                              border  : 2px solid Black ;
                                              border-radius : 25px ;}}
                     
                     QCheckBox::indicator:unchecked {{ width : 50px;height :50px;
                                              border  : 2px solid Black ;
                                              border-radius : 25px ;}}
                     QWidget#qt_calendar_navigationbar{{
                     background-color:"Yellow";
                     
                     
                     
                     }}
                    
                     
                     
                     
                     
                     """)
   w=MainScreen()
   sys.exit(app.exec_())
        













