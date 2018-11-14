####################################################################Familyholidayprogram.py####################################################################
from __future__ import division
import vanniekerkholiday
from PyQt4 import QtCore, QtGui


###########################################################################Variables###########################################################################
names = [0, 1, 2
         ]
x = 1




############################################################################Classes############################################################################
class familyholiday(QtGui.QDialog, vanniekerkholiday.Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.Add_pbtn.clicked.connect(self.addList)
        self.Remove_pbtn.clicked.connect(self.removeItem)
        self.Pair_pbtn.clicked.connect(self.pairlist)



    def addList(self):

        if self.vanNiekerk_rbtn.isChecked():
            self.FamMem_listw.addItem(self.FamNamSur_le.text() + " van Niekerk" + ", " + self.Age_le.text() + " years of age")
        elif self.Moolman_rbtn.isChecked():
            self.FamMem_listw.addItem(self.FamNamSur_le.text() + " Moolman" + ", " + self.Age_le.text() + " years of age")

        self.FamNamSur_le.setText('')
        self.Age_le.setText('')



    def removeItem(self):
        self.FamMem_listw.takeItem(self.FamMem_listw.currentRow())


    def pairlist(self):
        for x in names:
            print(names)


########################################################################Initiate Program########################################################################
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = familyholiday()
    Dialog.show()
    sys.exit(app.exec_())