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
        my_label.setFont(qtg.QFont('Harry P',35))
        self.layout().addWidget(my_label)
        my_label.setAlignment(QtCore.Qt.AlignCenter)

       #create a entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        #Create a button 
        my_button = qtw.QPushButton("You're a Wizzard !",clicked = lambda:press_it())
        self.layout().addWidget(my_button)

        self.show()

        #Show the app
        self.show()
        
        def press_it():
            #Add student name to label
            my_label.setText(f'Hello {my_entry.text()} !')
            #Clear the entry box 
            my_entry.setText("")
        
            


app = qtw.QApplication([])
mw = hogwartsExpress()

app.exec_()


