from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_gestion_ressources import Ui_Form as Gestion_ressources_form

class GestionRessourcesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Gestion_ressources_form()
        self.ui.setupUi(self)
        self.ui.navire.clicked.connect(self.showNavire)
        self.ui.marchandise.clicked.connect(self.showMarchandise)
        self.ui.camion.clicked.connect(self.showCamion)
        self.ui.pays.clicked.connect(self.showPays)
        self.ui.monnaie.clicked.connect(self.showMonnaie)

    def showNavire(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
    def showMarchandise(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
    def showCamion(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
    def showPays(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
    def showMonnaie(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)

if __name__ == "__main__":
    app = QApplication()
    main = GestionRessourcesWindow()
    main.show()
    app.exec_()