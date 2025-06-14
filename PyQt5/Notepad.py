# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:34:02 2025

@author: Dixit
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QTextEdit,QMessageBox,QFileDialog

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setGeometry(100,100,300,400)
        self.setWindowTitle('4.1-NotepadGUI')
        self.notepadWidgets()
        self.show()
    def notepadWidgets(self):
        new_button=QPushButton("New",self)
        new_button.move(10,20)
        new_button.clicked.connect(self.clearText)
        
        save_button=QPushButton("save",self)
        save_button.move(80,20)
        save_button.clicked.connect(self.saveText)
        
        self.text_field=QTextEdit(self)
        self.text_field.resize(280,330)
        self.text_field.move(10,60)
    def clearText(self):
        answer=QMessageBox().question(self,"Clear Text","Do you want to clear the text ?",QMessageBox.No|QMessageBox.Yes,QMessageBox.Yes)
        if answer == QMessageBox.Yes :
            self.text_field.clear()
        else:
            pass
    def saveText(self):
        options = QFileDialog.Options()
        notepad_text=self.text_field.toPlainText()
        
        file_name,_=QFileDialog.getSaveFileName(self,'Save File',"","All Files(*);;Text Files(*.txt)",options=options)
        if file_name :
            with open(file_name,'w') as f :
                f.write(notepad_text)

if __name__=="__main__":
  app=QApplication(sys.argv)
  window=Notepad()
  sys.exit(app.exec_())
                
        

