from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_nature_marchandise import Ui_Form as Nature_marchandise_form
from ui_ajout_marchandise import Ui_Form as Ajout_marchandise_form
from ui_modifier_marchandise import Ui_Form as Modifier_marchandise_form

from multiobjet2 import *

class AjoutMarchandiseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ajout_marchandise_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.type.clear()
        self.ui.description.clear()
        super(AjoutMarchandiseWindow, self).closeEvent(event)

class ModifierMarchandiseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Modifier_marchandise_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.type.clear()
        self.ui.description.clear()
        super(ModifierMarchandiseWindow, self).closeEvent(event)

class NatureMarchandiseWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Nature_marchandise_form()
        self.ui.setupUi(self)
        self.display_table("SELECT * FROM marchandise")
        self.selectedItems = None

        #related_widgets
        self.widget = AjoutMarchandiseWindow()
        self.widget2 = ModifierMarchandiseWindow()

        #push_button_connections
        self.ui.recherche_marchandise.textChanged.connect(self.rechercher_marchandise)
        self.ui.nouveau_marchandise.clicked.connect(self.widget.show)
        self.ui.modifier_marchandise.clicked.connect(self.modifier_marchandise)
        self.ui.supprimer_marchandise.clicked.connect(self.supprimer_marchandise)
        self.ui.fermer_marchandise.clicked.connect(self.close)

        #externel_push_button_connections
        self.widget.ui.ajouter_ajout_marchandise.clicked.connect(self.ajouter_ajout_marchandise)
        self.widget.ui.fermer_ajout_marchandise.clicked.connect(self.fermer_ajouter_marchandise)
        self.widget2.ui.enregistrer_modifier_marchandise.clicked.connect(self.enregistrer_modifier_marchandise)
        self.widget2.ui.fermer_modifier_marchandise.clicked.connect(self.fermer_modifier_marchandise)

    def display_table(self, sql):
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.commit()
        row_count = len(myresult)
        self.ui.table_marchandise.setRowCount(row_count)
        for row in range(row_count):
            self.ui.table_marchandise.setVerticalHeaderItem(row,QTableWidgetItem(str(myresult[row][0])))
            self.ui.table_marchandise.setItem(row, 0, QTableWidgetItem(myresult[row][2]))
            self.ui.table_marchandise.setItem(row, 1, QTableWidgetItem(MultiObjet.getDescription(myresult[row][1])))

    def rechercher_marchandise(self):
        sql = "SELECT * FROM marchandise WHERE nature_marchandise LIKE '{}%'".format(self.ui.recherche_marchandise.text())
        self.display_table(sql)

    def modifier_marchandise(self):
        self.selectedItems = self.ui.table_marchandise.selectedItems()
        if len(self.selectedItems) == 2:
            self.widget2.show()
            self.widget2.ui.type.insert(self.selectedItems[0].text())
            self.widget2.ui.description.insertPlainText(self.selectedItems[1].text())

    def supprimer_marchandise(self):
        selectedItems = self.ui.table_marchandise.selectedItems()
        if len(selectedItems) >= 2:
            for i in range(0, len(selectedItems), 2):
                id = int(self.ui.table_marchandise.verticalHeaderItem(selectedItems[i].row()).text())
                mar = Marchandise(id, Marchandise.getMultiObjetId(id))
                mar.supprimer()
                self.ui.table_marchandise.removeRow(selectedItems[i].row())

    def ajouter_ajout_marchandise(self):
        self.widget.show()
        type = self.widget.ui.type.text()
        description = self.widget.ui.description.toPlainText()
        mar = Marchandise(0, 0)
        marchandise_id = mar.inserer(type, description)
        # clear line edits after inserting
        self.widget.ui.type.clear()
        self.widget.ui.description.clear()
        # displaying the added row
        availableRow = self.ui.table_marchandise.rowCount()
        self.ui.table_marchandise.insertRow(availableRow)
        self.ui.table_marchandise.setVerticalHeaderItem(availableRow, QTableWidgetItem(str(marchandise_id)))
        self.ui.table_marchandise.setItem(availableRow, 0, QTableWidgetItem(type))
        self.ui.table_marchandise.setItem(availableRow, 1, QTableWidgetItem(description))

    def fermer_ajouter_marchandise(self):
        self.widget.ui.type.clear()
        self.widget.ui.description.clear()
        self.widget.close()

    def enregistrer_modifier_marchandise(self):
        current_marchandise_id = int(self.ui.table_marchandise.verticalHeaderItem(self.selectedItems[0].row()).text())
        mar = Marchandise(current_marchandise_id, Marchandise.getMultiObjetId(current_marchandise_id))
        mar.modifier(self.widget2.ui.type.text(), self.widget2.ui.description.toPlainText())
        # update displayed table
        self.selectedItems[0].setText(self.widget2.ui.type.text())
        self.selectedItems[1].setText(self.widget2.ui.description.toPlainText())
        # clear line edits after modifying
        self.widget2.ui.type.clear()
        self.widget2.ui.description.clear()

    def fermer_modifier_marchandise(self):
        self.widget2.ui.type.clear()
        self.widget2.ui.description.clear()
        self.widget2.close()

if __name__ == "__main__":
    app = QApplication()
    widget = NatureMarchandiseWindow()
    widget.show()
    app.exec_()