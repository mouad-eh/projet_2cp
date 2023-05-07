# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginkSizFL.ui'
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
        Form.resize(400, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,0.3);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #2f3e46;\n"
"color: white;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(213, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #52796f;")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.nom = QLineEdit(self.frame_3)
        self.nom.setObjectName(u"nom")
        self.nom.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border : 1px solid #52796f;\n"
"border-radius: 3px;")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.nom)


        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.login = QPushButton(self.frame_3)
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.gridLayout_2.addWidget(self.login, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(303, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #52796f;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.password = QLineEdit(self.frame_3)
        self.password.setObjectName(u"password")
        self.password.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border : 1px solid #52796f;\n"
"border-radius: 3px;")
        self.password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.password)


        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 5)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"AZMA PARC", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Bienvenue", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nom d'utilisateur", None))
        self.login.setText(QCoreApplication.translate("Form", u"Connecter", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"mot de passe", None))
        self.password.setInputMask("")
    # retranslateUi

