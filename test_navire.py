from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_navire import Ui_Form as Navire_form
from ui_ajout_navire import Ui_Form as Ajout_navire_form
from ui_modifier_navire import Ui_Form as Modifier_navire_form

from class_multiobjet import *

class AjoutNavireWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ajout_navire_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.navire.clear()
        self.ui.description.clear()
        super(AjoutNavireWindow, self).closeEvent(event)

class ModifierNavireWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Modifier_navire_form()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.ui.navire.clear()
        self.ui.description.clear()
        super(ModifierNavireWindow, self).closeEvent(event)

class NavireWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Navire_form()
        self.ui.setupUi(self)
        self.display_table("SELECT * FROM navire")
        self.selectedItems = None

        #related_widgets
        self.widget = AjoutNavireWindow()
        self.widget2 = ModifierNavireWindow()

        #push_button_connections
        self.ui.rechercher_navire.textChanged.connect(self.rechercher_navire)
        self.ui.nouveau_navire.clicked.connect(self.widget.show)
        self.ui.modifier_navire.clicked.connect(self.modifier_navire)
        self.ui.supprimer_navire.clicked.connect(self.supprimer_navire)
        self.ui.fermer_navire.clicked.connect(self.close)

        #externel_push_button_connections
        self.widget.ui.ajouter_ajout_navire.clicked.connect(self.ajouter_ajout_navire)
        self.widget.ui.fermer_ajout_navire.clicked.connect(self.fermer_ajouter_navire)
        self.widget2.ui.enregistrer_modifier_navire.clicked.connect(self.enregistrer_modifier_navire)
        self.widget2.ui.fermer_modifier_navire.clicked.connect(self.fermer_modifier_navire)

    def display_table(self, sql):
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mydb.commit()
        row_count = len(myresult)
        self.ui.navire_table.setRowCount(row_count)
        for row in range(row_count):
            self.ui.navire_table.setVerticalHeaderItem(row,QTableWidgetItem(str(myresult[row][0])))
            self.ui.navire_table.setItem(row, 0, QTableWidgetItem(myresult[row][2]))
            self.ui.navire_table.setItem(row, 1, QTableWidgetItem(MultiObjet.getDescription(myresult[row][1])))

    def rechercher_navire(self):
        sql = "SELECT * FROM navire WHERE nom LIKE '{}%'".format(self.ui.rechercher_navire.text())
        self.display_table(sql)

    def modifier_navire(self):
        self.selectedItems = self.ui.navire_table.selectedItems()
        if len(self.selectedItems) == 2:
            self.widget2.show()
            self.widget2.ui.navire.insert(self.selectedItems[0].text())
            self.widget2.ui.description.insertPlainText(self.selectedItems[1].text())

    def supprimer_navire(self):
        selectedItems = self.ui.navire_table.selectedItems()
        if len(selectedItems) >= 2:
            for i in range(0, len(selectedItems), 2):
                id = int(self.ui.navire_table.verticalHeaderItem(selectedItems[i].row()).text())
                nv = Navire(id, Navire.getMultiObjetId(id))
                nv.supprimer()
                self.ui.navire_table.removeRow(selectedItems[i].row())

    def ajouter_ajout_navire(self):
        self.widget.show()
        navire = self.widget.ui.navire.text()
        description = self.widget.ui.description.toPlainText()
        nav = Navire(0, 0)
        navire_id = nav.inserer(navire, description)
        # clear line edits after inserting
        self.widget.ui.navire.clear()
        self.widget.ui.description.clear()
        # displaying the added row
        availableRow = self.ui.navire_table.rowCount()
        self.ui.navire_table.insertRow(availableRow)
        self.ui.navire_table.setVerticalHeaderItem(availableRow, QTableWidgetItem(str(navire_id)))
        self.ui.navire_table.setItem(availableRow, 0, QTableWidgetItem(navire))
        self.ui.navire_table.setItem(availableRow, 1, QTableWidgetItem(description))
        self.widget.close()

    def fermer_ajouter_navire(self):
        self.widget.ui.navire.clear()
        self.widget.ui.description.clear()
        self.widget.close()

    def enregistrer_modifier_navire(self):
        current_navire_id = int(self.ui.navire_table.verticalHeaderItem(self.selectedItems[0].row()).text())
        nav = Navire(current_navire_id, Navire.getMultiObjetId(current_navire_id))
        nav.modifier(self.widget2.ui.navire.text(), self.widget2.ui.description.toPlainText())
        # update displayed table
        self.selectedItems[0].setText(self.widget2.ui.navire.text())
        self.selectedItems[1].setText(self.widget2.ui.description.toPlainText())
        # clear line edits after modifying
        self.widget2.ui.navire.clear()
        self.widget2.ui.description.clear()
        self.widget2.close()

    def fermer_modifier_navire(self):
        self.widget2.ui.navire.clear()
        self.widget2.ui.description.clear()
        self.widget2.close()
#todo : add a tooltip to descriptions cz it's not showed completly
if __name__ == "__main__" :
    app = QApplication()
    widget = NavireWindow()
    widget.show()
    app.exec_()