# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajout_bon_visitegnWlcM.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(493, 211)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: #2f3e40; /*#2f3e46,1a535c;1d3557;233d4d*/\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(510, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #52796f;")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.declarant = QLineEdit(self.frame_4)
        self.declarant.setObjectName(u"declarant")
        self.declarant.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout.addWidget(self.declarant, 0, 2, 1, 2)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #52796f;")

        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 2)

        self.num_dossier = QLineEdit(self.frame_4)
        self.num_dossier.setObjectName(u"num_dossier")
        self.num_dossier.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout.addWidget(self.num_dossier, 0, 6, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: #52796f;")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.date = QLineEdit(self.frame_4)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout.addWidget(self.date, 1, 1, 1, 2)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: #52796f;")

        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 2)

        self.agent = QLineEdit(self.frame_4)
        self.agent.setObjectName(u"agent")
        self.agent.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout.addWidget(self.agent, 1, 5, 1, 2)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: #52796f;")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)

        self.transit = QLineEdit(self.frame_4)
        self.transit.setObjectName(u"transit")
        self.transit.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout.addWidget(self.transit, 2, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.valider_ajout_bon_visite = QPushButton(self.frame_5)
        self.valider_ajout_bon_visite.setObjectName(u"valider_ajout_bon_visite")
        self.valider_ajout_bon_visite.setFont(font)
        self.valider_ajout_bon_visite.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout_3.addWidget(self.valider_ajout_bon_visite)

        self.fermer_ajout_bon_visite = QPushButton(self.frame_5)
        self.fermer_ajout_bon_visite.setObjectName(u"fermer_ajout_bon_visite")
        self.fermer_ajout_bon_visite.setFont(font)
        self.fermer_ajout_bon_visite.setStyleSheet(u"QPushButton {background-color: white;\n"
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

        self.verticalLayout_3.addWidget(self.fermer_ajout_bon_visite)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ajout bon de visite", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Declarant", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"N\u00b0 Dossier", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Date", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Agent", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Transit", None))
        self.valider_ajout_bon_visite.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.fermer_ajout_bon_visite.setText(QCoreApplication.translate("Form", u"Fermer", None))
    # retranslateUi

