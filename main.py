import csv
import pandas        #pip install pandas
import sys
from PyQt5 import QtWidgets, QtCore, QtGui         #pip install PyQt5
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox


def data_base():
    file = open("stock.csv", "r")
    reader = csv.reader(file)
    lists = []
    for row in reader:
        lists.append(row)
    lists.remove(['PRODUCT', 'PRODUCT_CODE', 'COST', 'STOCK'])
    file.flush()

    print(lists)
    return lists

def product_sub(ind,stak):
    stk = pandas.read_csv("stock.csv")
    stk.loc[ind, "STOCK"] = str(stak-1)
    stk.to_csv(r"stock.csv", index=False)

class page(QDialog):
    def __init__(self):
        super (page,self).__init__()
        loadUi("vm.ui", self)
        global reg
        reg = True

        print("start")
        self.lable.setText("VendingMachin")
        self._1.clicked.connect(lambda: self.m1())
        self._2.clicked.connect(lambda: self.m2())
        self._3.clicked.connect(lambda: self.m3())
        self._4.clicked.connect(lambda: self.m4())
        self._5.clicked.connect(lambda: self.m5())
        self._6.clicked.connect(lambda: self.m6())
        self._7.clicked.connect(lambda: self.m7())
        self._8.clicked.connect(lambda: self.m8())
        self._9.clicked.connect(lambda: self.m9())
        self._0.clicked.connect(lambda: self.m0())
        self.save.clicked.connect(lambda: self.save_ch())
        self.back_syc.clicked.connect(lambda: self.back_sim())
        self.product.clicked.connect(lambda: self.producttake())
        self.Enter.clicked.connect(lambda: self.menter())
        self.cancel.clicked.connect(lambda: self.mcancel())
        self.back.clicked.connect(lambda: self.mback())
        self.Mng.clicked.connect(lambda: self.mmanage())
        self.lable_2.setText("")
        self.product.setVisible(False)
        self.Manage.setVisible(False)

    def m1(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <=15:
            self.display.setText(text+"1")
        if "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"1")
    def m2(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"2")
        if "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"2")
    def m3(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"3")
        if "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"3")
    def m4(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"4")
        if "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"4")
    def m5(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"5")
        if "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"5")
    def m6(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"6")
        if "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"6")
    def m7(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"7")
        if "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"7")
    def m8(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"8")
        if "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"8")
    def m9(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"9")
        if "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"9")
    def m0(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"0")
        if "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"0")

    def mmanage(self):
        global manade
        manage = True
        global reg
        reg = False
        self.display.setText("Passcode:")

    def mcancel(self):
        self.display.setText("Product code:")
        self.lable_2.setText("")

    def mback(self):
        text = self.display.text()
        if "Product code:" in text and len(text)>14:
            x = len(text) - 1
            a = text[0:x]
            self.display.setText(a)
        elif "Passcode:" in text and len(text)>9:
            x = len(text) - 1
            a = text[0:x]
            self.display.setText(a)

    def menter(self):
        text = self.display.text()
        if "Product code:" in text and len(text) == 16:
            prd_code = text[13:16]
            print(prd_code)
            try:
                self.product_get(prd_code)
            except:
                print()
        elif "Passcode:" in text and len(text) == 11:
            pass_code = text[9:11]
            if pass_code == "00":
                self.table()
                self.display.setText("Product code:")
                self.lable_2.clear()
            else:
                self.display.setText("Product code:")

    def table(self):
        self.Manage.setVisible(True)
        self.tableWidget.setColumnWidth(0,180)
        self.tableWidget.setColumnWidth(1, 140)
        self.tableWidget.setColumnWidth(2, 110)
        self.tableWidget.setColumnWidth(3, 123)
        list = data_base()
        row = 0
        clm = 0
        self.tableWidget.setRowCount(len(list))
        for i in list:
            for item in i:
                self.tableWidget.setItem(0, clm, QtWidgets.QTableWidgetItem(item))
                clm+=1
        global tlist
        tlist =[]
        for row in range(9):
            slist = []
            for col in range(4):
                a = self.tableWidget.item(row, col).text()
                slist.append(a)
            tlist.append(slist)
        print(tlist)

    def save_ch(self):
        chk,newlist = self.checkdiff()
        if chk == True:
            pass
        else:
            print("righ")
            data = pandas.DataFrame(newlist,columns=["PRODUCT","PRODUCT_CODE","COST","STOCK"])
            data.to_csv("stock.csv", index=False)

    def back_sim(self):
        print("good")
        chk, newlist = self.checkdiff()
        if chk == True:
            self.Manage.setVisible(False)
        else:
            print(-1)
            qm = QtWidgets.QMessageBox
            print(-2)
            ret = qm.question(self,'', "Do you want to save the change before leaving?", qm.Yes | qm.No)
            print(-3)
            if ret == qm.Yes:
                self.save_ch()
                self.Manage.setVisible(False)
            else:
                self.Manage.setVisible(False)


    def checkdiff(self):
        list = data_base()
        _2nd = []
        for row in range(9):
            slist = []
            for col in range(4):
                a = self.tableWidget.item(row, col).text()
                slist.append(a)
            _2nd.append(slist)
        print(list)
        print(_2nd)
        if _2nd == list:
            chk = True
        else:
            chk = False
        print(chk)
        return chk,_2nd

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def producttake(self):
        self.display.setText("Product code:")
        self.lable_2.setText(" ")
        self.lable.setText("VendingMachine")
        self.product.setVisible(False)

    def productshow(self,product):
        self.display.clear()
        self.display.setText(product)
        self.product.setVisible(True)
        if product == 'Coke':
            self.product.setIcon(QtGui.QIcon('product/co.png'))
        if product == 'Lays':
            self.product.setIcon(QtGui.QIcon('product/la.png'))
        if product == 'Pepsi':
            self.product.setIcon(QtGui.QIcon('product/pe.png'))
        if product == 'Maaza':
            self.product.setIcon(QtGui.QIcon('product/ma.png'))
        if product == 'Bingo':
            self.product.setIcon(QtGui.QIcon('product/bi.png'))
        if product == 'Water':
            self.product.setIcon(QtGui.QIcon('product/wa.png'))
        if product == 'Diary Milk':
            self.product.setIcon(QtGui.QIcon('product/da.png'))
        if product == 'Doritos':
            self.product.setIcon(QtGui.QIcon('product/do.png'))
        if product == 'Mountain dew':
            self.product.setIcon(QtGui.QIcon('product/md.png'))



    def product_get(self, p_code):
        lists = data_base()
        selected = int(p_code)
        money = int(self.wallet.text())
        nop = False
        stkre = True
        for i in (lists):
            if i[3] <= '0':
                nop = True

        if nop != True:
            for i in (lists):
                if selected == int(i[1]):
                    if money > int(i[2]):
                        change = money - int(i[2])
                        product_sub(lists.index(i), int(i[3]))
                        wallet = change
                    else:
                        print("money in wallet is not enough\nYour drink is cancled")
                        change = money
                        break
                    product = str(i[0])
                    self.lable_2.setText("Rs: "+i[2])
                    self.productshow(product)
                    self.lable.setText("Thank you. Please visit again")
                    if int(selected) != int(i[1]):
                        print(int(selected) != int(i[1]))
                        self.lable_2.setText("Invalid code")
                        self.display.setText("Product code:")

            self.wallet.setText(str(wallet))
        else:
            self.lable_2.setText("stock need to be added")
            self.mmanage()

app = QApplication(sys.argv)
mainwindow = page()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(877)
widget.setFixedHeight(753)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("exit")
