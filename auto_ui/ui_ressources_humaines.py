# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ressources_humaineseTdodg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from auto_ui.ui_client import *
from ui.declarant import DeclarantWindow



class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(621, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #52796f;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.client = QPushButton(self.frame_2)
        self.client.setObjectName(u"client")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.client.setFont(font)
        self.client.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.client)

        self.declarant = QPushButton(self.frame_2)
        self.declarant.setObjectName(u"declarant")
        self.declarant.setFont(font)
        self.declarant.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.declarant)

        """self.fournisseur = QPushButton(self.frame_2)
        self.fournisseur.setObjectName(u"fournisseur")
        self.fournisseur.setFont(font)
        self.fournisseur.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.fournisseur)"""

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 2)

        self.verticalLayout.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.client_2 = Ui_client()
        self.client_2.form.setObjectName(u"client_2")
        self.stackedWidget.addWidget(self.client_2.form)
        self.declarant_2 = DeclarantWindow()
        self.declarant_2.setObjectName(u"declarant_2")
        self.stackedWidget.addWidget(self.declarant_2)
        #self.fournisseur_2 = QWidget()
        #self.fournisseur_2.setObjectName(u"fournisseur_2")
        #self.stackedWidget.addWidget(self.fournisseur_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.client.setText(QCoreApplication.translate("Form", u"Client", None))
        self.declarant.setText(QCoreApplication.translate("Form", u"D\u00e9clarant", None))
#        self.fournisseur.setText(QCoreApplication.translate("Form", u"fournisseur", None))
    # retranslateUi

