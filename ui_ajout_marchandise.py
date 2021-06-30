# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajout_marchandiseEQNELA.ui'
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
        Form.resize(571, 397)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,0.3);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #2f3e46;\n"
"color: white;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
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
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.fermer_ajout_marchandise = QPushButton(self.frame_3)
        self.fermer_ajout_marchandise.setObjectName(u"fermer_ajout_marchandise")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.fermer_ajout_marchandise.setFont(font1)
        self.fermer_ajout_marchandise.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #ee2e31;\n"
"padding: 5px;\n"
"border: 2px solid #ee2e31;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #ee2e31;color: white;}\n"
"QPushButton:pressed{margin: 1px;}")

        self.horizontalLayout_3.addWidget(self.fermer_ajout_marchandise)

        self.ajouter_ajout_marchandise = QPushButton(self.frame_3)
        self.ajouter_ajout_marchandise.setObjectName(u"ajouter_ajout_marchandise")
        self.ajouter_ajout_marchandise.setFont(font1)
        self.ajouter_ajout_marchandise.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout_3.addWidget(self.ajouter_ajout_marchandise)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #52796f;")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #52796f;")

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.type = QLineEdit(self.frame_3)
        self.type.setObjectName(u"type")
        self.type.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border : 1px solid #52796f;\n"
"border-radius: 3px;\n"
"")

        self.verticalLayout.addWidget(self.type)

        self.description = QTextEdit(self.frame_3)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border : 1px solid #52796f;\n"
"border-radius: 3px;\n"
"")

        self.verticalLayout.addWidget(self.description)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ajout Marchandise", None))
        self.fermer_ajout_marchandise.setText(QCoreApplication.translate("Form", u"fermer", None))
        self.ajouter_ajout_marchandise.setText(QCoreApplication.translate("Form", u"ajouter", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Type", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Description", None))
    # retranslateUi

