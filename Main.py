####################################################################Familyholidayprogram.py####################################################################
from __future__ import division
import vanniekerkholiday
from PyQt4 import QtCore, QtGui

###########################################################################Variables###########################################################################
list1 = []

############################################################################Classes############################################################################
class familyholiday(QtGui.QDialog, vanniekerkholiday.Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.Add_pbtn.clicked.connect(self.addList)
        self.Remove_pbtn.clicked.connect(self.removeItem)
        self.Pair_pbtn.clicked.connect(self.pairlist)

    def addList(self):
        name = ""
        age = self.Age_le.text()

        if self.vanNiekerk_rbtn.isChecked():
            name = self.FamNamSur_le.text() + " van Niekerk"
        elif self.Moolman_rbtn.isChecked():
            name = self.FamNamSur_le.text() + " Moolman"

        self.FamMem_listw.addItem(name + ", " + age + " years of age")

        self.FamNamSur_le.setText('')
        self.Age_le.setText('')
        list1.append({'Name': name, 'age': age})

    def removeItem(self):
        self.FamMem_listw.takeItem(self.FamMem_listw.currentRow())

    def pairlist(self):
        newlist = sorted(list1, key=lambda k: k['age'])
        count = len(newlist) - 1
        for x in newlist:
            if count + 1 == (len(newlist))/2:
                break
            self.RandomPairFamMem_listw.addItem(x['Name'] + ' ' + newlist[count]['Name'])
            count = count - 1

########################################################################Initiate Program########################################################################
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = familyholiday()
    Dialog.show()
    sys.exit(app.exec_())