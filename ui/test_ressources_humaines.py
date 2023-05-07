from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from auto_ui.ui_ressources_humaines import Ui_Form as Ressources_humaines_form

class RessourcesHumainesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ressources_humaines_form()
        self.ui.setupUi(self)
        self.ui.client.clicked.connect(self.showClient)
        self.ui.declarant.clicked.connect(self.showDeclarant)
        #self.ui.fournisseur.clicked.connect(self.showFournisseur)

    def showClient(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.client_2.form)
    def showDeclarant(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.declarant_2)
    #def showFournisseur(self):
        #self.ui.stackedWidget.setCurrentWidget(self.ui.fournisseur_2)

if __name__ == "__main__":
    app = QApplication()
    main = RessourcesHumainesWindow()
    main.show()
    app.exec_()