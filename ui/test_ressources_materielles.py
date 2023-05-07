from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from auto_ui.ui_ressources_materielles import Ui_Form as Ressources_materielles_form

class RessourcesMateriellesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ressources_materielles_form()
        self.ui.setupUi(self)
        self.ui.navire.clicked.connect(self.showNavire)
        self.ui.pays.clicked.connect(self.showPays)
        self.ui.monnaie.clicked.connect(self.showMonnaie)

    def showNavire(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.navire_2)
    def showPays(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pays_2)
    def showMonnaie(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.monnaie_2)

if __name__ == "__main__":
    app = QApplication()
    main = RessourcesMateriellesWindow()
    main.show()
    app.exec_()