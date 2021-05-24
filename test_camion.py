from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_camion import Ui_Form as Camion_form
from ui_ajout_camion import Ui_Form as Ajout_camion_form
from ui_modifier_camion import Ui_Form as Modifier_camion_form

from multiobjet2 import *

def charToString(dispo):
    if dispo == 'D':
        return "Disponible"
    elif dispo == 'N':
        return "Non disponible"

def stringToChar(dispo):
    if dispo == "Disponible":
        return 'D'
    elif dispo == "Non disponible":
        return 'N'

def stringToIndex(dispo):
    if dispo == "Disponible":
        return 0
    elif dispo == "Non disponible":
        return 1

class AjoutCamionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ajout_camion_form()
        self.ui.setupUi(self)

    def closeEvent(self,event):
        self.ui.matricule.clear()
        self.ui.disponibilite.setCurrentIndex(-1)
        self.ui.description.clear()
        super(AjoutCamionWindow, self).closeEvent(event)

class ModifierCamionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Modifier_camion_form()
        self.ui.setupUi(self)

    def closeEvent(self,event):
        self.ui.matricule.clear()
        self.ui.disponibilite.setCurrentIndex(-1)
        self.ui.description.clear()
        super(ModifierCamionWindow, self).closeEvent(event)

class CamionWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Camion_form()
        self.ui.setupUi(self)
        #self.ui.disponibilite.setCurrentIndex(-1)
        self.display_table("SELECT * FROM camion")
        self.selectedItems = None

        #related_widgets
        self.widget = AjoutCamionWindow()
        self.widget2 = ModifierCamionWindow()

        #push_button_connections
        self.ui.recherche_matricule.textChanged.connect(self.rechercher_matricule)
        self.ui.nouveau_camion.clicked.connect(self.widget.show)
        self.ui.modifier_camion.clicked.connect(self.modifier_camion)
        self.ui.supprimer_camion.clicked.connect(self.supprimer_camion)
        self.ui.fermer_camion.clicked.connect(self.close)

        #externel_push_button_connections
        self.widget.ui.ajouter_ajout_camion.clicked.connect(self.ajouter_ajout_camion)
        self.widget.ui.fermer_ajout_camion.clicked.connect(self.fermer_ajouter_camion)
        self.widget2.ui.enregistrer_modifier_camion.clicked.connect(self.enregistrer_modifier_camion)
        self.widget2.ui.fermer_modifier_camion.clicked.connect(self.fermer_modifier_camion)

    def display_table(self, sql):
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.commit()
        row_count = len(myresult)
        self.ui.camion_table.setRowCount(row_count)
        for row in range(row_count):
            self.ui.camion_table.setVerticalHeaderItem(row, QTableWidgetItem(str(myresult[row][0])))
            self.ui.camion_table.setItem(row, 0, QTableWidgetItem(myresult[row][1]))
            self.ui.camion_table.setItem(row, 2, QTableWidgetItem(MultiObjet.getDescription(myresult[row][2])))
            self.ui.camion_table.setItem(row, 1, QTableWidgetItem(charToString(myresult[row][3])))

    def rechercher_matricule(self):
        sql = "SELECT * FROM camion WHERE matricule LIKE '{}%'".format(self.ui.recherche_matricule.text())
        self.display_table(sql)

    def modifier_camion(self):
        self.selectedItems = self.ui.camion_table.selectedItems()
        if len(self.selectedItems) == 3:
            self.widget2.show()
            self.widget2.ui.matricule.insert(self.selectedItems[0].text())
            self.widget2.ui.disponibilite.setCurrentIndex(stringToIndex(self.selectedItems[1].text()))
            self.widget2.ui.description.insertPlainText(self.selectedItems[2].text())

    def supprimer_camion(self):
        selectedItems = self.ui.camion_table.selectedItems()
        if len(selectedItems) >= 3:
            for i in range(0, len(selectedItems), 3):
                id = int(self.ui.camion_table.verticalHeaderItem(selectedItems[i].row()).text())
                cam = Camion(id, Camion.getMultiObjetId(id))
                cam.supprimer()
                self.ui.camion_table.removeRow(selectedItems[i].row())

    def ajouter_ajout_camion(self):
        self.widget.show()
        matricule = self.widget.ui.matricule.text()
        disponibilite = self.widget.ui.disponibilite.currentText()
        description = self.widget.ui.description.toPlainText()
        cam = Camion(0, 0)
        camion_id = cam.inserer(matricule, stringToChar(disponibilite), description)
        # clear line edits after inserting
        self.widget.ui.matricule.clear()
        self.widget.ui.disponibilite.setCurrentIndex(-1)
        self.widget.ui.description.clear()
        # displaying the added row
        availableRow = self.ui.camion_table.rowCount()
        self.ui.camion_table.insertRow(availableRow)
        self.ui.camion_table.setVerticalHeaderItem(availableRow, QTableWidgetItem(str(camion_id)))

        self.ui.camion_table.setItem(availableRow, 0, QTableWidgetItem(matricule))
        self.ui.camion_table.setItem(availableRow, 1, QTableWidgetItem(disponibilite))
        self.ui.camion_table.setItem(availableRow, 2, QTableWidgetItem(description))

    def fermer_ajouter_camion(self):
        self.widget.ui.matricule.clear()
        self.widget.ui.disponibilite.setCurrentIndex(-1)
        self.widget.ui.description.clear()
        self.widget.close()

    def enregistrer_modifier_camion(self):
        current_camion_id = int(self.ui.camion_table.verticalHeaderItem(self.selectedItems[0].row()).text())
        cam = Camion(current_camion_id, Camion.getMultiObjetId(current_camion_id))
        print(Camion.getMultiObjetId(current_camion_id))
        cam.modifier(self.widget2.ui.matricule.text(), stringToChar(self.widget2.ui.disponibilite.currentText()), self.widget2.ui.description.toPlainText())
        # update displayed table
        self.selectedItems[0].setText(self.widget2.ui.matricule.text())
        self.selectedItems[1].setText(self.widget2.ui.disponibilite.currentText())
        self.selectedItems[2].setText(self.widget2.ui.description.toPlainText())
        # clear line edits after modifying
        self.widget2.ui.matricule.clear()
        self.widget2.ui.disponibilite.setCurrentIndex(-1)
        self.widget2.ui.description.clear()

    def fermer_modifier_camion(self):
        self.widget2.ui.matricule.clear()
        self.widget2.ui.disponibilite.setCurrentIndex(-1)
        self.widget2.ui.description.clear()
        self.widget2.close()
#todo : handle all input input errors matricule and description
if __name__ == "__main__":
    app = QApplication()
    widget = CamionWindow()
    widget.show()
    app.exec_()