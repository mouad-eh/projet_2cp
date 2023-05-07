# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifier_declarant NkCkLt.ui'
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
        Form.resize(520, 211)
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
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: #2f3e40; /*#2f3e46,1a535c;1d3557;233d4d*/\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_8)

        self.horizontalSpacer = QSpacerItem(510, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

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
        self.email = QLineEdit(self.frame_4)
        self.email.setObjectName(u"email")
        self.email.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout_3.addWidget(self.email, 1, 5, 1, 1)

        self.nom = QLineEdit(self.frame_4)
        self.nom.setObjectName(u"nom")
        self.nom.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout_3.addWidget(self.nom, 0, 2, 1, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: #52796f;")

        self.gridLayout_3.addWidget(self.label_3, 0, 3, 1, 2)

        self.label_1 = QLabel(self.frame_4)
        self.label_1.setObjectName(u"label_1")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"color: #52796f;")

        self.gridLayout_3.addWidget(self.label_1, 0, 0, 1, 2)

        self.prenom = QLineEdit(self.frame_4)
        self.prenom.setObjectName(u"prenom")
        self.prenom.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout_3.addWidget(self.prenom, 0, 5, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: #52796f;")

        self.gridLayout_3.addWidget(self.label_4, 1, 3, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: #52796f;")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.tel = QLineEdit(self.frame_4)
        self.tel.setObjectName(u"tel")
        self.tel.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout_3.addWidget(self.tel, 1, 2, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #52796f;")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.adresse = QLineEdit(self.frame_4)
        self.adresse.setObjectName(u"adresse")
        self.adresse.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout_3.addWidget(self.adresse, 2, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.valider_declarant = QPushButton(self.frame_5)
        self.valider_declarant.setObjectName(u"valider_declarant")
        self.valider_declarant.setFont(font)
        self.valider_declarant.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.gridLayout_4.addWidget(self.valider_declarant, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.fermer_declarant = QPushButton(self.frame_5)
        self.fermer_declarant.setObjectName(u"fermer_declarant")
        self.fermer_declarant.setFont(font)
        self.fermer_declarant.setStyleSheet(u"QPushButton {background-color: white;\n"
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

        self.gridLayout_4.addWidget(self.fermer_declarant, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Modifier declarant", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"pr\u00e9nom", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"nom", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Tel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Adresse", None))
        self.valider_declarant.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.fermer_declarant.setText(QCoreApplication.translate("Form", u"Fermer", None))
    # retranslateUi

