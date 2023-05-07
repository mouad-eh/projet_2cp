from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from auto_ui.ui_pays2 import Ui_Form as Pays_form
from auto_ui.ui_ajout_pays import Ui_Form as Ajout_pays_form
from auto_ui.ui_modifier_pays import Ui_Form as Modifier_pays_form

from classes.class_paysmonnaie import *

class AjoutPaysWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ajout_pays_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.code_pays.clear()
        self.ui.libelle.clear()
        super(AjoutPaysWindow, self).closeEvent(event)

class ModifierPaysWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Modifier_pays_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.code_pays.clear()
        self.ui.libelle.clear()
        super(ModifierPaysWindow, self).closeEvent(event)

class PaysWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Pays_form()
        self.ui.setupUi(self)
        self.display_table("SELECT * FROM pays")
        self.selectedItems = None

        #related_widgets
        self.widget = AjoutPaysWindow()
        self.widget2 = ModifierPaysWindow()

        #push_button_connections
        self.ui.code.textChanged.connect(self.rechercher_pays_code)
        self.ui.libelle.textChanged.connect(self.rechercher_pays_libelle)

        self.ui.nouveau_pays.clicked.connect(self.widget.show)
        self.ui.modifier_pays.clicked.connect(self.modifier_pays)
        self.ui.supprimer_pays.clicked.connect(self.supprimer_pays)
        self.ui.fermer_pays.clicked.connect(self.close)
        self.ui.valider.clicked.connect(self.valider_pays)

        #externel_push_button_connections
        self.widget.ui.ajouter_ajout_pays.clicked.connect(self.ajouter_ajout_pays)
        self.widget.ui.fermer_ajout_pays.clicked.connect(self.fermer_ajout_pays)
        self.widget2.ui.enregistrer_modifier_pays.clicked.connect(self.enregistrer_modifier_pays)
        self.widget2.ui.fermer_modifier_pays.clicked.connect(self.fermer_modifier_pays)

    def display_table(self, sql):
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.commit()
        row_count = len(myresult)
        self.ui.pays_table.setRowCount(row_count)
        for row in range(row_count):
            self.ui.pays_table.setVerticalHeaderItem(row,QTableWidgetItem(str(myresult[row][0])))
            self.ui.pays_table.setItem(row, 0, QTableWidgetItem(str(myresult[row][1])))
            self.ui.pays_table.setItem(row, 1, QTableWidgetItem(myresult[row][2]))

    def rechercher_pays_code(self):
        sql = "SELECT * FROM pays WHERE code_pays LIKE '{}%'".format(self.ui.code.text())
        self.display_table(sql)

    def rechercher_pays_libelle(self):
        sql = "SELECT * FROM pays WHERE libelle LIKE '{}%'".format(self.ui.libelle.text())
        self.display_table(sql)


    def modifier_pays(self):
        self.selectedItems = self.ui.pays_table.selectedItems()
        if len(self.selectedItems) == 2:
            self.widget2.show()
            self.widget2.ui.code_pays.insert(self.selectedItems[0].text())
            self.widget2.ui.libelle.insertPlainText(self.selectedItems[1].text())
    def valider_pays(self):
        selectedItems = self.ui.pays_table.selectedItems()
        print(self.ui.pays_table.item(self.ui.pays_table.currentRow().numerator,0).text())

        if len(selectedItems) == 2:
          self.rowpays = (self.ui.pays_table.verticalHeaderItem(selectedItems[0].row()).text(),self.ui.pays_table.item(self.ui.pays_table.currentRow().numerator,1).text())
        print(self.rowpays)
        self.close()
    def supprimer_pays(self):
        selectedItems = self.ui.pays_table.selectedItems()
        if len(selectedItems) >= 2:
            for i in range(0, len(selectedItems), 2):
                pays_id = int(self.ui.pays_table.verticalHeaderItem(selectedItems[i].row()).text())
                pays = Pays(pays_id)                
                pays.supprimer()
                self.ui.pays_table.removeRow(selectedItems[i].row())

    def ajouter_ajout_pays(self):
        self.widget.show()
        code_pays = self.widget.ui.code_pays.text()
        libelle = self.widget.ui.libelle.toPlainText()
        pays = Pays(0)
        pays_id = pays.inserer(code_pays, libelle)
        
        # clear line edits after inserting
        self.widget.ui.code_pays.clear()
        self.widget.ui.libelle.clear()
        
        # displaying the added row
        availableRow = self.ui.pays_table.rowCount()
        self.ui.pays_table.insertRow(availableRow)
        self.ui.pays_table.setVerticalHeaderItem(availableRow, QTableWidgetItem(str(pays_id)))
        self.ui.pays_table.setItem(availableRow, 0, QTableWidgetItem(code_pays))
        self.ui.pays_table.setItem(availableRow, 1, QTableWidgetItem(libelle))
        self.widget.close()

    def fermer_ajout_pays(self):
        self.widget.ui.code_pays.clear()
        self.widget.ui.libelle.clear()
        self.widget.close()

    def enregistrer_modifier_pays(self):
        current_pays_id = int(self.ui.pays_table.verticalHeaderItem(self.selectedItems[0].row()).text())
        pays = Pays(current_pays_id)
        pays.modifier(self.widget2.ui.code_pays.text(), self.widget2.ui.libelle.toPlainText())
        
        # update displayed table
        self.selectedItems[0].setText(self.widget2.ui.code_pays.text())
        self.selectedItems[1].setText(self.widget2.ui.libelle.toPlainText())

        # clear line edits after modifying
        self.widget2.ui.code_pays.clear()
        self.widget2.ui.libelle.clear() 
        self.widget2.close()

    def fermer_modifier_pays(self):
        self.widget2.ui.code_pays.clear()
        self.widget2.ui.libelle.clear()
        self.widget2.close()

if __name__ == "__main__" :
    app = QApplication()
    widget = PaysWindow()
    widget.show()
    app.exec_()

