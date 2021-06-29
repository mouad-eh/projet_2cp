from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_bon_sortie import Ui_Form as Sortie_form
from ui_ajout_bon_sortie import Ui_Form as Ajout_bon_sortie_form
from ui_modifier_bon_sortie import Ui_Form as Modifier_bon_sortie_form

from bon import *

class AjouterSortieWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ajout_bon_sortie_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.declarant.clear()
        self.ui.num_dossier.clear()
        self.ui.date.clear()
        self.ui.agent.clear()
        self.ui.transit.clear()
        super(AjouterSortieWindow, self).closeEvent(event)

class ModifierSortieWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Modifier_bon_sortie_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.declarant.clear()
        self.ui.num_dossier.clear()
        self.ui.date.clear()
        self.ui.agent.clear()
        self.ui.transit.clear()
        super(ModifierSortieWindow, self).closeEvent(event)

class SortieWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Sortie_form()
        self.ui.setupUi(self)
        self.display_table("SELECT * FROM bon WHERE bon_id IN (SELECT bon_id FROM bon_sortie)")
        self.selectedItems = None

        #related_widgets
        self.widget = AjouterSortieWindow()
        self.widget2 = ModifierSortieWindow()

        #push_button_connections
        self.ui.rechercher_bon_sortie.textChanged.connect(self.rechercher_bon_sortie)
        self.ui.nouveau_bon_sortie.clicked.connect(self.widget.show)
        self.ui.modifier_bon_sortie.clicked.connect(self.modifier_bon_sortie)
        self.ui.supprimer_bon_sortie.clicked.connect(self.supprimer_bon_sortie)
        self.ui.fermer_bon_sortie.clicked.connect(self.close)

        #externel_push_button_connections
        self.widget.ui.valider_ajout_bon_sortie.clicked.connect(self.ajouter_ajout_bon_sortie)
        self.widget.ui.fermer_ajout_bon_sortie.clicked.connect(self.fermer_ajout_bon_sortie)
        self.widget2.ui.valider_modifier_bon_sortie.clicked.connect(self.enregistrer_modifier_bon_sortie)
        self.widget2.ui.fermer_modifier_bon_sortie.clicked.connect(self.fermer_modifier_bon_sortie)

    def display_table(self, sql):
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.commit()
        row_count = len(myresult)
        self.ui.bon_sortie_table.setRowCount(row_count)
        for row in range(row_count):
            self.ui.bon_sortie_table.setVerticalHeaderItem(row,QTableWidgetItem(str(myresult[row][0])))
            self.ui.bon_sortie_table.setItem(row, 0, QTableWidgetItem(myresult[row][1]))
            self.ui.bon_sortie_table.setItem(row, 1, QTableWidgetItem(str(myresult[row][2])))
            self.ui.bon_sortie_table.setItem(row, 2, QTableWidgetItem(str(myresult[row][3])))
            self.ui.bon_sortie_table.setItem(row, 3, QTableWidgetItem(myresult[row][4]))
            self.ui.bon_sortie_table.setItem(row, 4, QTableWidgetItem(myresult[row][5]))

    def rechercher_bon_sortie(self):
        sql = "SELECT * FROM bon WHERE num_dossier LIKE '{}%'".format(self.ui.rechercher_bon_sortie.text())
        self.display_table(sql)

    def modifier_bon_sortie(self):
        self.selectedItems = self.ui.bon_sortie_table.selectedItems()
        if len(self.selectedItems) == 5:
            self.widget2.show()
            self.widget2.ui.declarant.insert(self.selectedItems[0].text())
            self.widget2.ui.num_dossier.insert(self.selectedItems[1].text())
            self.widget2.ui.date.insert(self.selectedItems[2].text())
            self.widget2.ui.agent.insert(self.selectedItems[3].text())
            self.widget2.ui.transit.insert(self.selectedItems[4].text())

    def supprimer_bon_sortie(self):
        selectedItems = self.ui.bon_sortie_table.selectedItems()
        if len(selectedItems) >= 5:
            for i in range(0, len(selectedItems), 5):
                id = int(self.ui.bon_sortie_table.verticalHeaderItem(selectedItems[i].row()).text())
                bon = Bon_sortie(id, Bon_sortie.getBonId(id))
                bon.supprimer()
                self.ui.bon_sortie_table.removeRow(selectedItems[i].row())

    def ajouter_ajout_bon_sortie(self):
        self.widget.show()
        declarant = self.widget.ui.declarant.text()
        num_dossier = self.widget.ui.num_dossier.text()
        date = self.widget.ui.date.text()
        agent = self.widget.ui.agent.text()
        transit = self.widget.ui.transit.text()
        bon = Bon_sortie(0, 0)
        bon_sortie_id = bon.inserer(declarant, num_dossier, date, agent, transit)

        # clear line edits after inserting
        self.widget.ui.declarant.clear()
        self.widget.ui.num_dossier.clear()
        self.widget.ui.date.clear()
        self.widget.ui.agent.clear()
        self.widget.ui.transit.clear()


        # displaying the added row
        availableRow = self.ui.bon_sortie_table.rowCount()
        self.ui.bon_sortie_table.insertRow(availableRow)
        self.ui.bon_sortie_table.setVerticalHeaderItem(availableRow, QTableWidgetItem(str(bon_sortie_id)))
        self.ui.bon_sortie_table.setItem(availableRow, 0, QTableWidgetItem(declarant))
        self.ui.bon_sortie_table.setItem(availableRow, 1, QTableWidgetItem(num_dossier))
        self.ui.bon_sortie_table.setItem(availableRow, 2, QTableWidgetItem(date))
        self.ui.bon_sortie_table.setItem(availableRow, 3, QTableWidgetItem(agent))
        self.ui.bon_sortie_table.setItem(availableRow, 4, QTableWidgetItem(transit))

        self.widget.close()

    def fermer_ajout_bon_sortie(self):
        self.widget.ui.declarant.clear()
        self.widget.ui.num_dossier.clear()
        self.widget.ui.date.clear()
        self.widget.ui.agent.clear()
        self.widget.ui.transit.clear()

        self.widget.close()

    def enregistrer_modifier_bon_sortie(self):
        current_bon_sortie_id = int(self.ui.bon_sortie_table.verticalHeaderItem(self.selectedItems[0].row()).text())
        bon = Bon_sortie(current_bon_sortie_id, Bon_sortie.getBonId(current_bon_sortie_id))
        bon.modifier(self.widget2.ui.declarant.text(), self.widget2.ui.num_dossier.text(), self.widget2.ui.date.text(), self.widget2.ui.agent.text(), self.widget2.ui.transit.text())
        # update displayed table
        self.selectedItems[0].setText(self.widget2.ui.declarant.text())
        self.selectedItems[1].setText(self.widget2.ui.num_dossier.text())
        self.selectedItems[2].setText(self.widget2.ui.date.text())
        self.selectedItems[3].setText(self.widget2.ui.agent.text())
        self.selectedItems[4].setText(self.widget2.ui.transit.text())

        # clear line edits after modifying
        self.widget2.ui.declarant.clear()
        self.widget2.ui.num_dossier.clear()
        self.widget2.ui.date.clear()
        self.widget2.ui.agent.clear()
        self.widget2.ui.transit.clear()

        self.widget2.close()

    def fermer_modifier_bon_sortie(self):
        self.widget2.ui.declarant.clear()
        self.widget2.ui.num_dossier.clear()
        self.widget2.ui.date.clear()
        self.widget2.ui.agent.clear()
        self.widget2.ui.transit.clear()

        self.widget2.close()

if __name__ == "__main__" :
    app = QApplication()
    widget = SortieWindow()
    widget.show()
    app.exec()

