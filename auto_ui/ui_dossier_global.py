# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dossier_golbalDdFmMB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from auto_ui.dossier_final import Ui_Form as Ui_dossier
from ui.file_bon_sortie import SortieWindow
from ui.file_bon_visite import VisiteWindow


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

        self.ajout_dossier = QPushButton(self.frame_2)
        self.ajout_dossier.setObjectName(u"ajout_dossier")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ajout_dossier.setFont(font)
        self.ajout_dossier.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.ajout_dossier)

        self.consulter_dossier = QPushButton(self.frame_2)
        self.consulter_dossier.setObjectName(u"consulter_dossier")
        self.consulter_dossier.setFont(font)
        self.consulter_dossier.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.consulter_dossier)

        self.bon_de_visite = QPushButton(self.frame_2)
        self.bon_de_visite.setObjectName(u"bon_de_visite")
        self.bon_de_visite.setFont(font)
        self.bon_de_visite.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.bon_de_visite)

        self.bon_de_sortie = QPushButton(self.frame_2)
        self.bon_de_sortie.setObjectName(u"bon_de_sortie")
        self.bon_de_sortie.setFont(font)
        self.bon_de_sortie.setStyleSheet(u"QPushButton {\n"
"background-color: #52796f;\n"
"color: white;\n"
"padding: 4px;\n"
"border: 2px solid #52796f;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #52796f;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout.addWidget(self.bon_de_sortie)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(5, 2)

        self.verticalLayout.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dossier = Ui_dossier()
        self.ajout_dossier_2 = self.dossier.form
        self.ajout_dossier_2.setObjectName(u"ajout_dossier_2")
        self.stackedWidget.addWidget(self.ajout_dossier_2)
        self.bon_de_sortie_2 = SortieWindow()
        self.bon_de_sortie_2.setObjectName(u"bon_de_sortie_2")
        self.stackedWidget.addWidget(self.bon_de_sortie_2)
        self.consulter_dossier_2 = QWidget()
        self.consulter_dossier_2.setObjectName(u"consulter_dossier_2")
        self.stackedWidget.addWidget(self.consulter_dossier_2)
        self.bon_de_visite_2 = VisiteWindow()
        self.bon_de_visite_2.setObjectName(u"bon_de_visite_2")
        self.stackedWidget.addWidget(self.bon_de_visite_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ajout_dossier.setText(QCoreApplication.translate("Form", u"Ajout dossier", None))
        self.consulter_dossier.setText(QCoreApplication.translate("Form", u"Consulter dossier", None))
        self.bon_de_visite.setText(QCoreApplication.translate("Form", u"Bon de visite", None))
        self.bon_de_sortie.setText(QCoreApplication.translate("Form", u"Bon de sortie", None))
    # retranslateUi

