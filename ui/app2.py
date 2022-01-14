from PyQt5 import QtWidgets, uic
import sys


class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__() # informs the QMainWindow about MyApp info
        uic.loadUi('ui/app2.ui',self)
        # interaction
        self.btn1.clicked.connect(self.update_ui)
        self.btn2.clicked.connect(self.update_ui_2)

    def update_ui(self):
        self.output.setText('RED')
    
    def update_ui_2(self):
        self.output.setText('GREEN')

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
app.exec_()