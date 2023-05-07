# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prestation_debrourGxWNJS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from auto_ui.ui_nv_prdb_debour import *
import mysql.connector
import sys
mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="rotage2015002",
   database="projet_beta"
)
mycursor = mydb.cursor()

class Ui_prestation_debours(object):
    def __init__(self,form):
        self.form = form
        self.setupUi(self.form)
        self.loaddata()
        self.nv = Ui_Form()

        self.valider.clicked.connect( self.valid)
        self.nouveau_prestation_debour.clicked.connect(self.new)
        self.supprimer_prestation_debour.clicked.connect(self.supp)
        self.fermer_prestation_debour.clicked.connect(self.fermer)
        #self.nouveau_prestation_debour.clicked.connect()

    def setupUi(self, Form):
            if not Form.objectName():
                Form.setObjectName(u"Form")
            Form.resize(760, 441)
            self.gridLayout = QGridLayout(Form)
            self.gridLayout.setObjectName(u"gridLayout")
            self.frame = QFrame(Form)
            self.frame.setObjectName(u"frame")
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.frame.setFrameShadow(QFrame.Raised)
            self.verticalLayout_2 = QVBoxLayout(self.frame)
            self.verticalLayout_2.setObjectName(u"verticalLayout_2")
            self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.frame_3 = QFrame(self.frame)
            self.frame_3.setObjectName(u"frame_3")
            self.frame_3.setStyleSheet(u"background-color: #2f3e40; /*#2f3e46,1a535c;1d3557;233d4d*/\n"
                                       "color: rgb(255, 255, 255);")
            self.frame_3.setFrameShape(QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QFrame.Raised)
            self.horizontalLayout = QHBoxLayout(self.frame_3)
            self.horizontalLayout.setObjectName(u"horizontalLayout")
            self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
            self.label_2 = QLabel(self.frame_3)
            self.label_2.setObjectName(u"label_2")
            font = QFont()
            font.setFamily(u"Segoe UI")
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet(u"background-color: #2f3e40; /*#2f3e46,1a535c;1d3557;233d4d*/\n"
                                       "color: rgb(255, 255, 255);")

            self.horizontalLayout.addWidget(self.label_2)

            self.horizontalSpacer = QSpacerItem(510, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.horizontalLayout.addItem(self.horizontalSpacer)

            self.verticalLayout_2.addWidget(self.frame_3)

            self.frame_4 = QFrame(self.frame)
            self.frame_4.setObjectName(u"frame_4")
            self.frame_4.setFrameShape(QFrame.StyledPanel)
            self.frame_4.setFrameShadow(QFrame.Raised)
            self.gridLayout_2 = QGridLayout(self.frame_4)
            self.gridLayout_2.setObjectName(u"gridLayout_2")
            self.verticalLayout = QVBoxLayout()
            self.verticalLayout.setObjectName(u"verticalLayout")
            self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

            self.verticalLayout.addItem(self.verticalSpacer)

            self.nouveau_prestation_debour = QPushButton(self.frame_4)
            self.nouveau_prestation_debour.setObjectName(u"nouveau_prestation_debour")
            self.nouveau_prestation_debour.setFont(font)
            self.nouveau_prestation_debour.setStyleSheet(u"QPushButton {width: 65px;\n"
                                                         "background-color: white;\n"
                                                         "border: 2px solid #3bb273;\n"
                                                         "color: #3bb273;\n"
                                                         "padding: 6px;\n"
                                                         "border-radius: 10px;}\n"
                                                         "\n"
                                                         "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                                         "QPushButton:pressed { margin: 1px; }\n"
                                                         "")

            self.verticalLayout.addWidget(self.nouveau_prestation_debour)

            self.valider = QPushButton(self.frame_4)
            self.valider.setObjectName(u"valider")
            self.valider.setFont(font)
            self.valider.setStyleSheet(u"QPushButton {width: 65px;\n"
                                       "background-color: white;\n"
                                       "border: 2px solid #3bb273;\n"
                                       "color: #3bb273;\n"
                                       "padding: 6px;\n"
                                       "border-radius: 10px;}\n"
                                       "\n"
                                       "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                       "QPushButton:pressed { margin: 1px; }\n"
                                       "")

            self.verticalLayout.addWidget(self.valider)

            self.modifier_prestation_debour = QPushButton(self.frame_4)
            self.modifier_prestation_debour.setObjectName(u"modifier_prestation_debour")
            self.modifier_prestation_debour.setFont(font)
            self.modifier_prestation_debour.setStyleSheet(u"QPushButton {width: 65px;\n"
                                                          "background-color: white;\n"
                                                          "border: 2px solid #3bb273;\n"
                                                          "color: #3bb273;\n"
                                                          "padding: 6px;\n"
                                                          "border-radius: 10px;}\n"
                                                          "\n"
                                                          "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                                          "QPushButton:pressed { margin: 1px; }\n"
                                                          "")

            self.verticalLayout.addWidget(self.modifier_prestation_debour)

            self.supprimer_prestation_debour = QPushButton(self.frame_4)
            self.supprimer_prestation_debour.setObjectName(u"supprimer_prestation_debour")
            self.supprimer_prestation_debour.setFont(font)
            self.supprimer_prestation_debour.setStyleSheet(u"QPushButton {background-color: white;\n"
                                                           "border: 2px solid #ee2e31;\n"
                                                           "color: #ee2e31;\n"
                                                           "padding: 5px;\n"
                                                           "border-radius: 10px;}\n"
                                                           "QPushButton:hover {\n"
                                                           "background-color: #ee2e31;\n"
                                                           "color: white;\n"
                                                           "}\n"
                                                           "QPushButton:pressed{\n"
                                                           "margin: 1px;\n"
                                                           "}\n"
                                                           "/*#ee2e31*/\n"
                                                           "")

            self.verticalLayout.addWidget(self.supprimer_prestation_debour)

            self.fermer_prestation_debour = QPushButton(self.frame_4)
            self.fermer_prestation_debour.setObjectName(u"fermer_prestation_debour")
            self.fermer_prestation_debour.setFont(font)
            self.fermer_prestation_debour.setStyleSheet(u"QPushButton {background-color: white;\n"
                                                        "border: 2px solid #ee2e31;\n"
                                                        "color: #ee2e31;\n"
                                                        "padding: 5px;\n"
                                                        "border-radius: 10px;}\n"
                                                        "QPushButton:hover {\n"
                                                        "background-color: #ee2e31;\n"
                                                        "color: white;\n"
                                                        "}\n"
                                                        "QPushButton:pressed{\n"
                                                        "margin: 1px;\n"
                                                        "}\n"
                                                        "/*#ee2e31*/\n"
                                                        "")

            self.verticalLayout.addWidget(self.fermer_prestation_debour)

            self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

            self.verticalLayout.addItem(self.verticalSpacer_2)

            self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)

            self.table_restation_debour = QTableWidget(self.frame_4)
            if (self.table_restation_debour.columnCount() < 2):
                self.table_restation_debour.setColumnCount(2)
            __qtablewidgetitem = QTableWidgetItem()
            self.table_restation_debour.setHorizontalHeaderItem(0, __qtablewidgetitem)
            __qtablewidgetitem1 = QTableWidgetItem()
            self.table_restation_debour.setHorizontalHeaderItem(1, __qtablewidgetitem1)
            self.table_restation_debour.setObjectName(u"table_restation_debour")
            self.table_restation_debour.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.table_restation_debour.horizontalHeader().setDefaultSectionSize(285)

            self.gridLayout_2.addWidget(self.table_restation_debour, 0, 0, 1, 1)

            self.verticalLayout_2.addWidget(self.frame_4)

            self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

            self.retranslateUi(Form)

            QMetaObject.connectSlotsByName(Form)

        # setupUi

    def retranslateUi(self, Form):
            Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
            self.label_2.setText(QCoreApplication.translate("Form", u"Prestation/Debour", None))
            self.nouveau_prestation_debour.setText(QCoreApplication.translate("Form", u"Nouveau", None))
            self.valider.setText(QCoreApplication.translate("Form", u"valider", None))
            self.modifier_prestation_debour.setText(QCoreApplication.translate("Form", u"Modifier", None))
            self.supprimer_prestation_debour.setText(QCoreApplication.translate("Form", u"Supprimer", None))
            self.fermer_prestation_debour.setText(QCoreApplication.translate("Form", u"Fermer", None))
            ___qtablewidgetitem = self.table_restation_debour.horizontalHeaderItem(0)
            ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Prestation / Debour ", None));
            ___qtablewidgetitem1 = self.table_restation_debour.horizontalHeaderItem(1)
            ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Type", None));
        # retranslateUi

    def loaddata(self):
        sql = "SELECT * FROM prestation_debours"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        tablerow = 0
        self.ids = []
        self.table_restation_debour.setRowCount(mycursor.rowcount)
        for row in myresult:
            self.ids.append(row[0])
            self.table_restation_debour.setItem(tablerow,0,QTableWidgetItem(row[1]))
            print(row[2])
            if (row[2] == '0'):
              self.table_restation_debour.setItem(tablerow,1,QTableWidgetItem('prestation'))
            else:
              self.table_restation_debour.setItem(tablerow, 1, QTableWidgetItem('debours'))

            tablerow += 1
    def valid(self):
        self.id_selected = self.table_restation_debour.currentRow().numerator
        print(self.table_restation_debour.item(self.id_selected,1).text())
        self.value = (self.table_restation_debour.item(self.id_selected,0).text(),self.table_restation_debour.item(self.id_selected,1).text())
        self.form.close()


    def supp(self):
        id = self.ids[self.table_restation_debour.currentRow().numerator]
        sql = "DELETE FROM prestation_debours WHERE debours_prestation_id = "
        sql += str(id)
        mycursor.execute(sql)
        mydb.commit()
        self.loaddata()
    def fermer(self):
        self.form.close()
    def new(self):
        self.nv.form.show()
        self.nv.valider.clicked.connect(self.loaddata)


if __name__ == "__main__":
    app = QApplication()
    form=QWidget()
    widget = Ui_prestation_debours(form)
    form.show()
    app.exec_()