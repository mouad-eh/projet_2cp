# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ajout_prestation_deboureNycLk.ui'
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

class Ui_Form(object):
    def __init__(self):
        self.form = QWidget()
        self.setupUi(self.form)
        self.valider.clicked.connect(self.valid)
        self.fermer_prestation_debour.clicked.connect(self.fermer)
        self.ajou_debour_prestation.textChanged.connect(self.couleur)
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(513, 359)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
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

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label)

        self.ajou_debour_prestation = QLineEdit(self.frame_4)
        self.ajou_debour_prestation.setObjectName(u"ajou_debour_prestation")
        self.ajou_debour_prestation.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.horizontalLayout_4.addWidget(self.ajou_debour_prestation)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(18)
        self.label_4.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox = QComboBox(self.frame_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.valider = QPushButton(self.frame_2)
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

        self.horizontalLayout_3.addWidget(self.valider)

        self.fermer_prestation_debour = QPushButton(self.frame_2)
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

        self.horizontalLayout_3.addWidget(self.fermer_prestation_debour)


        self.verticalLayout.addWidget(self.frame_2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ajouter debour prestation", None))
        self.label.setText(QCoreApplication.translate("Form", u"Debour/prestation", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Type", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"prestation", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"debour", None))

        self.valider.setText(QCoreApplication.translate("Form", u"valider", None))
        self.fermer_prestation_debour.setText(QCoreApplication.translate("Form", u"Fermer", None))
    # retranslateUi
    def valid(self):
      if(self.ajou_debour_prestation.text() != ""):
        mysql = "INSERT INTO prestation_debours(debours_prestation,type) VALUES (%s,%s) "
        val = (self.ajou_debour_prestation.text(),self.comboBox.currentIndex())
        mycursor.execute(mysql,val)
        mydb.commit()
        self.form.close()
      else:
         self.ajou_debour_prestation.setStyleSheet(u"border : 3px solid #ee2e31;\n"
                                         "border-radius:10px;\n"
                                         "padding: 3px;\n"
                                         "background-color: white;\n"

                                         )  # ee2e31
    def couleur(self):
        self.ajou_debour_prestation.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                       "border-radius:10px;\n"
                                       "color: black ; \n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"

                                       "")
    def fermer(self):
        self.form.close()
if __name__ == "__main__":
    app = QApplication()

    widget = Ui_Form()
    app.exec_()


