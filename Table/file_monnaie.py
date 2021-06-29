from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_monnaie import Ui_Form as Monnaie_form
from ui_ajout_monnaie import Ui_Form as Ajout_monnaie_form
from ui_modifier_monnaie import Ui_Form as Modifier_monnaie_form

from classes import *

class AjoutMonnaieWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ajout_monnaie_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.code_monnaie.clear()
        self.ui.libelle_monnaie.clear()
        self.ui.taux_change.clear()
        super(AjoutMonnaieWindow, self).closeEvent(event)

class ModifierMonnaieWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Modifier_monnaie_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.code_monnaie.clear()
        self.ui.libelle_monnaie.clear()
        self.ui.taux_change.clear()
        super(ModifierMonnaieWindow, self).closeEvent(event)

class MonnaieWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Monnaie_form()
        self.ui.setupUi(self)
        self.display_table("SELECT * FROM monnaie")
        self.selectedItems = None

        #related_widgets
        self.widget = AjoutMonnaieWindow()
        self.widget2 = ModifierMonnaieWindow()

        #push_button_connections

        # la recherche sera faite plus tard(
            # recherche par code_monnaie
            # recherche par libelle
        #)

        #self.ui.rechercher_monnaie.textChanged.connect(self.rechercher_monnaie)
        self.ui.nouveau_monnaie.clicked.connect(self.widget.show)
        self.ui.modifier_monnaie.clicked.connect(self.modifier_monnaie)
        self.ui.supprimer_monnaie.clicked.connect(self.supprimer_monnaie)
        self.ui.fermer_monnaie.clicked.connect(self.close)

        #externel_push_button_connections
        self.widget.ui.ajouter_ajout_monnaie.clicked.connect(self.ajouter_ajout_monnaie)
        self.widget.ui.fermer_ajout_monnaie.clicked.connect(self.fermer_ajout_monnaie)
        self.widget2.ui.enregistrer_modifier_monnaie.clicked.connect(self.enregistrer_modifier_monnaie)
        self.widget2.ui.fermer_modifier_monnaie.clicked.connect(self.fermer_modifier_monnaie)

    def display_table(self, sql):
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.commit()
        row_count = len(myresult)
        self.ui.monnaie_table.setRowCount(row_count)

        for row in range(row_count):
            self.ui.monnaie_table.setVerticalHeaderItem(row,QTableWidgetItem(str(myresult[row][0])))
            self.ui.monnaie_table.setItem(row, 0, QTableWidgetItem(myresult[row][1]))
            self.ui.monnaie_table.setItem(row, 1, QTableWidgetItem(myresult[row][2]))
            self.ui.monnaie_table.setItem(row, 2, QTableWidgetItem(str(myresult[row][3])))

    def rechercher_monnaie(self):
        sql = "SELECT * FROM monnaie WHERE nom LIKE '{}%'".format(self.ui.rechercher_monnaie.text())
        self.display_table(sql)

    def modifier_monnaie(self):
        self.selectedItems = self.ui.monnaie_table.selectedItems()
        if len(self.selectedItems) == 3:
            self.widget2.show()
            self.widget2.ui.code_monnaie.insert(self.selectedItems[0].text())
            self.widget2.ui.libelle_monnaie.insert(self.selectedItems[1].text())
            self.widget2.ui.taux_change.insert(self.selectedItems[2].text())

    def supprimer_monnaie(self):
        selectedItems = self.ui.monnaie_table.selectedItems()
        if len(selectedItems) >= 3:
            for i in range(0, len(selectedItems), 3):
                monnaie_id = int(self.ui.monnaie_table.verticalHeaderItem(selectedItems[i].row()).text())
                monnaie = Monnaie(monnaie_id)
                monnaie.supprimer()
                self.ui.monnaie_table.removeRow(selectedItems[i].row())

    def ajouter_ajout_monnaie(self):
        self.widget.show()
        code_monnaie = self.widget.ui.code_monnaie.text()
        libelle_monnaie = self.widget.ui.libelle_monnaie.text()
        taux_change = self.widget.ui.taux_change.text()
        monnaie1 = Monnaie(0)
        monnaie_id = monnaie1.inserer(code_monnaie, libelle_monnaie, taux_change)

        # clear line edits after inserting
        self.widget.ui.code_monnaie.clear()
        self.widget.ui.libelle_monnaie.clear()
        self.widget.ui.taux_change.clear()

        # displaying the added row
        availableRow = self.ui.monnaie_table.rowCount()
        self.ui.monnaie_table.insertRow(availableRow)
        self.ui.monnaie_table.setVerticalHeaderItem(availableRow, QTableWidgetItem(str(monnaie_id)))
        self.ui.monnaie_table.setItem(availableRow, 0, QTableWidgetItem(code_monnaie))
        self.ui.monnaie_table.setItem(availableRow, 1, QTableWidgetItem(libelle_monnaie))
        self.ui.monnaie_table.setItem(availableRow, 2, QTableWidgetItem(taux_change))

        self.widget.close()

    def fermer_ajout_monnaie(self):
        self.widget.ui.code_monnaie.clear()
        self.widget.ui.libelle_monnaie.clear()
        self.widget.ui.taux_change.clear()
        self.widget.close()

    def enregistrer_modifier_monnaie(self):
        current_monnaie_id = int(self.ui.monnaie_table.verticalHeaderItem(self.selectedItems[0].row()).text())
        monnaie = Monnaie(current_monnaie_id)
        monnaie.modifier(self.widget2.ui.code_monnaie.text(), self.widget2.ui.libelle_monnaie.text(), self.widget2.ui.taux_change.text())
        # update displayed table
        self.selectedItems[0].setText(self.widget2.ui.code_monnaie.text())
        self.selectedItems[1].setText(self.widget2.ui.libelle_monnaie.text())
        self.selectedItems[2].setText(self.widget2.ui.taux_change.text())

        # clear line edits after modifying
        self.widget2.ui.code_monnaie.clear()
        self.widget2.ui.libelle_monnaie.clear()
        self.widget2.ui.taux_change.clear()
        self.widget2.close()

    def fermer_modifier_monnaie(self):
        self.widget2.ui.code_monnaie.clear()
        self.widget2.ui.libelle_monnaie.clear()
        self.widget2.ui.taux_change.clear()
        self.widget2.close()

if __name__ == "__main__" :
    app = QApplication()
    widget = MonnaieWindow()
    widget.show()
    app.exec()

