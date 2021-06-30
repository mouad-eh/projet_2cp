from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_main_window import Ui_MainWindow as Main_form
from test_ressources import GestionRessourcesWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Main_form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.show_gestion_dossier)
        self.ui.pushButton_3.clicked.connect(self.show_gestion_ressources)
    def show_gestion_ressources(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
    def show_gestion_dossier(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
if __name__ == "__main__" :
    app = QApplication()
    main = MainWindow()
    main.show()
    app.exec_()