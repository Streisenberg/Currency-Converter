import sys 
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from exchange_app import Ui_MainWindow
import requests
import json

class exchange(QMainWindow):
    
    def __init__(self):
        super(exchange, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        self.ui.pushButton.clicked.connect(self.hesapla)

    def hesapla(self):

        url = "https://api.exchangeratesapi.io/latest?base="
        miktar = int(self.ui.txt_para.text())
        sonuc = 0

        

        if self.ui.comboBox.currentText() == "Euro":

            result = requests.get(url+"EUR")
            result = json.loads(result.text)
            sonuc = miktar*result["rates"]["TRY"]

        elif self.ui.comboBox.currentText() == "Dolar":
            
            result = requests.get(url+"USD")
            result = json.loads(result.text)
            sonuc = miktar*result["rates"]["TRY"]



        elif self.ui.comboBox.currentText() == "Sterlin":

            result = requests.get(url+"GBP")
            result = json.loads(result.text)
            sonuc = miktar*result["rates"]["TRY"]

        elif self.ui.comboBox.currentText() == "Yuan":

            result = requests.get(url+"CNY")
            result = json.loads(result.text)
            sonuc = miktar*result["rates"]["TRY"]


        
        self.ui.lbl_sonuc.setText("Sonuç: " + str(sonuc))

        

def app():
    app = QApplication(sys.argv)
    win = exchange()
    win.show()
    sys.exit(app.exec_())


app()
