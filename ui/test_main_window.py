from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from auto_ui.ui_main_window import Ui_MainWindow as Main_form

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Main_form()
        self.ui.setupUi(self)
        self.ui.dossiers_2.clicked.connect(self.show_dossiers)
        self.ui.factures_2.clicked.connect(self.show_factures)
        self.ui.factures_2.clicked.connect(self.ui.factures.ui.facture.loaddata)

        self.ui.res_humaines_2.clicked.connect(self.show_res_humaines)
        self.ui.res_materielles_2.clicked.connect(self.show_res_materielles)
    def show_dossiers(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.dossiers)
    def show_factures(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.factures)
    def show_res_humaines(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.res_humaines)
    def show_res_materielles(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.res_materielles)
if __name__ == "__main__" :
    app = QApplication()
    main = MainWindow()
    main.setWindowTitle("Logiciel de facturation")
    main.show()
    app.exec_()