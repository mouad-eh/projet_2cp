# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifier_bon_sortiecZzYTG.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
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
        Form.resize(492, 211)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: #52796f;")

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 2)

        self.declarant = QLineEdit(self.frame_4)
        self.declarant.setObjectName(u"declarant")
        self.declarant.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout_3.addWidget(self.declarant, 0, 2, 1, 1)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: #52796f;")

        self.gridLayout_3.addWidget(self.label_9, 0, 3, 1, 2)

        self.num_dossier = QLineEdit(self.frame_4)
        self.num_dossier.setObjectName(u"num_dossier")
        self.num_dossier.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout_3.addWidget(self.num_dossier, 0, 5, 1, 1)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: #52796f;")

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.date = QLineEdit(self.frame_4)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout_3.addWidget(self.date, 1, 1, 1, 2)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: #52796f;")

        self.gridLayout_3.addWidget(self.label_11, 1, 3, 1, 1)

        self.agent = QLineEdit(self.frame_4)
        self.agent.setObjectName(u"agent")
        self.agent.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout_3.addWidget(self.agent, 1, 4, 1, 2)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: #52796f;")

        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 2)

        self.transit = QLineEdit(self.frame_4)
        self.transit.setObjectName(u"transit")
        self.transit.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout_3.addWidget(self.transit, 2, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.valider_modifier_bon_sortie = QPushButton(self.frame_5)
        self.valider_modifier_bon_sortie.setObjectName(u"valider_modifier_bon_sortie")
        self.valider_modifier_bon_sortie.setFont(font)
        self.valider_modifier_bon_sortie.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.gridLayout_4.addWidget(self.valider_modifier_bon_sortie, 1, 0, 1, 1)

        self.fermer_modifier_bon_sortie = QPushButton(self.frame_5)
        self.fermer_modifier_bon_sortie.setObjectName(u"fermer_modifier_bon_sortie")
        self.fermer_modifier_bon_sortie.setFont(font)
        self.fermer_modifier_bon_sortie.setStyleSheet(u"QPushButton {background-color: white;\n"
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

        self.gridLayout_4.addWidget(self.fermer_modifier_bon_sortie, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Modifier bon de sortie", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Declarant", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"N\u00b0 Dossier", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Date", None))
        self.date.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Agent", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Transit", None))
        self.valider_modifier_bon_sortie.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.fermer_modifier_bon_sortie.setText(QCoreApplication.translate("Form", u"Fermer", None))
    # retranslateUi

