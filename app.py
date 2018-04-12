from PyQt5 import QtCore, QtGui, QtWidgets
from calc import Ui_MainWindow



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    result=ui.output
    ui.button0.clicked.connect(ui.Clicked0)
    ui.button1.clicked.connect(ui.Clicked1)
    ui.button2.clicked.connect(ui.Clicked2)
    ui.button3.clicked.connect(ui.Clicked3)
    ui.button4.clicked.connect(ui.Clicked4)
    ui.button5.clicked.connect(ui.Clicked5)
    ui.button6.clicked.connect(ui.Clicked6)
    ui.button7.clicked.connect(ui.Clicked7)
    ui.button8.clicked.connect(ui.Clicked8)
    ui.button9.clicked.connect(ui.Clicked9)
    ui.buttonMult.clicked.connect(ui.ClickedMU)
    ui.buttonMod.clicked.connect(ui.ClickedMO)
    ui.buttonDiv.clicked.connect(ui.ClickedDI)
    ui.buttonSub.clicked.connect(ui.ClickedMI)
    ui.buttonAdd.clicked.connect(ui.ClickedPL)
    ui.buttonDec.clicked.connect(ui.ClickedDE)
    ui.buttonEquals.clicked.connect(ui.ClickedEQ)

    MainWindow.show()
    sys.exit(app.exec_())


    
