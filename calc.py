# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.output = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.output.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.output.setFont(font)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)
        self.buffer = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.buffer.setObjectName("buffer")
        self.verticalLayout.addWidget(self.buffer)
        self.buttonEquals = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonEquals.setObjectName("buttonEquals")
        self.verticalLayout.addWidget(self.buttonEquals)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button7.setObjectName("button7")
        self.gridLayout.addWidget(self.button7, 0, 1, 1, 1)
        self.button0 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button0.setObjectName("button0")
        self.gridLayout.addWidget(self.button0, 3, 2, 1, 1)
        self.buttonDiv = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonDiv.setObjectName("buttonDiv")
        self.gridLayout.addWidget(self.buttonDiv, 3, 4, 1, 1)
        self.buttonSub = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonSub.setObjectName("buttonSub")
        self.gridLayout.addWidget(self.buttonSub, 1, 4, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 2, 2, 1, 1)
        self.button3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 2, 1, 1, 1)
        self.button6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button6.setObjectName("button6")
        self.gridLayout.addWidget(self.button6, 1, 1, 1, 1)
        self.button5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button5.setObjectName("button5")
        self.gridLayout.addWidget(self.button5, 1, 2, 1, 1)
        self.button4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button4.setObjectName("button4")
        self.gridLayout.addWidget(self.button4, 1, 3, 1, 1)
        self.buttonAdd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonAdd.setObjectName("buttonAdd")
        self.gridLayout.addWidget(self.buttonAdd, 0, 4, 1, 1)
        self.button8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button8.setObjectName("button8")
        self.gridLayout.addWidget(self.button8, 0, 2, 1, 1)
        self.button1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 2, 3, 1, 1)
        self.button9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button9.setAutoRepeatDelay(300)
        self.button9.setObjectName("button9")
        self.gridLayout.addWidget(self.button9, 0, 3, 1, 1)
        self.buttonMult = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonMult.setObjectName("buttonMult")
        self.gridLayout.addWidget(self.buttonMult, 2, 4, 1, 1)
        self.buttonMod = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonMod.setObjectName("buttonMod")
        self.gridLayout.addWidget(self.buttonMod, 3, 1, 1, 1)
        self.buttonDec = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonDec.setObjectName("buttonDec")
        self.gridLayout.addWidget(self.buttonDec, 3, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scientific Calculator"))
        self.output.setPlaceholderText(_translate("MainWindow", "0"))
        self.buttonEquals.setText(_translate("MainWindow", "="))
        self.button7.setText(_translate("MainWindow", "7"))
        self.button0.setText(_translate("MainWindow", "0"))
        self.buttonDiv.setText(_translate("MainWindow", "/"))
        self.buttonSub.setText(_translate("MainWindow", "-"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.buttonAdd.setText(_translate("MainWindow", "+"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.button1.setText(_translate("MainWindow", "1"))
        self.button9.setText(_translate("MainWindow", "9"))
        self.buttonMult.setText(_translate("MainWindow", "*"))
        self.buttonMod.setText(_translate("MainWindow", "%"))
        self.buttonDec.setText(_translate("MainWindow", "."))
    
    
    def __init__(self):
        self.bufferTxt=""
        self.a=0.0
        self.b=0.0
        self.currentOperator=-1
        self.doneCalc=False
        self.decimalCount=0

    def Clicked(self,x):
        if(self.doneCalc):
            if(x>=0):
                self.a=x
            else:
                self.decimalCount=0
                self.a=0.0
            self.b=0.0
            self.decimalCount=0
            self.output.setText(str(self.a))
            self.bufferTxt=str(int(self.a))
            self.buffer.setText(self.bufferTxt)

            self.doneCalc=False
        
        else:
            if(x>=0):
                if(self.currentOperator==-1):
                    if(self.decimalCount==0):
                        self.a=self.a*10+x
                    else:
                        self.a=self.a+x*(10**-self.decimalCount)
                        self.decimalCount=self.decimalCount+1
                    self.output.setText(str(self.a))
                else:
                    if(self.decimalCount==0):
                        self.b=self.b*10+x
                    else:
                        self.b=self.b+x*(10**-self.decimalCount)
                    self.output.setText(str(self.b))
            elif(x==-1):
                if(self.currentOperator==-2):
                    self.a=self.a+self.b
                if(self.currentOperator==-3):
                    self.a=self.a-self.b
                if(self.currentOperator==-4):
                    self.a=self.a*self.b
                if(self.currentOperator==-5):
                    self.a=self.a/self.b
                if(self.currentOperator==-6):
                    self.a=self.a%self.b
                self.b=0.0
                self.currentOperator=-1
                self.decimalCount=0
                self.doneCalc=True
                self.output.setText(str(self.a))
            else:
                if(self.currentOperator==-2):
                    self.a=self.a+self.b
                if(self.currentOperator==-3):
                    self.a=self.a-self.b
                if(self.currentOperator==-4):
                    self.a=self.a*self.b
                if(self.currentOperator==-5):
                    self.a=self.a/self.b
                if(self.currentOperator==-6):
                    self.a=self.a%self.b
                self.b=0.0
                self.decimalCount=0
                self.currentOperator=x
                self.output.setText(str(self.a))

    
    def Clicked0(self):
        self.bufferTxt=self.bufferTxt+"0"
        self.buffer.setText(self.bufferTxt)
        self.Clicked(0)
    def Clicked1(self):
        self.bufferTxt=self.bufferTxt+"1"
        self.buffer.setText(self.bufferTxt)
        self.Clicked(1)
    def Clicked2(self):
        self.bufferTxt=self.bufferTxt+"2"
        self.buffer.setText(self.bufferTxt)
        self.Clicked(2)
    def Clicked3(self):
        self.bufferTxt=self.bufferTxt+"3"
        self.buffer.setText(self.bufferTxt)
        self.Clicked(3)
    def Clicked4(self):
        self.bufferTxt=self.bufferTxt+"4"
        self.buffer.setText(self.bufferTxt)
        self.Clicked(4)
    def Clicked5(self):
        self.bufferTxt=self.bufferTxt+"5"
        self.buffer.setText(self.bufferTxt)
        self.Clicked(5)
    def Clicked6(self):
        self.bufferTxt=self.bufferTxt+"6"
        self.buffer.setText(self.bufferTxt)
        self.Clicked(6)
    def Clicked7(self):
        self.bufferTxt=self.bufferTxt+"7"
        self.buffer.setText(self.bufferTxt)
        self.Clicked(7)
    def Clicked8(self):
        self.bufferTxt=self.bufferTxt+"8"
        self.buffer.setText(self.bufferTxt)
        self.Clicked(8)
    def Clicked9(self):
        self.bufferTxt=self.bufferTxt+"9"
        self.buffer.setText(self.bufferTxt)
        self.Clicked(9)
    def ClickedEQ(self):
        self.Clicked(-1)
    def ClickedPL(self):
        self.bufferTxt=self.bufferTxt+" + "
        self.buffer.setText(self.bufferTxt)
        self.Clicked(-2)
    def ClickedMI(self):
        self.bufferTxt=self.bufferTxt+" - "
        self.buffer.setText(self.bufferTxt)
        self.Clicked(-3)
    def ClickedMU(self):
        self.bufferTxt=self.bufferTxt+" X "
        self.buffer.setText(self.bufferTxt)
        self.Clicked(-4)
    def ClickedDI(self):
        self.bufferTxt=self.bufferTxt+" / "
        self.buffer.setText(self.bufferTxt)
        self.Clicked(-5)
    def ClickedMO(self):
        self.bufferTxt=self.bufferTxt+" % "
        self.buffer.setText(self.bufferTxt)
        self.Clicked(-6)
    def ClickedDE(self):
        if(self.decimalCount==0):
            self.decimalCount+=1
            self.bufferTxt=self.bufferTxt+"."
            self.buffer.setText(self.bufferTxt)
        
