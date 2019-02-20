# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'part0.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(477, 400))
        MainWindow.setMaximumSize(QtCore.QSize(477, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 75 italic 25pt \"Noto Sans\" ;\n"
"color: rgb(0, 0, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setObjectName("btnNext")
        self.gridLayout.addWidget(self.btnNext, 7, 1, 1, 1)
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 75 italic 14pt \"Noto Sans\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 75 italic 14pt \"Noto Sans\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: 75 italic 14pt \"Noto Sans\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 italic 14pt \"Noto Sans\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.userName = QtWidgets.QLineEdit(self.centralwidget)
        self.userName.setObjectName("userName")
        self.gridLayout.addWidget(self.userName, 5, 0, 1, 2)
        self.userSem = QtWidgets.QLineEdit(self.centralwidget)
        self.userSem.setObjectName("userSem")
        self.gridLayout.addWidget(self.userSem, 6, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Helpdesk Scheduler v1.0"))
        self.label.setText(_translate("MainWindow", "MET IT Helpdesk Scheduler v1.0"))
        self.btnNext.setText(_translate("MainWindow", "Next"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "Part 1 will allow you to choose the available shifts"))
        self.label_4.setText(_translate("MainWindow", "Part 2 will allow you to pick up to 5 prefered shifts. \n"
"These shifts will then be prioritize for you when\n"
" the schedule is generated"))
        self.label_5.setText(_translate("MainWindow", "Please enter your name and semester below:"))
        self.label_2.setText(_translate("MainWindow", "Please complete both parts of this program"))
        self.userName.setPlaceholderText(_translate("MainWindow", "Name (e.g. John Doe)"))
        self.userSem.setPlaceholderText(_translate("MainWindow", "Semester (e.g. Spring 2019)"))

