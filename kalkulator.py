from s1_uts_kalkulator import Ui_MainWindow, QtWidgets
from functools import partial

def varcustom(self):
    self._angka = ""
    self._angka2 = ""
    self._hasil = ""
    self._ops = ""


def signals(self):    
    self.bt_0.clicked.connect(partial(self.isinomor, 0))
    self.bt_1.clicked.connect(partial(self.isinomor, 1))
    self.bt_2.clicked.connect(partial(self.isinomor, 2))
    self.bt_3.clicked.connect(partial(self.isinomor, 3))
    self.bt_4.clicked.connect(partial(self.isinomor, 4))
    self.bt_5.clicked.connect(partial(self.isinomor, 5))
    self.bt_6.clicked.connect(partial(self.isinomor, 6))
    self.bt_7.clicked.connect(partial(self.isinomor, 7))
    self.bt_8.clicked.connect(partial(self.isinomor, 8))
    self.bt_9.clicked.connect(partial(self.isinomor, 9))
    self.bt_02.clicked.connect(partial(self.isinomor, "00"))
    self.bt_03.clicked.connect(partial(self.isinomor, "000"))

    self.bt_tambah.clicked.connect(partial(self.opspilih, "+"))
    self.bt_kurang.clicked.connect(partial(self.opspilih, "-"))
    self.bt_bagi.clicked.connect(partial(self.opspilih, "/"))
    self.bt_kali.clicked.connect(partial(self.opspilih, "*"))
    self.bt_persen.clicked.connect(partial(self.opspilih, "%"))
    self.bt_mod.clicked.connect(partial(self.opspilih, "mod"))

    self.bt_samadengan.clicked.connect(partial(self.opshitung, False, "="))

    self.bt_clear.clicked.connect(self.hapussemua)

def isinomor(self, addnomor):
    opstext = self.ed_ops.text() + str(addnomor)
    self.ed_ops.setText(opstext)

    self._hasil = ""
    self.ed_hasil.setText(self._hasil)

def opspilih(self, opsnya):
    if (self._ops == ""):
        self._ops = str(opsnya)
        self._angka = self.ed_ops.text()
        self.ed_ops.setText(self._angka + " " +self._ops+ " ")
        print("_angka "+self._angka)
    else:
        strsm = self.ed_ops.text()
        strsm = strsm.strip()
        self._angka2 = strsm.replace(self._angka+" "+self._ops, "")
        print("_angka2 "+self._angka2)
        self._angka2 = self._angka2.strip()

        if (self._angka2 == ""):
            self._ops = str(opsnya)
            self.ed_ops.setText(self._angka + " " +self._ops+ " ")
        else:
            self.opshitung(True, opsnya)


def opshitung(self, opslagi, opsnya):
    strsm = self.ed_ops.text()
    strsm = strsm.strip()
    self._angka2 = strsm.replace(self._angka+" "+self._ops, "")
    print("_angka2 "+self._angka2)
    self._angka2 = self._angka2.strip()
    print("_angka2 "+self._angka2)
    
    if (self._angka2 != ""):
        if str(self._ops)=="+":
            self._hasil=str(int(self._angka) + int(self._angka2))
        elif str(self._ops)=="-":
            self._hasil=str(int(self._angka) - int(self._angka2))
        elif str(self._ops)=="/":
            #bagi
            self._hasil=str(int(self._angka) / int(self._angka2))
        elif str(self._ops)=="*":
            #perkalian
            self._hasil=str(int(self._angka) * int(self._angka2))
        elif str(self._ops)=="%": 
            #persen dari
            self._hasil=str(int(self._angka) * (int(self._angka2) / 100))
        elif str(self._ops)=="mod":
            #mod
            self._hasil=str(int(self._angka) % int(self._angka2))
        elif str(self._ops)=="^":
            #mod
            self._hasil=str(int(self._angka) ** int(self._angka2))
        else:
            self._hasil="Unknown Operator"

    self.ed_hasil.setText(self._hasil)
    
    if (opslagi==True):
        if (self._hasil != ""):
            self.ed_ops.setText(self._hasil)
            self._hasil = ""
            self._angka2 = ""
            self._ops = ""
            self.opspilih(opsnya)

    else:
        self.ed_ops.clear()
        self._ops = ""
        self._angka = ""
        self._angka2 = ""
        self._hasil = ""


def hapussemua(self):
    self._ops = ""
    self._angka = ""
    self._angka2 = ""
    self._hasil = ""
    self.ed_ops.clear()
    self.ed_hasil.clear()
    

Ui_MainWindow.signals = signals
Ui_MainWindow.varcustom = varcustom
Ui_MainWindow.hapussemua = hapussemua
Ui_MainWindow.isinomor = isinomor
Ui_MainWindow.opshitung = opshitung
Ui_MainWindow.hapussemua = hapussemua
Ui_MainWindow.opspilih = opspilih

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    ui.varcustom()
    MainWindow.show()
    sys.exit(app.exec_())
