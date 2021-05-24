# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajout_camionIRBujn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(571, 232)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 131, 130);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(435, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(0, 131, 130);")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(0, 131, 130);")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(0, 131, 130);")

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.matricule = QLineEdit(self.frame_3)
        self.matricule.setObjectName(u"matricule")
        self.matricule.setStyleSheet(u"border : 1px solid rgba(0,0,0,0);\n"
"border-bottom-color : rgba(46,82,101,255);")

        self.verticalLayout.addWidget(self.matricule)

        self.disponibilite = QComboBox(self.frame_3)
        self.disponibilite.addItem("")
        self.disponibilite.addItem("")
        self.disponibilite.setObjectName(u"disponibilite")

        self.verticalLayout.addWidget(self.disponibilite)

        self.description = QTextEdit(self.frame_3)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"border : 1px solid rgba(0,0,0,0);\n"
"border-bottom-color : rgba(46,82,101,255);")

        self.verticalLayout.addWidget(self.description)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.fermer_ajout_camion = QPushButton(self.frame_3)
        self.fermer_ajout_camion.setObjectName(u"fermer_ajout_camion")
        self.fermer_ajout_camion.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.fermer_ajout_camion)

        self.ajouter_ajout_camion = QPushButton(self.frame_3)
        self.ajouter_ajout_camion.setObjectName(u"ajouter_ajout_camion")
        self.ajouter_ajout_camion.setStyleSheet(u"background-color: rgb(0, 131, 130);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.ajouter_ajout_camion)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ajout Camion", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Matricule", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Disponibilit\u00e9", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Description", None))
        self.disponibilite.setItemText(0, QCoreApplication.translate("Form", u"Disponible", None))
        self.disponibilite.setItemText(1, QCoreApplication.translate("Form", u"Non disponible", None))

        self.disponibilite.setPlaceholderText(QCoreApplication.translate("Form", u"disponibilit\u00e9", None))
        self.fermer_ajout_camion.setText(QCoreApplication.translate("Form", u"fermer", None))
        self.ajouter_ajout_camion.setText(QCoreApplication.translate("Form", u"ajouter", None))
    # retranslateUi

