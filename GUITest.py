# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import codecs
from output import execution
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 554)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 470, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 470, 99, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 281, 441))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 470, 99, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 161, 17))
        self.label.setObjectName("label")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(300, 20, 281, 441))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(300, 0, 161, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 470, 99, 27))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 595, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(self.plainTextEdit.clear)
        self.pushButton_2.clicked.connect(self.plainTextEdit.copy)
        self.pushButton_4.clicked.connect(self.plainTextEdit_2.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.button_click)
        self.pushButton.clicked.connect(sys.exit)
        self.pushButton_3.clicked.connect(self.run)

    def error_return(self):
        with open("errors.txt") as openfile:
            for line in openfile:
                for part in line.split():
                    if "pyparsing.ParseException" in part:
                        self.plainTextEdit_2.setPlainText("चुकीची मांडणी")
                    elif "IndexError" in part:
                        self.plainTextEdit_2.setPlainText("अनपेक्षित चूक")

    def run(self):
        with open("errors.txt", "w+") as error:
            subprocess.call(["python", "./tokenize.py"], stderr=error)
        num_lines = sum(1 for line in open('errors.txt'))
        if (num_lines > 0):
            self.error_return()
        else:
            self.plainTextEdit_2.setPlainText("")
            a = execution()
            a.star()
            subprocess.call(["python", "./testCode.py"])

            opk = open("input2.txt", "w+")
            with open("input1.txt", "r") as f:
                for line in f:
                    cleanedLine = line.strip()
                    if cleanedLine:  # is not empty
                        print >> opk, cleanedLine
            opk.close()
            o = open('input2.txt', 'r+')
            num_lines = sum(1 for line in open('input2.txt'))
            for i in range(0, num_lines):
                string = o.readline()
                self.plainTextEdit_2.appendPlainText(string)

    def button_click(self):
        f = open("input.txt", mode='w')
        str = self.plainTextEdit.toPlainText().encode('utf-8')
        print >> f, str

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "दीप - आता प्रोग्रामिंग करा मराठीत !"))
        self.pushButton_2.setText(_translate("MainWindow", "निश्चित करा"))
        self.pushButton_3.setText(_translate("MainWindow", "कार्यान्वित"))
        self.pushButton_4.setText(_translate("MainWindow", "खोडा"))
        self.label.setText(_translate("MainWindow", "आपला कोड येथे लिहा :"))
        self.label_2.setText(_translate("MainWindow", "आपल्या कोडचे उत्तर :"))
        self.pushButton.setText(_translate("MainWindow", "बाहेर पडा"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    sys.exit(app.exec_())




