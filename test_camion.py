from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_camion import Ui_Form as Camion_form
from ui_ajout_camion import Ui_Form as Ajout_camion_form
from ui_modifier_camion import Ui_Form as Modifier_camion_form

from multiobjet2 import *

class AjoutCamionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ajout_camion_form()
        self.ui.setupUi(self)

class ModifierCamionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Modifier_camion_form()
        self.ui.setupUi(self)

class CamionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Camion_form()
        self.ui.setupUi(self)

        self.widget = AjoutCamionWindow()
        self.widget2 = ModifierCamionWindow()


if __name__ == "__main__":
    app = QApplication()
    widget = CamionWindow()
    widget.show()
    app.exec_()