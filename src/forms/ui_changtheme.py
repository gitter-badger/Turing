# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_changtheme.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangeThemeWindow(object):
    def setupUi(self, ChangeThemeWindow):
        ChangeThemeWindow.setObjectName("ChangeThemeWindow")
        ChangeThemeWindow.setWindowModality(QtCore.Qt.WindowModal)
        ChangeThemeWindow.resize(503, 353)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/action/media/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChangeThemeWindow.setWindowIcon(icon)
        ChangeThemeWindow.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChangeThemeWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_01 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_01.setObjectName("label_01")
        self.gridLayout.addWidget(self.label_01, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.btnCodeColor_01 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_01.setEnabled(True)
        self.btnCodeColor_01.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/action/media/color_wheel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCodeColor_01.setIcon(icon1)
        self.btnCodeColor_01.setObjectName("btnCodeColor_01")
        self.gridLayout.addWidget(self.btnCodeColor_01, 0, 2, 1, 1)
        self.txtColor_01 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_01.setObjectName("txtColor_01")
        self.gridLayout.addWidget(self.txtColor_01, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 4, 1, 1)
        self.txtColor_11 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_11.setObjectName("txtColor_11")
        self.gridLayout.addWidget(self.txtColor_11, 0, 5, 1, 1)
        self.txtColor_02 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_02.setObjectName("txtColor_02")
        self.gridLayout.addWidget(self.txtColor_02, 1, 1, 1, 1)
        self.txtColor_03 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_03.setObjectName("txtColor_03")
        self.gridLayout.addWidget(self.txtColor_03, 2, 1, 1, 1)
        self.txtColor_04 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_04.setObjectName("txtColor_04")
        self.gridLayout.addWidget(self.txtColor_04, 3, 1, 1, 1)
        self.txtColor_05 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_05.setObjectName("txtColor_05")
        self.gridLayout.addWidget(self.txtColor_05, 4, 1, 1, 1)
        self.txtColor_06 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_06.setObjectName("txtColor_06")
        self.gridLayout.addWidget(self.txtColor_06, 5, 1, 1, 1)
        self.txtColor_07 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_07.setObjectName("txtColor_07")
        self.gridLayout.addWidget(self.txtColor_07, 6, 1, 1, 1)
        self.txtColor_08 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_08.setObjectName("txtColor_08")
        self.gridLayout.addWidget(self.txtColor_08, 7, 1, 1, 1)
        self.txtColor_09 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_09.setObjectName("txtColor_09")
        self.gridLayout.addWidget(self.txtColor_09, 8, 1, 1, 1)
        self.txtColor_10 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_10.setObjectName("txtColor_10")
        self.gridLayout.addWidget(self.txtColor_10, 9, 1, 1, 1)
        self.btnCodeColor_02 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_02.setEnabled(True)
        self.btnCodeColor_02.setText("")
        self.btnCodeColor_02.setIcon(icon1)
        self.btnCodeColor_02.setObjectName("btnCodeColor_02")
        self.gridLayout.addWidget(self.btnCodeColor_02, 1, 2, 1, 1)
        self.btnCodeColor_03 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_03.setEnabled(True)
        self.btnCodeColor_03.setText("")
        self.btnCodeColor_03.setIcon(icon1)
        self.btnCodeColor_03.setObjectName("btnCodeColor_03")
        self.gridLayout.addWidget(self.btnCodeColor_03, 2, 2, 1, 1)
        self.btnCodeColor_04 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_04.setEnabled(True)
        self.btnCodeColor_04.setText("")
        self.btnCodeColor_04.setIcon(icon1)
        self.btnCodeColor_04.setObjectName("btnCodeColor_04")
        self.gridLayout.addWidget(self.btnCodeColor_04, 3, 2, 1, 1)
        self.btnCodeColor_05 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_05.setEnabled(True)
        self.btnCodeColor_05.setText("")
        self.btnCodeColor_05.setIcon(icon1)
        self.btnCodeColor_05.setObjectName("btnCodeColor_05")
        self.gridLayout.addWidget(self.btnCodeColor_05, 4, 2, 1, 1)
        self.btnCodeColor_06 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_06.setEnabled(True)
        self.btnCodeColor_06.setText("")
        self.btnCodeColor_06.setIcon(icon1)
        self.btnCodeColor_06.setObjectName("btnCodeColor_06")
        self.gridLayout.addWidget(self.btnCodeColor_06, 5, 2, 1, 1)
        self.btnCodeColor_07 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_07.setEnabled(True)
        self.btnCodeColor_07.setText("")
        self.btnCodeColor_07.setIcon(icon1)
        self.btnCodeColor_07.setObjectName("btnCodeColor_07")
        self.gridLayout.addWidget(self.btnCodeColor_07, 6, 2, 1, 1)
        self.btnCodeColor_08 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_08.setEnabled(True)
        self.btnCodeColor_08.setText("")
        self.btnCodeColor_08.setIcon(icon1)
        self.btnCodeColor_08.setObjectName("btnCodeColor_08")
        self.gridLayout.addWidget(self.btnCodeColor_08, 7, 2, 1, 1)
        self.btnCodeColor_09 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_09.setEnabled(True)
        self.btnCodeColor_09.setText("")
        self.btnCodeColor_09.setIcon(icon1)
        self.btnCodeColor_09.setObjectName("btnCodeColor_09")
        self.gridLayout.addWidget(self.btnCodeColor_09, 8, 2, 1, 1)
        self.btnCodeColor_10 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_10.setEnabled(True)
        self.btnCodeColor_10.setText("")
        self.btnCodeColor_10.setIcon(icon1)
        self.btnCodeColor_10.setObjectName("btnCodeColor_10")
        self.gridLayout.addWidget(self.btnCodeColor_10, 9, 2, 1, 1)
        self.btnCodeColor_11 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_11.setEnabled(True)
        self.btnCodeColor_11.setText("")
        self.btnCodeColor_11.setIcon(icon1)
        self.btnCodeColor_11.setObjectName("btnCodeColor_11")
        self.gridLayout.addWidget(self.btnCodeColor_11, 0, 6, 1, 1)
        self.label_17 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 4, 1, 1)
        self.label_20 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 4, 4, 1, 1)
        self.txtColor_12 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_12.setObjectName("txtColor_12")
        self.gridLayout.addWidget(self.txtColor_12, 1, 5, 1, 1)
        self.txtColor_13 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_13.setObjectName("txtColor_13")
        self.gridLayout.addWidget(self.txtColor_13, 2, 5, 1, 1)
        self.txtColor_14 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_14.setObjectName("txtColor_14")
        self.gridLayout.addWidget(self.txtColor_14, 3, 5, 1, 1)
        self.txtColor_15 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_15.setObjectName("txtColor_15")
        self.gridLayout.addWidget(self.txtColor_15, 4, 5, 1, 1)
        self.txtColor_16 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_16.setObjectName("txtColor_16")
        self.gridLayout.addWidget(self.txtColor_16, 5, 5, 1, 1)
        self.txtColor_17 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_17.setObjectName("txtColor_17")
        self.gridLayout.addWidget(self.txtColor_17, 6, 5, 1, 1)
        self.txtColor_18 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_18.setObjectName("txtColor_18")
        self.gridLayout.addWidget(self.txtColor_18, 7, 5, 1, 1)
        self.txtColor_19 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_19.setObjectName("txtColor_19")
        self.gridLayout.addWidget(self.txtColor_19, 8, 5, 1, 1)
        self.txtColor_20 = QtWidgets.QLineEdit(ChangeThemeWindow)
        self.txtColor_20.setObjectName("txtColor_20")
        self.gridLayout.addWidget(self.txtColor_20, 9, 5, 1, 1)
        self.btnCodeColor_12 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_12.setEnabled(True)
        self.btnCodeColor_12.setText("")
        self.btnCodeColor_12.setIcon(icon1)
        self.btnCodeColor_12.setObjectName("btnCodeColor_12")
        self.gridLayout.addWidget(self.btnCodeColor_12, 1, 6, 1, 1)
        self.btnCodeColor_13 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_13.setEnabled(True)
        self.btnCodeColor_13.setText("")
        self.btnCodeColor_13.setIcon(icon1)
        self.btnCodeColor_13.setObjectName("btnCodeColor_13")
        self.gridLayout.addWidget(self.btnCodeColor_13, 2, 6, 1, 1)
        self.btnCodeColor_14 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_14.setEnabled(True)
        self.btnCodeColor_14.setText("")
        self.btnCodeColor_14.setIcon(icon1)
        self.btnCodeColor_14.setObjectName("btnCodeColor_14")
        self.gridLayout.addWidget(self.btnCodeColor_14, 3, 6, 1, 1)
        self.btnCodeColor_15 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_15.setEnabled(True)
        self.btnCodeColor_15.setText("")
        self.btnCodeColor_15.setIcon(icon1)
        self.btnCodeColor_15.setObjectName("btnCodeColor_15")
        self.gridLayout.addWidget(self.btnCodeColor_15, 4, 6, 1, 1)
        self.btnCodeColor_16 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_16.setEnabled(True)
        self.btnCodeColor_16.setText("")
        self.btnCodeColor_16.setIcon(icon1)
        self.btnCodeColor_16.setObjectName("btnCodeColor_16")
        self.gridLayout.addWidget(self.btnCodeColor_16, 5, 6, 1, 1)
        self.btnCodeColor_17 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_17.setEnabled(True)
        self.btnCodeColor_17.setText("")
        self.btnCodeColor_17.setIcon(icon1)
        self.btnCodeColor_17.setObjectName("btnCodeColor_17")
        self.gridLayout.addWidget(self.btnCodeColor_17, 6, 6, 1, 1)
        self.btnCodeColor_18 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_18.setEnabled(True)
        self.btnCodeColor_18.setText("")
        self.btnCodeColor_18.setIcon(icon1)
        self.btnCodeColor_18.setObjectName("btnCodeColor_18")
        self.gridLayout.addWidget(self.btnCodeColor_18, 7, 6, 1, 1)
        self.btnCodeColor_19 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_19.setEnabled(True)
        self.btnCodeColor_19.setText("")
        self.btnCodeColor_19.setIcon(icon1)
        self.btnCodeColor_19.setObjectName("btnCodeColor_19")
        self.gridLayout.addWidget(self.btnCodeColor_19, 8, 6, 1, 1)
        self.btnCodeColor_20 = QtWidgets.QPushButton(ChangeThemeWindow)
        self.btnCodeColor_20.setEnabled(True)
        self.btnCodeColor_20.setText("")
        self.btnCodeColor_20.setIcon(icon1)
        self.btnCodeColor_20.setObjectName("btnCodeColor_20")
        self.gridLayout.addWidget(self.btnCodeColor_20, 9, 6, 1, 1)
        self.label_21 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 5, 4, 1, 1)
        self.label_22 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 6, 4, 1, 1)
        self.label_23 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 7, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 8, 4, 1, 1)
        self.label_25 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 9, 4, 1, 1)
        self.label_02 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_02.setObjectName("label_02")
        self.gridLayout.addWidget(self.label_02, 1, 0, 1, 1)
        self.label_03 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_03.setObjectName("label_03")
        self.gridLayout.addWidget(self.label_03, 2, 0, 1, 1)
        self.label_04 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_04.setObjectName("label_04")
        self.gridLayout.addWidget(self.label_04, 3, 0, 1, 1)
        self.label_05 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_05.setObjectName("label_05")
        self.gridLayout.addWidget(self.label_05, 4, 0, 1, 1)
        self.label_06 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_06.setObjectName("label_06")
        self.gridLayout.addWidget(self.label_06, 5, 0, 1, 1)
        self.label_07 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_07.setObjectName("label_07")
        self.gridLayout.addWidget(self.label_07, 6, 0, 1, 1)
        self.label_08 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_08.setObjectName("label_08")
        self.gridLayout.addWidget(self.label_08, 7, 0, 1, 1)
        self.label_09 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_09.setObjectName("label_09")
        self.gridLayout.addWidget(self.label_09, 8, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(ChangeThemeWindow)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ChangeThemeWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_01.setBuddy(self.txtColor_11)
        self.label_16.setBuddy(self.txtColor_11)
        self.label_17.setBuddy(self.txtColor_12)
        self.label_18.setBuddy(self.txtColor_12)
        self.label_19.setBuddy(self.txtColor_14)
        self.label_20.setBuddy(self.txtColor_15)
        self.label_21.setBuddy(self.txtColor_15)
        self.label_22.setBuddy(self.txtColor_15)
        self.label_23.setBuddy(self.txtColor_15)
        self.label_24.setBuddy(self.txtColor_15)
        self.label_25.setBuddy(self.txtColor_15)
        self.label_02.setBuddy(self.txtColor_11)
        self.label_03.setBuddy(self.txtColor_11)
        self.label_04.setBuddy(self.txtColor_11)
        self.label_05.setBuddy(self.txtColor_11)
        self.label_06.setBuddy(self.txtColor_11)
        self.label_07.setBuddy(self.txtColor_11)
        self.label_08.setBuddy(self.txtColor_11)
        self.label_09.setBuddy(self.txtColor_11)
        self.label_10.setBuddy(self.txtColor_11)

        self.retranslateUi(ChangeThemeWindow)
        self.buttonBox.accepted.connect(ChangeThemeWindow.accept)
        self.buttonBox.rejected.connect(ChangeThemeWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangeThemeWindow)

    def retranslateUi(self, ChangeThemeWindow):
        _translate = QtCore.QCoreApplication.translate
        ChangeThemeWindow.setWindowTitle(_translate("ChangeThemeWindow", "Edit theme"))
        self.label_01.setText(_translate("ChangeThemeWindow", "Window :"))
        self.label_16.setText(_translate("ChangeThemeWindow", "Shadow :"))
        self.label_17.setText(_translate("ChangeThemeWindow", "Button :"))
        self.label_18.setText(_translate("ChangeThemeWindow", "Button Text :"))
        self.label_19.setText(_translate("ChangeThemeWindow", "Disabled\n"
"Button Text :"))
        self.label_20.setText(_translate("ChangeThemeWindow", "Bright Text :"))
        self.label_21.setText(_translate("ChangeThemeWindow", "Link :"))
        self.label_22.setText(_translate("ChangeThemeWindow", "Highlight :"))
        self.label_23.setText(_translate("ChangeThemeWindow", "Disabled\n"
"Highlight :"))
        self.label_24.setText(_translate("ChangeThemeWindow", "Highlighted Text :"))
        self.label_25.setText(_translate("ChangeThemeWindow", "Disabled\n"
"Highlighted Text :"))
        self.label_02.setText(_translate("ChangeThemeWindow", "Window Text :"))
        self.label_03.setText(_translate("ChangeThemeWindow", "Disabled\n"
"window Text : "))
        self.label_04.setText(_translate("ChangeThemeWindow", "Base :"))
        self.label_05.setText(_translate("ChangeThemeWindow", "Alternate Base :"))
        self.label_06.setText(_translate("ChangeThemeWindow", "Tool Tip Base :"))
        self.label_07.setText(_translate("ChangeThemeWindow", "Tool Tip Text :"))
        self.label_08.setText(_translate("ChangeThemeWindow", "Text :"))
        self.label_09.setText(_translate("ChangeThemeWindow", "Disabled\n"
"Text :"))
        self.label_10.setText(_translate("ChangeThemeWindow", "Dark :"))

import turing_rc
