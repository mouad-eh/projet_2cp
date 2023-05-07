# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'facturezMCGtJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from auto_ui.ajout_prestation_debour import *
from auto_ui.ui_doss import *
import shutil
import os
class Ui_Form(object):
    def __init__(self):
       self.form = QWidget()
       self.setupUi(self.form)
       self.nouveau_facture.clicked.connect(self.nouveau)
       self.montant.setText("0")
       self.fermer_facture.clicked.connect(self.close)
       self.uidossier = Ui_doss()
       self.num_dossier.clicked.connect(self.numdossier)
       self.uidossier.valider.clicked.connect(self.remplir)
       self.valider_facture.clicked.connect(self.valid)
       self.fermer_facture.clicked.connect(self.close)
       self.tab_db = []

    def setupUi(self, Form):
           if not Form.objectName():
               Form.setObjectName(u"Form")
           Form.resize(925, 511)
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

           self.frame_4 = QFrame(self.frame_2)
           self.frame_4.setObjectName(u"frame_4")
           self.frame_4.setStyleSheet(u"background-color:#DCDCDC	")
           self.frame_4.setFrameShape(QFrame.StyledPanel)
           self.frame_4.setFrameShadow(QFrame.Raised)
           self.gridLayout = QGridLayout(self.frame_4)
           self.gridLayout.setObjectName(u"gridLayout")
           self.num_de_declaration = QLineEdit(self.frame_4)
           self.num_de_declaration.setObjectName(u"num_de_declaration")
           self.num_de_declaration.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                                 "border-radius:10px;\n"
                                                 "padding: 3px;\n"
                                                 "background-color: white;\n"
                                                 "color: #2f3e46;\n"
                                                 "")
           self.num_de_declaration.setReadOnly(True)

           self.gridLayout.addWidget(self.num_de_declaration, 2, 1, 1, 1)

           self.label_7 = QLabel(self.frame_4)
           self.label_7.setObjectName(u"label_7")
           font1 = QFont()
           font1.setBold(True)
           font1.setWeight(75)
           self.label_7.setFont(font1)
           self.label_7.setStyleSheet(u"color: #2f3e46;")

           self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

           self.num_facture = QLineEdit(self.frame_4)
           self.num_facture.setObjectName(u"num_facture")
           self.num_facture.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"
                                          "color: #2f3e46;\n"
                                          "")
           self.num_facture.setReadOnly(True)

           self.gridLayout.addWidget(self.num_facture, 0, 1, 1, 2)

           self.label = QLabel(self.frame_4)
           self.label.setObjectName(u"label")
           self.label.setFont(font1)
           self.label.setStyleSheet(u"color: #2f3e46;")

           self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

           self.montant = QLineEdit(self.frame_4)
           self.montant.setObjectName(u"montant")
           self.montant.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                      "border-radius:10px;\n"
                                      "padding: 3px;\n"
                                      "background-color: white;\n"
                                      "color: #2f3e46;\n"
                                      "")
           self.montant.setReadOnly(True)

           self.gridLayout.addWidget(self.montant, 4, 9, 1, 1)

           self.line_numdossier = QLineEdit(self.frame_4)
           self.line_numdossier.setObjectName(u"line_numdossier")
           self.line_numdossier.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                              "border-radius:10px;\n"
                                              "padding: 3px;\n"
                                              "background-color: white;\n"
                                              "color: #2f3e46;\n"
                                              "")
           self.line_numdossier.setReadOnly(True)

           self.gridLayout.addWidget(self.line_numdossier, 0, 8, 1, 1)

           self.num_dossier = QPushButton(self.frame_4)
           self.num_dossier.setObjectName(u"num_dossier")
           self.num_dossier.setFont(font)
           self.num_dossier.setStyleSheet(u"QPushButton {width: 65px;\n"
                                          "background-color: white;\n"
                                          "border: 2px solid #2f3e40;;\n"
                                          "color: #2f3e40;;\n"
                                          "padding: 6px;\n"
                                          "border-radius: 10px;}\n"
                                          "\n"
                                          "QPushButton:hover {background-color: #2f3e40;;color: white;}\n"
                                          "QPushButton:pressed { margin: 1px; }\n"
                                          "")

           self.gridLayout.addWidget(self.num_dossier, 0, 9, 1, 1)

           self.label_9 = QLabel(self.frame_4)
           self.label_9.setObjectName(u"label_9")
           self.label_9.setFont(font1)
           self.label_9.setStyleSheet(u"color: #2f3e46;")

           self.gridLayout.addWidget(self.label_9, 4, 8, 1, 1)

           self.label_3 = QLabel(self.frame_4)
           self.label_3.setObjectName(u"label_3")
           self.label_3.setFont(font1)
           self.label_3.setStyleSheet(u"color: #2f3e46;")

           self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

           self.date = QDateEdit(self.frame_4)
           self.date.setObjectName(u"date")
           self.date.setStyleSheet(u"background-color: white;\n"
                                   "color: #2f3e46;\n"
                                   "padding: 3px;\n"
                                   "border : 3px solid #52796f;\n"
                                   "border-radius: 10px;\n"
                                   "")

           self.gridLayout.addWidget(self.date, 4, 1, 1, 1)

           self.verticalLayout_4.addWidget(self.frame_4)

           self.frame = QFrame(self.frame_2)
           self.frame.setObjectName(u"frame")
           self.frame.setFrameShape(QFrame.StyledPanel)
           self.frame.setFrameShadow(QFrame.Raised)
           self.horizontalLayout_2 = QHBoxLayout(self.frame)
           self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
           self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
           self.table_prestation_debour = QTableWidget(self.frame)
           if (self.table_prestation_debour.columnCount() < 3):
               self.table_prestation_debour.setColumnCount(3)
           font2 = QFont()
           font2.setPointSize(8)
           __qtablewidgetitem = QTableWidgetItem()
           __qtablewidgetitem.setFont(font2);
           self.table_prestation_debour.setHorizontalHeaderItem(0, __qtablewidgetitem)
           __qtablewidgetitem1 = QTableWidgetItem()
           self.table_prestation_debour.setHorizontalHeaderItem(1, __qtablewidgetitem1)
           __qtablewidgetitem2 = QTableWidgetItem()
           self.table_prestation_debour.setHorizontalHeaderItem(2, __qtablewidgetitem2)
           self.table_prestation_debour.setObjectName(u"table_prestation_debour")
           self.table_prestation_debour.setSelectionBehavior(QAbstractItemView.SelectRows)
           self.table_prestation_debour.horizontalHeader().setCascadingSectionResizes(True)
           self.table_prestation_debour.horizontalHeader().setDefaultSectionSize(250)

           self.horizontalLayout_2.addWidget(self.table_prestation_debour)

           self.frame_6 = QFrame(self.frame)
           self.frame_6.setObjectName(u"frame_6")
           self.frame_6.setFrameShape(QFrame.StyledPanel)
           self.frame_6.setFrameShadow(QFrame.Raised)
           self.verticalLayout = QVBoxLayout(self.frame_6)
           self.verticalLayout.setObjectName(u"verticalLayout")
           self.nouveau_facture = QPushButton(self.frame_6)
           self.nouveau_facture.setObjectName(u"nouveau_facture")
           self.nouveau_facture.setFont(font)
           self.nouveau_facture.setStyleSheet(u"QPushButton {width: 65px;\n"
                                              "background-color: white;\n"
                                              "border: 2px solid #3bb273;\n"
                                              "color: #3bb273;\n"
                                              "padding: 6px;\n"
                                              "border-radius: 10px;}\n"
                                              "\n"
                                              "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                              "QPushButton:pressed { margin: 1px; }\n"
                                              "")

           self.verticalLayout.addWidget(self.nouveau_facture)

           self.modifier_facture = QPushButton(self.frame_6)
           self.modifier_facture.setObjectName(u"modifier_facture")
           self.modifier_facture.setFont(font)
           self.modifier_facture.setStyleSheet(u"QPushButton {width: 65px;\n"
                                               "background-color: white;\n"
                                               "border: 2px solid #3bb273;\n"
                                               "color: #3bb273;\n"
                                               "padding: 6px;\n"
                                               "border-radius: 10px;}\n"
                                               "\n"
                                               "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                               "QPushButton:pressed { margin: 1px; }\n"
                                               "")

           self.verticalLayout.addWidget(self.modifier_facture)

           self.supprimer_facture = QPushButton(self.frame_6)
           self.supprimer_facture.setObjectName(u"supprimer_facture")
           self.supprimer_facture.setFont(font)
           self.supprimer_facture.setStyleSheet(u"QPushButton {background-color: white;\n"
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

           self.verticalLayout.addWidget(self.supprimer_facture)

           self.horizontalLayout_2.addWidget(self.frame_6)

           self.verticalLayout_4.addWidget(self.frame)

           self.frame_5 = QFrame(self.frame_2)
           self.frame_5.setObjectName(u"frame_5")
           self.frame_5.setFrameShape(QFrame.StyledPanel)
           self.frame_5.setFrameShadow(QFrame.Raised)
           self.verticalLayout_3 = QVBoxLayout(self.frame_5)
           self.verticalLayout_3.setObjectName(u"verticalLayout_3")
           self.valider_facture = QPushButton(self.frame_5)
           self.valider_facture.setObjectName(u"valider_facture")
           self.valider_facture.setFont(font)
           self.valider_facture.setStyleSheet(u"QPushButton {width: 65px;\n"
                                              "background-color: white;\n"
                                              "border: 2px solid #3bb273;\n"
                                              "color: #3bb273;\n"
                                              "padding: 6px;\n"
                                              "border-radius: 10px;}\n"
                                              "\n"
                                              "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                              "QPushButton:pressed { margin: 1px; }\n"
                                              "")

           self.verticalLayout_3.addWidget(self.valider_facture)

           self.fermer_facture = QPushButton(self.frame_5)
           self.fermer_facture.setObjectName(u"fermer_facture")
           self.fermer_facture.setFont(font)
           self.fermer_facture.setStyleSheet(u"QPushButton {background-color: white;\n"
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

           self.verticalLayout_3.addWidget(self.fermer_facture)

           self.verticalLayout_4.addWidget(self.frame_5)

           self.verticalLayout_2.addWidget(self.frame_2)

           self.retranslateUi(Form)

           QMetaObject.connectSlotsByName(Form)

       # setupUi

    def retranslateUi(self, Form):
           Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
           self.label_2.setText(QCoreApplication.translate("Form", u"Facture", None))
           self.label_7.setText(QCoreApplication.translate("Form", u"client", None))
           self.label.setText(QCoreApplication.translate("Form", u"Num facture", None))
           self.num_dossier.setText(QCoreApplication.translate("Form", u"  N\u00b0 Dossier  ", None))
           self.label_9.setText(
               QCoreApplication.translate("Form", u"                                           Montant", None))
           self.label_3.setText(QCoreApplication.translate("Form", u"Date", None))
           ___qtablewidgetitem = self.table_prestation_debour.horizontalHeaderItem(0)
           ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Debours / Prestation", None));
           ___qtablewidgetitem1 = self.table_prestation_debour.horizontalHeaderItem(1)
           ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Montant  Debours ", None));
           ___qtablewidgetitem2 = self.table_prestation_debour.horizontalHeaderItem(2)
           ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Montant Prestation", None));
           self.nouveau_facture.setText(QCoreApplication.translate("Form", u"Nouveau", None))
           self.modifier_facture.setText(QCoreApplication.translate("Form", u"Modifier", None))
           self.supprimer_facture.setText(QCoreApplication.translate("Form", u"Supprimer", None))
           self.valider_facture.setText(QCoreApplication.translate("Form", u"Valider", None))
           self.fermer_facture.setText(QCoreApplication.translate("Form", u"Fermer", None))
       # retranslateUi
    def nouveau(self):
        self.form2 = QWidget()
        self.widget = Ui_ajout_pres_deb(self.form2)
        self.widget.valider_ajout_prestation.clicked.connect(self.loaddata)
        self.form2.show()

    def loaddata(self):
        self.tab_db.append(self.widget.row)
        tablerow = 0
        self.table_prestation_debour.setRowCount(len(self.tab_db))
        for row in self.tab_db:
         self.table_prestation_debour.setItem(tablerow,0,QTableWidgetItem(row[0][0]))
         self.table_prestation_debour.setItem(tablerow,1,QTableWidgetItem(row[0][1]))
         self.table_prestation_debour.setItem(tablerow,2,QTableWidgetItem(row[1]))
         self.montant.setText(str(self.uidossier.montant +float(row[1])))
         tablerow += 1
         print(self.tab_db)


    def close(self):
        self.form.close()
    def numdossier(self):
        self.uidossier.form.show()
    def remplir(self):
        self.num_facture.setText(self.uidossier.value[1])
        self.num_de_declaration.setText(self.uidossier.value[2])
        self.line_numdossier.setText(self.uidossier.value[0])
        self.montant.setText(str(self.uidossier.montant + float(self.montant.text())))
    def valid(self):
        sql = "INSERT INTO facture(num_facture,date,num_dossier,client,montant) VALUES (%s,%s,%s,%s,%s)"
        val = (int(self.num_facture.text()),self.date.date().toString(Qt.ISODate),int(self.line_numdossier.text()),self.num_de_declaration.text(),float(self.montant.text()))
        mycursor.execute(sql,val)
        mydb.commit()
        self.form.close()
        file = open(self.num_facture.text()+".txt","a+")
        file.write("Numéro de la facture : ")
        file.write(self.num_facture.text())
        file.write("\nNuméro du dossier : ")
        file.write(self.line_numdossier.text())
        file.write("\nClient : ")
        file.write(self.num_de_declaration.text())
        file.write("\nDate :" )
        file.write(self.date.date().toString(Qt.ISODate))
        file.write("\nListe des préstations/debours :")
        for row in self.tab_db:
            file.write("\nnom : ")
            file.write(row[0][0])
            file.write(" | type : ")
            file.write(row[0][1])
            file.write(" | montant : ")
            file.write(row[1])
            file.write(" DA")
        file.write("\n\nMontant taxes et droits en dinar : ")
        file.write(str(self.uidossier.montant))
        file.write(" DA\nMontant total : ")
        file.write(self.montant.text()+" DA")
        file.close()
        source = self.num_facture.text()+".txt"
        target = "factures/"+ self.num_facture.text()+".txt"
        shutil.copy(source,target)
        os.remove(source)
    def close(self):
        self.form.close()

if __name__ == "__main__":
    app = QApplication()
    widget = Ui_Form()
    widget.form.show()
    app.exec_()