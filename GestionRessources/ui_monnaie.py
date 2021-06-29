# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monnaiesnFCkC.ui'
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
        Form.resize(430, 450)
        Form.setStyleSheet(u"")
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
        self.frame_2.setStyleSheet(u"background-color: #2f3e46;\n"
"color: white;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, 0, -1)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, -1, 9, -1)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #52796f;")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.code = QLineEdit(self.frame_3)
        self.code.setObjectName(u"code")
        self.code.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.horizontalLayout_5.addWidget(self.code)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: #52796f;")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.libelle = QLineEdit(self.frame_3)
        self.libelle.setObjectName(u"libelle")
        self.libelle.setStyleSheet(u"border : 1px solid #2f3e46;\n"
"border-radius:10px;\n"
"padding: 3px;\n"
"background-color: white;\n"
"color: #2f3e46;\n"
"")

        self.horizontalLayout_5.addWidget(self.libelle)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(14, 14, 14, 14)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nouveau_monnaie = QPushButton(self.frame_4)
        self.nouveau_monnaie.setObjectName(u"nouveau_monnaie")
        self.nouveau_monnaie.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout_2.addWidget(self.nouveau_monnaie)

        self.modifier_monnaie = QPushButton(self.frame_4)
        self.modifier_monnaie.setObjectName(u"modifier_monnaie")
        self.modifier_monnaie.setStyleSheet(u"QPushButton {width: 65px;\n"
"background-color: white;\n"
"border: 2px solid #3bb273;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout_2.addWidget(self.modifier_monnaie)

        self.supprimer_monnaie = QPushButton(self.frame_4)
        self.supprimer_monnaie.setObjectName(u"supprimer_monnaie")
        self.supprimer_monnaie.setStyleSheet(u"QPushButton {background-color: white;\n"
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

        self.verticalLayout_2.addWidget(self.supprimer_monnaie)

        self.fermer_monnaie = QPushButton(self.frame_4)
        self.fermer_monnaie.setObjectName(u"fermer_monnaie")
        self.fermer_monnaie.setStyleSheet(u"QPushButton {background-color: white;\n"
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

        self.verticalLayout_2.addWidget(self.fermer_monnaie)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 104, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 72, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 2)

        self.monnaie_table = QTableWidget(self.frame_4)
        if (self.monnaie_table.columnCount() < 3):
            self.monnaie_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.monnaie_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.monnaie_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.monnaie_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.monnaie_table.setObjectName(u"monnaie_table")
        self.monnaie_table.setFont(font1)
        self.monnaie_table.setStyleSheet(u"background-color: white;\n"
"color: #52796f;\n"
"selection-background-color: #a2d2ff;\n"
"selection-color:#2f3e46;\n"
"border-radius: 10px;")
        self.monnaie_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.monnaie_table.setAlternatingRowColors(True)
        self.monnaie_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.monnaie_table.horizontalHeader().setStretchLastSection(True)
        self.monnaie_table.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.monnaie_table, 0, 0, 3, 1)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Monnaie", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Code", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Libell\u00e9", None))
        self.nouveau_monnaie.setText(QCoreApplication.translate("Form", u"Nouveau", None))
        self.modifier_monnaie.setText(QCoreApplication.translate("Form", u"Modifier", None))
        self.supprimer_monnaie.setText(QCoreApplication.translate("Form", u"Supprimer", None))
        self.fermer_monnaie.setText(QCoreApplication.translate("Form", u"Fermer", None))
        ___qtablewidgetitem = self.monnaie_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Code Monnaie", None));
        ___qtablewidgetitem1 = self.monnaie_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Libell\u00e9 Monnaie", None));
        ___qtablewidgetitem2 = self.monnaie_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Taux de Change", None));
    # retranslateUi

