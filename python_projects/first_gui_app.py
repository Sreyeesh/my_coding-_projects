"""
Project: Welcome App

"""
import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore
import PyQt5.QtGui as qtg

class hogwartsExpress(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()


        #Add Title
        self.setWindowTitle("Hogwarts Students Registery")

        # Set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        # Create A Lable
        my_label = qtw.QLabel("Welcome to Hogwarts")
        self.layout().addWidget(my_label)

        #Change the font size of label
        my_label.setFont(qtg.QFont('Harry P',200))
        self.layout().addWidget(my_label)
        my_label.setAlignment(QtCore.Qt.AlignCenter)

        #background image 
        

        self.show()

app = qtw.QApplication([])
mw = hogwartsExpress()

app.exec_()


