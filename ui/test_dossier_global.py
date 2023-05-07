from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from auto_ui.ui_dossier_global import Ui_Form as Dossier_global_form

class DossierGlobalWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Dossier_global_form()
        self.ui.setupUi(self)
        self.ui.ajout_dossier.clicked.connect(self.showAjoutDossier)
        self.ui.consulter_dossier.clicked.connect(self.showConsulterDossier)
        self.ui.bon_de_visite.clicked.connect(self.showBonDeVisite)
        self.ui.bon_de_sortie.clicked.connect(self.showBonDeSortie)

    def showAjoutDossier(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ajout_dossier_2)
    def showConsulterDossier(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.consulter_dossier_2)
    def showBonDeVisite(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bon_de_visite_2)
    def showBonDeSortie(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bon_de_sortie_2)

if __name__ == "__main__":
    app = QApplication()
    main = DossierGlobalWindow()
    main.show()
    app.exec_()