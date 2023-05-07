# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'facture_golableAGKOjc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from auto_ui.Facture import Ui_Form as Ui_Facture

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
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spacer)

        self.ajout_facture = QPushButton(self.frame_2)
        self.ajout_facture.setObjectName(u"ajout_facture")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ajout_facture.setFont(font)
        self.ajout_facture.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.ajout_facture)

        self.consulter_facture = QPushButton(self.frame_2)
        self.consulter_facture.setObjectName(u"consulter_facture")
        self.consulter_facture.setFont(font)
        self.consulter_facture.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.consulter_facture)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)

        self.verticalLayout.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.facture = Ui_Facture()
        self.ajout_facture_2 = self.facture.form
        self.ajout_facture_2.setObjectName(u"ajout_facture_2")
        self.stackedWidget.addWidget(self.ajout_facture_2)
        self.consulter_facture_2 = QWidget()
        self.consulter_facture_2.setObjectName(u"consulter_facture_2")
        self.stackedWidget.addWidget(self.consulter_facture_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ajout_facture.setText(QCoreApplication.translate("Form", u"ajout facture", None))
        self.consulter_facture.setText(QCoreApplication.translate("Form", u"consulter facture", None))
    # retranslateUi

