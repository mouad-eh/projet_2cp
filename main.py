from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import mysql.connector
from auto_ui.ui_login import Ui_Form as Login_form
from ui.test_main_window import MainWindow

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rotage2015002",
    database="projet_beta"
)
mycursor = mydb.cursor()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Login_form()
        self.ui.setupUi(self)
        self.widget = MainWindow()
        self.ui.login.clicked.connect(self.test)

    def test(self):
        username = self.ui.nom.text()
        password = self.ui.password.text()
        sql = "SELECT * FROM utilisateur WHERE identifiant= %s AND mot_de_passe = %s"
        mycursor.execute(sql, (username,password))
        myresult = mycursor.fetchall()
        mydb.commit()
        if(len(myresult) != 1):
            QMessageBox.about(self, "Error!", "Nom d'utilisateur ou mot de passe incorrect")
        else:
            self.close()
            self.widget.showMaximized()




if __name__ == "__main__":
    app = QApplication()
    widget = LoginWindow()
    widget.setWindowTitle("Login")
    widget.setFixedSize(800, 300)
    widget.show()
    app.exec_()