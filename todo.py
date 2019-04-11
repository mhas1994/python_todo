import sys
from PyQt5.QtWidgets import *

from db import *

class ToDo(QWidget):
    
    def __init__(self):
        super().__init__()        
        self.initUI()

    def get_data(self):
        data = self.db.get_all().val()

        self.table.setColumnCount(2)
        self.table.setRowCount(len(data.keys()))
        self.table.resize(1000, 500)
        header = self.table.horizontalHeader()
        
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        self.table.setHorizontalHeaderLabels(["Task","Description"]) 

        i=0
        for d in data:
            j=0
            for k in data[d]:            
                self.table.setItem(i,j, QTableWidgetItem(data[d][k]))
                j=j+1
            i=i+1


        
    def initUI(self):
        
        self.db = DB()
        
        grid = QGridLayout()
        self.setLayout(grid)
                
        self.okButton = QPushButton("Add")
        self.cancelButton = QPushButton("Cancel")
        self.okButton.clicked.connect(self.addToDo)
        self.cancelButton.clicked.connect(self.exit_program)

        form = QFormLayout()
        
        self.task = QLineEdit()
        self.description = QLineEdit()
        form.addRow("Task: ",self.task)
        form.addRow("Description: ",self.description)
        
        grid.addLayout(form,1,1)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.okButton)
        hbox1.addWidget(self.cancelButton)
        grid.addLayout(hbox1,2,1)

        self.table = QTableWidget()
        grid.addWidget(self.table,3,1)
              
        self.setGeometry(100, 50, 1000, 700)
        self.setWindowTitle('A small ToDo Application')
        self.get_data()
        self.show()

    def addToDo(self):
        self.db.addToDo(self.task.text(),self.description.text())
        QMessageBox.information(self,'Task added','Task has been added successfully')
        self.task.setText('')
        self.description.setText('')
        self.get_data()

    def exit_program(self):
        app.quit()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ToDo()
    sys.exit(app.exec_())
