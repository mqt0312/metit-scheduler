# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'part2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.TitlePart2 = QtWidgets.QLabel(self.centralwidget)
        self.TitlePart2.setStyleSheet("font: 16pt \"Sans Serif\";\n"
"")
        self.TitlePart2.setObjectName("TitlePart2")
        self.gridLayout.addWidget(self.TitlePart2, 0, 0, 1, 2)
        self.listShift = QtWidgets.QListWidget(self.centralwidget)
        self.listShift.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listShift.setObjectName("listShift")
        self.gridLayout.addWidget(self.listShift, 1, 0, 1, 2)
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setObjectName("btnBack")
        self.gridLayout.addWidget(self.btnBack, 2, 0, 1, 1)
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setObjectName("btnNext")
        self.gridLayout.addWidget(self.btnNext, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Helpdesk Scheduler v1.0"))
        self.TitlePart2.setText(_translate("MainWindow", "Part 2: Select up to 5 shifts that you want the most"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnNext.setText(_translate("MainWindow", "Next"))

