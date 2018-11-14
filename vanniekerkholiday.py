# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vanniekerkholiday.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1083, 899)
        self.vanNiekMool_gbox = QtGui.QGroupBox(Dialog)
        self.vanNiekMool_gbox.setGeometry(QtCore.QRect(50, 30, 981, 851))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.vanNiekMool_gbox.setFont(font)
        self.vanNiekMool_gbox.setObjectName(_fromUtf8("vanNiekMool_gbox"))
        self.FamNamSur_lbl = QtGui.QLabel(self.vanNiekMool_gbox)
        self.FamNamSur_lbl.setGeometry(QtCore.QRect(120, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.FamNamSur_lbl.setFont(font)
        self.FamNamSur_lbl.setObjectName(_fromUtf8("FamNamSur_lbl"))
        self.FamNamSur_le = QtGui.QLineEdit(self.vanNiekMool_gbox)
        self.FamNamSur_le.setGeometry(QtCore.QRect(70, 80, 271, 31))
        self.FamNamSur_le.setObjectName(_fromUtf8("FamNamSur_le"))
        self.Add_pbtn = QtGui.QPushButton(self.vanNiekMool_gbox)
        self.Add_pbtn.setGeometry(QtCore.QRect(100, 260, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Add_pbtn.setFont(font)
        self.Add_pbtn.setObjectName(_fromUtf8("Add_pbtn"))
        self.PairFamMem_gbox = QtGui.QGroupBox(self.vanNiekMool_gbox)
        self.PairFamMem_gbox.setGeometry(QtCore.QRect(430, 30, 491, 801))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PairFamMem_gbox.setFont(font)
        self.PairFamMem_gbox.setObjectName(_fromUtf8("PairFamMem_gbox"))
        self.Pair_pbtn = QtGui.QPushButton(self.PairFamMem_gbox)
        self.Pair_pbtn.setGeometry(QtCore.QRect(160, 30, 171, 41))
        self.Pair_pbtn.setObjectName(_fromUtf8("Pair_pbtn"))
        self.RandomPairFamMem_listw = QtGui.QListWidget(self.PairFamMem_gbox)
        self.RandomPairFamMem_listw.setGeometry(QtCore.QRect(50, 100, 391, 671))
        self.RandomPairFamMem_listw.setObjectName(_fromUtf8("RandomPairFamMem_listw"))
        self.ListofFamMem_label = QtGui.QLabel(self.vanNiekMool_gbox)
        self.ListofFamMem_label.setGeometry(QtCore.QRect(140, 300, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.ListofFamMem_label.setFont(font)
        self.ListofFamMem_label.setObjectName(_fromUtf8("ListofFamMem_label"))
        self.Remove_pbtn = QtGui.QPushButton(self.vanNiekMool_gbox)
        self.Remove_pbtn.setGeometry(QtCore.QRect(210, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Remove_pbtn.setFont(font)
        self.Remove_pbtn.setObjectName(_fromUtf8("Remove_pbtn"))
        self.vanNiekerk_rbtn = QtGui.QRadioButton(self.vanNiekMool_gbox)
        self.vanNiekerk_rbtn.setGeometry(QtCore.QRect(110, 150, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.vanNiekerk_rbtn.setFont(font)
        self.vanNiekerk_rbtn.setObjectName(_fromUtf8("vanNiekerk_rbtn"))
        self.Moolman_rbtn = QtGui.QRadioButton(self.vanNiekMool_gbox)
        self.Moolman_rbtn.setGeometry(QtCore.QRect(220, 150, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Moolman_rbtn.setFont(font)
        self.Moolman_rbtn.setObjectName(_fromUtf8("Moolman_rbtn"))
        self.SelectSur_lbl = QtGui.QLabel(self.vanNiekMool_gbox)
        self.SelectSur_lbl.setGeometry(QtCore.QRect(160, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.SelectSur_lbl.setFont(font)
        self.SelectSur_lbl.setObjectName(_fromUtf8("SelectSur_lbl"))
        self.Age_lbl = QtGui.QLabel(self.vanNiekMool_gbox)
        self.Age_lbl.setGeometry(QtCore.QRect(120, 210, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.Age_lbl.setFont(font)
        self.Age_lbl.setObjectName(_fromUtf8("Age_lbl"))
        self.Age_le = QtGui.QLineEdit(self.vanNiekMool_gbox)
        self.Age_le.setGeometry(QtCore.QRect(160, 200, 81, 31))
        self.Age_le.setObjectName(_fromUtf8("Age_le"))
        self.FamMem_listw = QtGui.QListWidget(self.vanNiekMool_gbox)
        self.FamMem_listw.setGeometry(QtCore.QRect(70, 330, 271, 501))
        self.FamMem_listw.setObjectName(_fromUtf8("FamMem_listw"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.vanNiekMool_gbox.setTitle(_translate("Dialog", "van Niekerk/Moolman Mossel Bay Holiday", None))
        self.FamNamSur_lbl.setText(_translate("Dialog", "Enter Family Participant Name", None))
        self.Add_pbtn.setText(_translate("Dialog", "Add", None))
        self.PairFamMem_gbox.setTitle(_translate("Dialog", "Pair family members (youngest with oldest)", None))
        self.Pair_pbtn.setText(_translate("Dialog", "Pair", None))
        self.ListofFamMem_label.setText(_translate("Dialog", "List of Family Members", None))
        self.Remove_pbtn.setText(_translate("Dialog", "Remove", None))
        self.vanNiekerk_rbtn.setText(_translate("Dialog", "van Niekerk", None))
        self.Moolman_rbtn.setText(_translate("Dialog", "Moolman", None))
        self.SelectSur_lbl.setText(_translate("Dialog", "Select Surname", None))
        self.Age_lbl.setText(_translate("Dialog", "Age:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

