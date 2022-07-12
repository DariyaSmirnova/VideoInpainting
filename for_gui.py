# Окно приложения
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Inpainting")
        self.setGeometry(500, 300, 500, 300)
        #self.textEdit = QTextEdit(self)
        #self.textEdit.toPlainText()

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('It is time to try E2FGVI!')
        self.main_text.move(20, 10)
        self.main_text.adjustSize()

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('Specify absolute paths to the following files.')
        self.main_text.move(20, 30)
        self.main_text.adjustSize()

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('INPUT FILE')
        self.main_text.move(330, 60)
        self.main_text.adjustSize()

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('INPUT MASK')
        self.main_text.move(330, 90)
        self.main_text.adjustSize()

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('OUTPUT FILE')
        self.main_text.move(330, 120)
        self.main_text.adjustSize()

        self.nameTextbox = QLineEdit(self)
        self.nameTextbox.move(20, 60)
        self.nameTextbox.setFixedWidth(300)

        self.nameTextbox = QLineEdit(self)
        self.nameTextbox.setFixedWidth(300)
        self.nameTextbox.move(20, 90)

        self.nameTextbox = QLineEdit(self)
        self.nameTextbox.move(20, 120)
        self.nameTextbox.setFixedWidth(300)

        self.button = QPushButton("Start", self)
        self.button.move(400, 250)
        self.button.clicked.connect(self.input_file)

        self.but = QPushButton("Info", self)
        self.but.move(20, 220)
        self.but.clicked.connect(self.inf)

        self.new_text = QtWidgets.QLabel(self)
        self.new_text1 = QtWidgets.QLabel(self)

        self.btn = QPushButton("Help", self)
        self.btn.move(20, 250)
        self.btn.clicked.connect(self.add_label)

    def input_file(self):
    #    text_input_file = self.textEdit.toPlainText()
    #    print(text_input_file)
        pass




    def add_label(self):
        self.new_text.setText('INPUT FILE - The video file from which the object will be deleted.\nINPUT MASK - The mask for deleting an object.'
                              '\nOUTPUT FILE - The video file with a deleted object.\nExample of an absolute path: C:\PycharmProjects\Project')
        self.new_text.move(20, 150)
        self.new_text.adjustSize()

    #def start(self):
    #    pass

    def inf(self):
        print('https://github.com/MCG-NKU/E2FGVI')
        self.new_text1.setText('Please, check the terminal.')
        self.new_text1.move(100, 225)
        self.new_text1.adjustSize()

def main():
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec_())
if __name__ == '__main__':
    main()