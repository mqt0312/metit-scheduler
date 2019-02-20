# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'success.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(515, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.navToFolderLabel = QtWidgets.QLabel(Dialog)
        self.navToFolderLabel.setStyleSheet("font: 75 italic 14pt \"Noto Sans\";\n"
"")
        self.navToFolderLabel.setObjectName("navToFolderLabel")
        self.verticalLayout.addWidget(self.navToFolderLabel)
        self.fileName = QtWidgets.QLabel(Dialog)
        self.fileName.setStyleSheet("font: 75 italic 14pt \"Noto Sans\";\n"
"")
        self.fileName.setText("")
        self.fileName.setObjectName("fileName")
        self.verticalLayout.addWidget(self.fileName)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("font: 75 italic 14pt \"Noto Sans\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Helpdesk Scheduler v1.0"))
        self.navToFolderLabel.setText(_translate("Dialog", "Thank you, your schedule preference has been recorded.\n"
" Please navigate to the folder where this program is stored.\n"
" You should be able to find a file named"))
        self.label_4.setText(_translate("Dialog", "Please send this file to your supervisor via email. \n"
"The supervisor will generate the helpdesk\'s schedule. \n"
" You should receive your actual schedule shortly. \n"
"Thank you."))

