# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'declarantanMjmn.ui'
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
        Form.resize(614, 383)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, -1)
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
        font.setWeight(75)
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

        self.rechercher_declarant = QLineEdit(self.frame_4)
        self.rechercher_declarant.setObjectName(u"rechercher_declarant")
        self.rechercher_declarant.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.gridLayout.addWidget(self.rechercher_declarant, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.declarant_table = QTableWidget(self.frame_2)
        if (self.declarant_table.columnCount() < 5):
            self.declarant_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.declarant_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.declarant_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.declarant_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.declarant_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.declarant_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.declarant_table.setObjectName(u"declarant_table")
        self.declarant_table.setFont(font)
        self.declarant_table.setStyleSheet(u"background-color: white;\n"
"color: #52796f;\n"
"selection-background-color: #a2d2ff;\n"
"selection-color:#2f3e46;\n"
"border-radius: 10px;")
        self.declarant_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.declarant_table.setAlternatingRowColors(True)
        self.declarant_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.declarant_table.horizontalHeader().setMinimumSectionSize(39)
        self.declarant_table.horizontalHeader().setDefaultSectionSize(90)
        self.declarant_table.horizontalHeader().setStretchLastSection(True)
        self.declarant_table.verticalHeader().setVisible(False)

        self.horizontalLayout_2.addWidget(self.declarant_table)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.valider = QPushButton(self.frame_2)
        self.valider.setObjectName(u"valider")
        self.valider.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout_3.addWidget(self.valider)

        self.nouveau_declarant = QPushButton(self.frame_2)
        self.nouveau_declarant.setObjectName(u"nouveau_declarant")
        self.nouveau_declarant.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout_3.addWidget(self.nouveau_declarant)

        self.modifier_declarant = QPushButton(self.frame_2)
        self.modifier_declarant.setObjectName(u"modifier_declarant")
        self.modifier_declarant.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout_3.addWidget(self.modifier_declarant)

        self.supprimer_declarant = QPushButton(self.frame_2)
        self.supprimer_declarant.setObjectName(u"supprimer_declarant")
        self.supprimer_declarant.setStyleSheet(u"QPushButton {background-color: white;\n"
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

        self.verticalLayout_3.addWidget(self.supprimer_declarant)

        self.fermer_declarant = QPushButton(self.frame_2)
        self.fermer_declarant.setObjectName(u"fermer_declarant")
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
"/*#ee2e31*/")

        self.verticalLayout_3.addWidget(self.fermer_declarant)

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
        self.label_2.setText(QCoreApplication.translate("Form", u"declarant", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"rechercher", None))
        ___qtablewidgetitem = self.declarant_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"nom", None));
        ___qtablewidgetitem1 = self.declarant_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"prenom", None));
        ___qtablewidgetitem2 = self.declarant_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"tel", None));
        ___qtablewidgetitem3 = self.declarant_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"email", None));
        ___qtablewidgetitem4 = self.declarant_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"adresse", None));
        self.valider.setText(QCoreApplication.translate("Form", u"valider", None))
        self.nouveau_declarant.setText(QCoreApplication.translate("Form", u"Nouveau", None))
        self.modifier_declarant.setText(QCoreApplication.translate("Form", u"Modifier", None))
        self.supprimer_declarant.setText(QCoreApplication.translate("Form", u"Supprimer", None))
        self.fermer_declarant.setText(QCoreApplication.translate("Form", u"Fermer", None))
    # retranslateUi

