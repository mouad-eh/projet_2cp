# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dossier_kamyl(1)anbxxR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import mysql.connector
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="rotage2015002",
   database="projet_beta"
)
mycursor = mydb.cursor()

class Ui_doss(object):
    def __init__(self):
        self.form = QWidget()
        self.setupUi(self.form)
        self.loaddata()
        self.valider.clicked.connect(self.valid)

    def setupUi(self, Form):
            if not Form.objectName():
                Form.setObjectName(u"Form")
            Form.resize(722, 427)
            self.verticalLayout_2 = QVBoxLayout(Form)
            self.verticalLayout_2.setObjectName(u"verticalLayout_2")
            self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.frame_2 = QFrame(Form)
            self.frame_2.setObjectName(u"frame_2")
            self.frame_2.setFrameShape(QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QFrame.Raised)
            self.verticalLayout_4 = QVBoxLayout(self.frame_2)
            self.verticalLayout_4.setObjectName(u"verticalLayout_4")
            self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.frame_3 = QFrame(self.frame_2)
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

            self.verticalLayout_4.addWidget(self.frame_3)

            self.frame = QFrame(self.frame_2)
            self.frame.setObjectName(u"frame")
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.frame.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_2 = QHBoxLayout(self.frame)
            self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
            self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.table_dossier = QTableWidget(self.frame)
            if (self.table_dossier.columnCount() < 3):
                self.table_dossier.setColumnCount(3)
            font1 = QFont()
            font1.setPointSize(8)
            __qtablewidgetitem = QTableWidgetItem()
            __qtablewidgetitem.setFont(font1);
            self.table_dossier.setHorizontalHeaderItem(0, __qtablewidgetitem)
            __qtablewidgetitem1 = QTableWidgetItem()
            self.table_dossier.setHorizontalHeaderItem(1, __qtablewidgetitem1)
            __qtablewidgetitem2 = QTableWidgetItem()
            self.table_dossier.setHorizontalHeaderItem(2, __qtablewidgetitem2)
            self.table_dossier.setObjectName(u"table_dossier")
            self.table_dossier.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.table_dossier.horizontalHeader().setCascadingSectionResizes(True)
            self.table_dossier.horizontalHeader().setDefaultSectionSize(250)

            self.horizontalLayout_2.addWidget(self.table_dossier)

            self.frame_6 = QFrame(self.frame)
            self.frame_6.setObjectName(u"frame_6")
            self.frame_6.setFrameShape(QFrame.StyledPanel)
            self.frame_6.setFrameShadow(QFrame.Raised)
            self.verticalLayout = QVBoxLayout(self.frame_6)
            self.verticalLayout.setObjectName(u"verticalLayout")

            self.horizontalLayout_2.addWidget(self.frame_6)

            self.verticalLayout_4.addWidget(self.frame)

            self.frame_5 = QFrame(self.frame_2)
            self.frame_5.setObjectName(u"frame_5")
            self.frame_5.setFrameShape(QFrame.StyledPanel)
            self.frame_5.setFrameShadow(QFrame.Raised)
            self.verticalLayout_3 = QVBoxLayout(self.frame_5)
            self.verticalLayout_3.setObjectName(u"verticalLayout_3")
            self.valider = QPushButton(self.frame_5)
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

            self.verticalLayout_3.addWidget(self.valider)

            self.fermer = QPushButton(self.frame_5)
            self.fermer.setObjectName(u"fermer")
            self.fermer.setFont(font)
            self.fermer.setStyleSheet(u"QPushButton {background-color: white;\n"
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

            self.verticalLayout_3.addWidget(self.fermer)

            self.frame_7 = QFrame(self.frame_5)
            self.frame_7.setObjectName(u"frame_7")
            self.frame_7.setFrameShape(QFrame.StyledPanel)
            self.frame_7.setFrameShadow(QFrame.Raised)

            self.verticalLayout_3.addWidget(self.frame_7)

            self.verticalLayout_4.addWidget(self.frame_5)

            self.verticalLayout_2.addWidget(self.frame_2)

            self.retranslateUi(Form)

            QMetaObject.connectSlotsByName(Form)

        # setupUi

    def retranslateUi(self, Form):
            Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
            self.label_2.setText(QCoreApplication.translate("Form", u"Dossier", None))
            ___qtablewidgetitem = self.table_dossier.horizontalHeaderItem(0)
            ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"num dossier", None));
            ___qtablewidgetitem1 = self.table_dossier.horizontalHeaderItem(1)
            ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"num facture", None));
            ___qtablewidgetitem2 = self.table_dossier.horizontalHeaderItem(2)
            ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"client", None));
            self.valider.setText(QCoreApplication.translate("Form", u"Valider", None))
            self.fermer.setText(QCoreApplication.translate("Form", u"Fermer", None))
        # retranslateUi
    def loaddata(self):
        sql = "SELECT dossier_id,client_id,num_facture,montant_droits_taxes FROM dossier"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        tablerow = 0
        self.mtns = []
        self.table_dossier.setRowCount(len(myresult))
        for row in myresult:
          sql = "SELECT * FROM facture WHERE num_facture="
          sql +=str(row[2])
          mycursor.execute(sql)
          myresult = mycursor.fetchall()
          print(myresult)
          if ( myresult == []):
            self.mtns.append(row[3])
            self.table_dossier.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.table_dossier.setItem(tablerow, 1, QTableWidgetItem(str(row[2])))
            sql = "SELECT entreprise_id FROM client WHERE client_id ="
            sql += str(row[1])
            mycursor.execute(sql)
            id = mycursor.fetchone()
            print(id[0])
            sql = "SELECT nom FROM entreprise WHERE entreprise_id ="
            sql += str(id[0])
            mycursor.execute(sql)
            id = mycursor.fetchone()
            self.table_dossier.setItem(tablerow, 2, QTableWidgetItem(id[0]))
            tablerow += 1
    def valid(self):
        self.id_selected = self.table_dossier.currentRow().numerator
        print(self.table_dossier.item(self.id_selected, 1).text())
        self.montant = self.mtns[self.table_dossier.currentRow().numerator]
        self.value = (self.table_dossier.item(self.id_selected, 0).text(),
                      self.table_dossier.item(self.id_selected, 1).text(),self.table_dossier.item(self.id_selected, 2).text())
        print(self.value)
        self.form.close()


if __name__ == "__main__":
    app = QApplication()
    widget = Ui_doss()
    widget.form.show()
    app.exec_()