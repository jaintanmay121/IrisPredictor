from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from Iris_Pred import irp

qtCreatorFile = "iris_gui.ui" # Enter file here.

Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
#mainWindow, , QMainWindow,
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.EntButton.clicked.connect(self.Calculate)
    
    def Calculate(self):
        a = float(self.sl.toPlainText())
        b = float(self.sw.toPlainText())
        c = float(self.pl.toPlainText())
        d = float(self.pw.toPlainText())   
        res="Iris species is: "+ str(irp(a,b,c,d))
        self.out.setText(res)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())