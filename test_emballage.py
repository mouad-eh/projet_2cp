import datetime

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_suivi_emballages import Ui_Form as Suivi_emballages_form
from ui_ajout_emballage import Ui_Form as Ajout_emballage_from
from ui_modifier_emballage import Ui_Form as Modifier_emballage_form

from multiobjet2 import *

def stringToDate(str):
    year, month, day = str.split("-")
    return datetime.date(int(year), int(month), int(day))

class AjoutEmballage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ajout_emballage_from()
        self.ui.setupUi(self)
        #todo : can be done from qt designer
        self.ui.date_livraison.setDisplayFormat("yyyy-MM-dd")
        self.ui.date_restitution.setDisplayFormat("yyyy-MM-dd")

        self.inputs = [self.ui.num, self.ui.num_emballage, self.ui.genre_emballage,
                  self.ui.pieds, self.ui.type_emballage, self.ui.date_livraison,
                  self.ui.date_restitution, self.ui.num_bon, self.ui.description]

    def closeEvent(self, event):
        for input in self.inputs:
            input.clear()
        super().closeEvent(event)

class ModifierEmballage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Modifier_emballage_form()
        self.ui.setupUi(self)
        #todo: can be done from qt designer
        self.ui.date_livraison.setDisplayFormat("yyyy-MM-dd")
        self.ui.date_restitution.setDisplayFormat("yyyy-MM-dd")

        self.inputs = [self.ui.num, self.ui.num_emballage, self.ui.genre_emballage,
                  self.ui.pieds, self.ui.type_emballage, self.ui.date_livraison,
                  self.ui.date_restitution, self.ui.num_bon, self.ui.description]

    def closeEvent(self, event):
        for input in self.inputs:
            input.clear()
        super().closeEvent(event)

class SuiviEmballagesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Suivi_emballages_form()
        self.ui.setupUi(self)
        self.display_table()
        # externel widgets
        self.widget = AjoutEmballage()
        self.widget2 = ModifierEmballage()

        self.selectedItems = None
        # buttons connections
        self.ui.nouveau.clicked.connect(self.widget.show)
        self.ui.modifier.clicked.connect(self.modifier_emballage)
        self.ui.supprimer.clicked.connect(self.supprimer_emballage)
        # externel buttons connections
        self.widget.ui.valider.clicked.connect(self.valider_ajout_emballage)
        self.widget.ui.annuler.clicked.connect(self.annuler_ajout_emballage)
        self.widget2.ui.valider.clicked.connect(self.valider_modifier_emballage)
        self.widget2.ui.annuler.clicked.connect(self.annuler_modifier_emballage)

    def display_table(self):
        sql = "SELECT * FROM emballage"
        # todo: i should get lines related to client_id and dossier_id only not all of them
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.commit()
        row_count = len(myresult)
        self.ui.emballage_table.setRowCount(row_count)
        for row in range(row_count):
            self.ui.emballage_table.setVerticalHeaderItem(row, QTableWidgetItem(str(myresult[row][0])))
            for i in range(3, 11):
                self.ui.emballage_table.setItem(row, i-3, QTableWidgetItem(str(myresult[row][i])))
            self.ui.emballage_table.setItem(row, 8, QTableWidgetItem(MultiObjet.getDescription(myresult[row][11])))


    def modifier_emballage(self):
        self.selectedItems = self.ui.emballage_table.selectedItems()
        if len(self.selectedItems) == 9:
            self.widget2.show()
            for i in range(9):
                if isinstance(self.widget2.inputs[i], QDateEdit):
                    self.widget2.inputs[i].setDate(stringToDate(self.selectedItems[i].text()))
                elif isinstance(self.widget2.inputs[i], QTextEdit):
                    self.widget2.inputs[i].insertPlainText(self.selectedItems[i].text())
                else:
                    self.widget2.inputs[i].insert(self.selectedItems[i].text())

    def supprimer_emballage(self):
        selectedItems = self.ui.emballage_table.selectedItems()
        if len(selectedItems) >= 9:
            for i in range(0, len(selectedItems), 9):
                id = int(self.ui.emballage_table.verticalHeaderItem(selectedItems[i].row()).text())
                emb = Emballage(id, None, None, Emballage.getMultiObjetId(id))
                emb.supprimer()
                self.ui.emballage_table.removeRow(selectedItems[i].row())

    def valider_ajout_emballage(self):
        emb = Emballage(0, None, None, 0)
        emballage_id = emb.inserer(int(self.widget.inputs[0].text()), self.widget.inputs[1].text(), self.widget.inputs[2].text(),
                                   self.widget.inputs[3].text(), self.widget.inputs[4].text(), self.widget.inputs[5].text(),
                                   self.widget.inputs[6].text(), self.widget.inputs[7].text(), self.widget.inputs[8].toPlainText())
        
        availableRow = self.ui.emballage_table.rowCount()
        self.ui.emballage_table.insertRow(availableRow)
        self.ui.emballage_table.setVerticalHeaderItem(availableRow, QTableWidgetItem(str(emballage_id)))
        for i in range(0, 8):
            # update items
            self.ui.emballage_table.setItem(availableRow, i, QTableWidgetItem(self.widget.inputs[i].text()))
            # clearing line edits after modifying
            self.widget.inputs[i].clear()
        self.ui.emballage_table.setItem(availableRow, 8, QTableWidgetItem(self.widget.inputs[8].toPlainText()))
        self.widget.inputs[8].clear()

    def annuler_ajout_emballage(self):
        for i in range(9):
            self.widget.inputs[i].clear()
        self.widget.close()

    def valider_modifier_emballage(self):
        current_emballage_id = int(self.ui.emballage_table.verticalHeaderItem(self.selectedItems[0].row()).text())
        emb = Emballage(current_emballage_id, None, None, Emballage.getMultiObjetId(current_emballage_id))
        emb.modifier(self.widget2.inputs[0].text(), self.widget2.inputs[1].text(), self.widget2.inputs[2].text(),
                     self.widget2.inputs[3].text(), self.widget2.inputs[4].text(), self.widget2.inputs[5].text(),
                     self.widget2.inputs[6].text(), self.widget2.inputs[7].text(), self.widget2.inputs[8].toPlainText())

        # update displayed table
        for i in range(8):
            self.selectedItems[i].setText(self.widget2.inputs[i].text())
        self.selectedItems[8].setText(self.widget2.inputs[8].toPlainText())
        # clear line edits after modifying
        for i in range(9):
            self.widget2.inputs[i].clear()

    def annuler_modifier_emballage(self):
        for i in range(9):
            self.widget2.inputs[i].clear()
        self.widget2.close()

if __name__ == "__main__":
    app = QApplication()
    widget = SuiviEmballagesWindow()
    widget.show()
    app.exec_()
