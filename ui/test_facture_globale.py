from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from auto_ui.ui_facture_golable import Ui_Form as Facture_global_form

class FactureGlobalWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Facture_global_form()
        self.ui.setupUi(self)
        self.ui.ajout_facture.clicked.connect(self.showAjoutFacture)
        self.ui.consulter_facture.clicked.connect(self.showConsulterFacture)

    def showAjoutFacture(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ajout_facture_2)
    def showConsulterFacture(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.consulter_facture_2)

if __name__ == "__main__":
    app = QApplication()
    main = FactureGlobalWindow()
    main.show()
    app.exec_()