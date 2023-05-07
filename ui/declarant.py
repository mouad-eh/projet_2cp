from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from auto_ui.ui_declarant import Ui_Form as Declarant_form
from auto_ui.ui_ajouter_declarant import Ui_Form as Ajout_declarant_form
from auto_ui.ui_modifier_declarant  import Ui_Form as Modifier_declarant_form

from classes.personne import *

class AjouterDeclarantWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ajout_declarant_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.nom.clear()
        self.ui.prenom.clear()
        self.ui.tel.clear()
        self.ui.email.clear()
        self.ui.adresse.clear()
        super(AjouterDeclarantWindow, self).closeEvent(event)

class ModifierDeclarantWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Modifier_declarant_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.nom.clear()
        self.ui.prenom.clear()
        self.ui.tel.clear()
        self.ui.email.clear()
        self.ui.adresse.clear()
        super(ModifierDeclarantWindow, self).closeEvent(event)

class DeclarantWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Declarant_form()
        self.ui.setupUi(self)
        self.display_table("SELECT * FROM personne WHERE id IN (SELECT personne_id FROM declarant)")
        self.selectedItems = None

        #related_widgets
        self.widget = AjouterDeclarantWindow()
        self.widget2 = ModifierDeclarantWindow()

        #push_button_connections
        self.ui.rechercher_declarant.textChanged.connect(self.rechercher_declarant)
        self.ui.nouveau_declarant.clicked.connect(self.widget.show)
        self.ui.modifier_declarant.clicked.connect(self.modifier_declarant)
        self.ui.supprimer_declarant.clicked.connect(self.supprimer_declarant)
        self.ui.fermer_declarant.clicked.connect(self.close)
        self.ui.valider.clicked.connect(self.valider_declarant)
        #externel_push_button_connections
        self.widget.ui.valider_declarant.clicked.connect(self.ajouter_ajout_declarant)
        self.widget.ui.fermer_declarant.clicked.connect(self.fermer_ajout_declarant)
        self.widget2.ui.valider_declarant.clicked.connect(self.enregistrer_modifier_declarant)
        self.widget2.ui.fermer_declarant.clicked.connect(self.fermer_modifier_declarant)

    def display_table(self, sql):
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.commit()
        row_count = len(myresult)
        self.ui.declarant_table.setRowCount(row_count)
        for row in range(row_count):
            self.ui.declarant_table.setVerticalHeaderItem(row,QTableWidgetItem(str(myresult[row][0])))
            self.ui.declarant_table.setItem(row, 0, QTableWidgetItem(myresult[row][1]))
            self.ui.declarant_table.setItem(row, 1, QTableWidgetItem(myresult[row][2]))
            self.ui.declarant_table.setItem(row, 2, QTableWidgetItem(myresult[row][3]))
            self.ui.declarant_table.setItem(row, 3, QTableWidgetItem(myresult[row][4]))
            self.ui.declarant_table.setItem(row, 4, QTableWidgetItem(myresult[row][5]))

    def rechercher_declarant(self):
        sql = "SELECT * FROM personne WHERE nom LIKE '{}%'".format(self.ui.rechercher_declarant.text())
        self.display_table(sql)

    def modifier_declarant(self):
        self.selectedItems = self.ui.declarant_table.selectedItems()
        if len(self.selectedItems) == 5:
            self.widget2.show()
            self.widget2.ui.nom.insert(self.selectedItems[0].text())
            self.widget2.ui.prenom.insert(self.selectedItems[1].text())
            self.widget2.ui.tel.insert(self.selectedItems[2].text())
            self.widget2.ui.email.insert(self.selectedItems[3].text())
            self.widget2.ui.adresse.insert(self.selectedItems[4].text())
    def valider_declarant(self):
        selectedItems = self.ui.declarant_table.selectedItems()
        print(self.ui.declarant_table.item(self.ui.declarant_table.currentRow().numerator,0).text())

        if len(selectedItems) == 5:
         self.rowdeclarant = (self.ui.declarant_table.verticalHeaderItem(selectedItems[0].row()).text(),self.ui.declarant_table.item(self.ui.declarant_table.currentRow().numerator,0).text(),self.ui.declarant_table.item(self.ui.declarant_table.currentRow().numerator,1).text())
        self.close()
    def supprimer_declarant(self):
        selectedItems = self.ui.declarant_table.selectedItems()
        if len(selectedItems) >= 5:
            for i in range(0, len(selectedItems), 5):
                id = int(self.ui.declarant_table.verticalHeaderItem(selectedItems[i].row()).text())
                personne = Declarant(id, Declarant.getPersonneId(id))
                personne.supprimer()
                self.ui.declarant_table.removeRow(selectedItems[i].row())

    def ajouter_ajout_declarant(self):
        self.widget.show()
        nom = self.widget.ui.nom.text()
        prenom = self.widget.ui.prenom.text()
        tel = self.widget.ui.tel.text()
        email = self.widget.ui.email.text()
        adresse = self.widget.ui.adresse.text()
        personne = Declarant(0, 0)
        declarant_id = personne.inserer(nom, prenom, tel, email, adresse)

        # clear line edits after inserting
        self.widget.ui.nom.clear()
        self.widget.ui.prenom.clear()
        self.widget.ui.tel.clear()
        self.widget.ui.email.clear()
        self.widget.ui.adresse.clear()


        # displaying the added row
        availableRow = self.ui.declarant_table.rowCount()
        self.ui.declarant_table.insertRow(availableRow)
        self.ui.declarant_table.setVerticalHeaderItem(availableRow, QTableWidgetItem(str(declarant_id)))
        self.ui.declarant_table.setItem(availableRow, 0, QTableWidgetItem(nom))
        self.ui.declarant_table.setItem(availableRow, 1, QTableWidgetItem(prenom))
        self.ui.declarant_table.setItem(availableRow, 2, QTableWidgetItem(tel))
        self.ui.declarant_table.setItem(availableRow, 3, QTableWidgetItem(email))
        self.ui.declarant_table.setItem(availableRow, 4, QTableWidgetItem(adresse))

        self.widget.close()

    def fermer_ajout_declarant(self):
        self.widget.ui.nom.clear()
        self.widget.ui.prenom.clear()
        self.widget.ui.tel.clear()
        self.widget.ui.email.clear()
        self.widget.ui.adresse.clear()

        self.widget.close()

    def enregistrer_modifier_declarant(self):
        current_declarant_id = int(self.ui.declarant_table.verticalHeaderItem(self.selectedItems[0].row()).text())
        personne = Declarant(current_declarant_id, Declarant.getPersonneId(current_declarant_id))
        personne.modifier(self.widget2.ui.nom.text(), self.widget2.ui.prenom.text(), self.widget2.ui.tel.text(), self.widget2.ui.email.text(), self.widget2.ui.adresse.text())
        # update displayed table
        self.selectedItems[0].setText(self.widget2.ui.nom.text())
        self.selectedItems[1].setText(self.widget2.ui.prenom.text())
        self.selectedItems[2].setText(self.widget2.ui.tel.text())
        self.selectedItems[3].setText(self.widget2.ui.email.text())
        self.selectedItems[4].setText(self.widget2.ui.adresse.text())

        # clear line edits after modifying
        self.widget2.ui.nom.clear()
        self.widget2.ui.prenom.clear()
        self.widget2.ui.tel.clear()
        self.widget2.ui.email.clear()
        self.widget2.ui.adresse.clear()

        self.widget2.close()

    def fermer_modifier_declarant(self):
        self.widget2.ui.nom.clear()
        self.widget2.ui.prenom.clear()
        self.widget2.ui.tel.clear()
        self.widget2.ui.email.clear()
        self.widget2.ui.adresse.clear()

        self.widget2.close()

if __name__ == "__main__" :
    app = QApplication()
    widget = DeclarantWindow()
    widget.show()
    app.exec_()

