# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ressources_materiellesWKUauG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.test_navire import NavireWindow
from ui.file_pays import PaysWindow
from ui.file_monnaie import MonnaieWindow

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

        self.navire = QPushButton(self.frame_2)
        self.navire.setObjectName(u"navire")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.navire.setFont(font)
        self.navire.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.navire)

        self.monnaie = QPushButton(self.frame_2)
        self.monnaie.setObjectName(u"monnaie")
        self.monnaie.setFont(font)
        self.monnaie.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.monnaie)

        self.pays = QPushButton(self.frame_2)
        self.pays.setObjectName(u"pays")
        self.pays.setFont(font)
        self.pays.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.pays)

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
        self.navire_2 = NavireWindow()
        self.navire_2.setObjectName(u"navire_2")
        self.stackedWidget.addWidget(self.navire_2)
        self.monnaie_2 = MonnaieWindow()
        self.monnaie_2.setObjectName(u"monnaie_2")
        self.stackedWidget.addWidget(self.monnaie_2)
        self.pays_2 = PaysWindow()
        self.pays_2.setObjectName(u"pays_2")
        self.stackedWidget.addWidget(self.pays_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.navire.setText(QCoreApplication.translate("Form", u"Navire", None))
        self.monnaie.setText(QCoreApplication.translate("Form", u"Monnaie", None))
        self.pays.setText(QCoreApplication.translate("Form", u"Pays", None))
    # retranslateUi

