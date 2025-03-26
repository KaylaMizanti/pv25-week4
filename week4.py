from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 420) 

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.label = QtWidgets.QLabel("Product", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 60, 20))
        self.label_2 = QtWidgets.QLabel("Quantity", self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 60, 20))
        self.label_3 = QtWidgets.QLabel("Discount", self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 60, 20))
        self.label_4 = QtWidgets.QLabel("Total: Rp. 0", self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 300, 300, 20))

        self.label_5 = QtWidgets.QLabel("Kayla Mizanti - F1D022127", self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 320, 300, 20))
        self.label_5.setStyleSheet("font-weight: bold; color: gray;") 

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 30, 200, 22))
        self.comboBox.addItems(["", "Bimoli (Rp. 20,000)", "Sugar (Rp. 15,000)", "Milk (Rp. 10,000)"])

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 50, 20))
        self.lineEdit.setValidator(QtGui.QIntValidator(1, 100))

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 90, 50, 22))
        self.comboBox_2.addItems(["0%", "5%", "10%", "20%"])

        self.pushButton = QtWidgets.QPushButton("Add to Cart", self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 130, 100, 30))
        self.pushButton.clicked.connect(self.add_to_cart)

        self.pushButton_2 = QtWidgets.QPushButton("Clear", self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 130, 100, 30))
        self.pushButton_2.clicked.connect(self.clear_cart)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 170, 370, 120))
        self.listWidget.setWordWrap(True) 
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)  

        MainWindow.setCentralWidget(self.centralwidget)

    def add_to_cart(self):
        product_text = self.comboBox.currentText()
        quantity = self.lineEdit.text()
        discount_text = self.comboBox_2.currentText()

        if not product_text or not quantity:
            self.label_4.setText("Invalid Input")  
            return  

        quantity = int(quantity)
        price = int(product_text.split("Rp. ")[1].split(")")[0].replace(",", ""))
        discount = int(discount_text.replace("%", ""))

        discounted_price = price * (1 - discount / 100) * quantity
        cart_text = f"{product_text} - {quantity} x Rp. {price:,} (disc {discount}%)"

        item = QtWidgets.QListWidgetItem(cart_text)
        item.setToolTip(cart_text) 
        item.setSizeHint(QtCore.QSize(350, 40)) 
        self.listWidget.addItem(item)

        total = sum([
            float(item.text().split("Rp. ")[-1].split(" ")[0].replace(",", ""))
            for item in self.listWidget.findItems("*", QtCore.Qt.MatchWildcard)
        ])
        self.label_4.setText(f"Total: Rp. {int(total):,}")

    def clear_cart(self):
        self.listWidget.clear()
        self.label_4.setText("Total: Rp. 0")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
