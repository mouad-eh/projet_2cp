# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bon_visiteOpWqgw.ui'
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
        Form.resize(616, 323)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
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

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #52796f;")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.rechercher_bon_visite = QLineEdit(self.frame_4)
        self.rechercher_bon_visite.setObjectName(u"rechercher_bon_visite")
        self.rechercher_bon_visite.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout.addWidget(self.rechercher_bon_visite, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.bon_visite_table = QTableWidget(self.frame_2)
        if (self.bon_visite_table.columnCount() < 5):
            self.bon_visite_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.bon_visite_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.bon_visite_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.bon_visite_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.bon_visite_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.bon_visite_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.bon_visite_table.setObjectName(u"bon_visite_table")
        self.bon_visite_table.setFont(font)
        self.bon_visite_table.setStyleSheet(u"background-color: white;\n"
"color: #52796f;\n"
"selection-background-color: #a2d2ff;\n"
"selection-color:#2f3e46;\n"
"border-radius: 10px;\n"
"")
        self.bon_visite_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.bon_visite_table.setAlternatingRowColors(True)
        self.bon_visite_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.bon_visite_table.horizontalHeader().setStretchLastSection(True)
        self.bon_visite_table.verticalHeader().setVisible(False)

        self.horizontalLayout_2.addWidget(self.bon_visite_table)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.nouveau_bon_visite = QPushButton(self.frame_2)
        self.nouveau_bon_visite.setObjectName(u"nouveau_bon_visite")
        self.nouveau_bon_visite.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout_3.addWidget(self.nouveau_bon_visite)

        self.modifier_bon_visite = QPushButton(self.frame_2)
        self.modifier_bon_visite.setObjectName(u"modifier_bon_visite")
        self.modifier_bon_visite.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout_3.addWidget(self.modifier_bon_visite)

        self.supprimer_bon_visite = QPushButton(self.frame_2)
        self.supprimer_bon_visite.setObjectName(u"supprimer_bon_visite")
        self.supprimer_bon_visite.setStyleSheet(u"QPushButton {background-color: white;\n"
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
"/*#ee2e31*/")

        self.verticalLayout_3.addWidget(self.supprimer_bon_visite)

        self.fermer_bon_visite = QPushButton(self.frame_2)
        self.fermer_bon_visite.setObjectName(u"fermer_bon_visite")
        self.fermer_bon_visite.setStyleSheet(u"QPushButton {background-color: white;\n"
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
"/*#ee2e31*/")

        self.verticalLayout_3.addWidget(self.fermer_bon_visite)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Bon de visite", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"N\u00b0 Dossier", None))
        ___qtablewidgetitem = self.bon_visite_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"declarant", None));
        ___qtablewidgetitem1 = self.bon_visite_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"num_dossier", None));
        ___qtablewidgetitem2 = self.bon_visite_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"date", None));
        ___qtablewidgetitem3 = self.bon_visite_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"agent", None));
        ___qtablewidgetitem4 = self.bon_visite_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"transit", None));
        self.nouveau_bon_visite.setText(QCoreApplication.translate("Form", u"Nouveau", None))
        self.modifier_bon_visite.setText(QCoreApplication.translate("Form", u"Modifier", None))
        self.supprimer_bon_visite.setText(QCoreApplication.translate("Form", u"Supprimer", None))
        self.fermer_bon_visite.setText(QCoreApplication.translate("Form", u"Fermer", None))
    # retranslateUi

