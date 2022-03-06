#import
import csv
import pandas        #pip install pandas
import sys
from PyQt5 import QtWidgets, QtCore, QtGui         #pip install PyQt5
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox


def data_base(): #data from csv file
    file = open("stock.csv", "r")
    reader = csv.reader(file)
    lists = []
    for row in reader:
        lists.append(row)
    lists.remove(['PRODUCT', 'PRODUCT_CODE', 'COST', 'STOCK'])
    file.flush()
    return lists

def product_sub(ind,stak):# -1 the no of product
    stk = pandas.read_csv("stock.csv")
    stk.loc[ind, "STOCK"] = str(stak-1)
    stk.to_csv(r"stock.csv", index=False)

class page(QDialog):#class function to use the gui created
    def __init__(self):
        super (page,self).__init__()
        loadUi("vm.ui", self)
        global reg
        reg = True
        #self using the variables from the .ui file
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
        self.display.setText("Enter Money:")
        self.wallet.setText("0")
        self.product.setVisible(False)
        self.Manage.setVisible(False)
        
        
    #===================================================================================
    # function for the buttons
    def m1(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <=15:
            self.display.setText(text+"1")
        elif "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"1")
        elif "Enter Money:" in text and len(text)<=15:
            self.display.setText(text+"1")
        
    def m2(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"2")
        elif "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"2")
        elif "Enter Money:" in text and len(text)<=15:
            self.display.setText(text+"2")
    def m3(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"3")
        elif "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"3")
        elif "Enter Money:" in text and len(text)<=15:
            self.display.setText(text+"3")
    def m4(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"4")
        elif "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"4")
        elif "Enter Money:" in text and len(text)<=15:
            self.display.setText(text+"4")
    def m5(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"5")
        elif "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"5")
        elif "Enter Money:" in text and len(text)<=15:
            self.display.setText(text+"5")
    def m6(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"6")
        elif "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"6")
        elif "Enter Money:" in text and len(text)<=15:
            self.display.setText(text+"6")
    def m7(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"7")
        elif "Passcode:" in text and len(text) < 11: 
            self.display.setText(text+"7")
        elif "Enter Money:" in text and len(text)<=15:
            self.display.setText(text+"7")
    def m8(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"8")
        elif "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"8")
        elif "Enter Money:" in text and len(text)<=15:
            self.display.setText(text+"8")
    def m9(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"9")
        elif "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"9")
        elif "Enter Money:" in text and len(text)<=15:
            self.display.setText(text+"9")
    def m0(self):
        text = self.display.text()
        if "Product code:" in text and len(text) <= 15:
            self.display.setText(text+"0")
        elif "Passcode:" in text and len(text) < 11:
            self.display.setText(text+"0")
        elif "Enter Money:" in text and len(text)<=15:
            self.display.setText(text+"0")
    #===================================================================================
    def mmanage(self):
        global manade
        manage = True
        global reg
        reg = False
        self.display.setText("Passcode:")

    def mcancel(self):
        if  "Enter Money:" not in self.display.text():
            self.display.setText("Product code:")
            self.lable_2.setText("")

    def mback(self):
        text = self.display.text()
        if  "Enter Money:" in text and len(text) >12:
            x = len(text) - 1
            a = text[0:x]
            self.display.setText(a)
        elif "Product code:" in text and len(text)>10:
            x = len(text) - 1
            a = text[0:x]
            self.display.setText(a)
        elif "Passcode:" in text and len(text)>9:
            x = len(text) - 1
            a = text[0:x]
            self.display.setText(a)

    def menter(self):# Enter button
        text = self.display.text()
        #product code checking(by user)
        if "Product code:" in text and len(text) == 16:
            prd_code = text[13:16]
            try:
                self.product_get(prd_code)
            except:
                print()
        #pass code enter (by owner)
        elif "Passcode:" in text and len(text) == 11:
            pass_code = text[9:11]
            if pass_code == "00":
                self.table()
                self.display.setText("Product code:")
                self.lable_2.clear()
            else:
                self.display.setText("Product code:")
        elif "Enter Money:" in text and len(text) <= 16:
            a = text[12:]
            b = self.wallet.text()
            if len(a) >1:
                self.lable.setText("")
                self.wallet.setText(str(int(a)+int(b)))
                self.display.setText("Product code:")
            
        
    #===================================================================================
    
    # creating a gui table from the csv file 
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
       
    #saving the changed file  
    def save_ch(self):
        chk,newlist = self.checkdiff()
        if chk == True:
            pass
        else:
            data = pandas.DataFrame(newlist,columns=["PRODUCT","PRODUCT_CODE","COST","STOCK"])
            data.to_csv("stock.csv", index=False)
   
    #closing the table
    def back_sim(self):
        chk, newlist = self.checkdiff()
        if chk == True:
            self.Manage.setVisible(False)
        else:
            qm = QtWidgets.QMessageBox
            ret = qm.question(self,'', "Do you want to save the change before leaving?", qm.Yes | qm.No)
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
        if _2nd == list:
            chk = True
        else:
            chk = False
        return chk,_2nd

   #===================================================================================
    
    def producttake(self):
        self.display.setText("Product code:")
        self.lable_2.setText(" ")
        self.lable.setText("VendingMachine")
        self.product.setVisible(False)
        
    # Displaying the bought item
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


    #checking and displaying the product 
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
                        self.lable.setText("money in wallet is not enough\nYour drink is cancled")
                        self.display.setText("Enter Money:")
                        change = money
                        break
                    product = str(i[0])
                    self.lable_2.setText("Rs: "+i[2]+"\tBalance: "+str(change))
                    self.productshow(product)
                    self.lable.setText("Thank you. Please visit again")
                    if int(selected) != int(i[1]):
                        self.lable_2.setText("Invalid code")
                        self.display.setText("Product code:")

            self.wallet.setText(str(wallet))
        else:
            self.lable_2.setText("stock need to be added")
            self.mmanage()
            
#===================================================================================

#calling the class function
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
    
# ========================================================END OF PROGRAM==========================================
