# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ajout prestation debournVstwh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from auto_ui.prestation_debour_ui import *
from auto_ui.Facture import *
mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="rotage2015002",
   database="projet_beta"
)
mycursor = mydb.cursor()
class Ui_ajout_pres_deb(object):
    def __init__(self,form):
        self.form = form
        self.setupUi(form)
        self.valider_ajout_prestation.clicked.connect(self.valider)
        self.ajouter.clicked.connect(self.ajout)
        self.fermer_ajout_prestation.clicked.connect(self.fermer)
        self.row = ()

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(634, 303)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #2f3e46;")

        self.verticalLayout_2.addWidget(self.label)

        self.ajouter = QPushButton(self.frame_2)
        self.ajouter.setObjectName(u"ajouter")
        self.ajouter.setFont(font)
        self.ajouter.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #2f3e40;\n"
"color: #2f3e40;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #2f3e40;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout_2.addWidget(self.ajouter)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: #2f3e46;")

        self.verticalLayout_2.addWidget(self.label_5)

        self.montant = QLineEdit(self.frame_2)
        self.montant.setObjectName(u"montant")
        self.montant.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.verticalLayout_2.addWidget(self.montant)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.valider_ajout_prestation = QPushButton(self.frame_4)
        self.valider_ajout_prestation.setObjectName(u"valider_ajout_prestation")
        self.valider_ajout_prestation.setFont(font)
        self.valider_ajout_prestation.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout_4.addWidget(self.valider_ajout_prestation)

        self.fermer_ajout_prestation = QPushButton(self.frame_4)
        self.fermer_ajout_prestation.setObjectName(u"fermer_ajout_prestation")
        self.fermer_ajout_prestation.setFont(font)
        self.fermer_ajout_prestation.setStyleSheet(u"QPushButton {background-color: white;\n"
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

        self.verticalLayout_4.addWidget(self.fermer_ajout_prestation)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ajout Prestation/Debour", None))
        self.label.setText(QCoreApplication.translate("Form", u"Prestation / Debour", None))
        self.ajouter.setText(QCoreApplication.translate("Form", u"Ajouter", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Montant", None))
        self.valider_ajout_prestation.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.fermer_ajout_prestation.setText(QCoreApplication.translate("Form", u"Fermer", None))
    # retranslateUi
    def ajout(self):
         self.form2 = QWidget()
         self.widget = Ui_prestation_debours(self.form2)
         self.form2.show()
    def valider(self):
        self.row = (self.widget.value,self.montant.text())
        self.form.close()
    def fermer(self):
        self.form.close()




if __name__ == "__main__":
    app = QApplication()
    form=QWidget()
    widget = Ui_prestation_debours(form)
    form.show()
    app.exec_()