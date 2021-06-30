# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nature_marchandiseXmPqsn.ui'
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
        Form.resize(618, 376)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,0.3);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(530, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #52796f;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.recherche_marchandise = QLineEdit(self.frame_3)
        self.recherche_marchandise.setObjectName(u"recherche_marchandise")
        self.recherche_marchandise.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border : 1px solid #52796f;\n"
"border-radius: 3px;")

        self.horizontalLayout_2.addWidget(self.recherche_marchandise)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table_marchandise = QTableWidget(self.frame_4)
        if (self.table_marchandise.columnCount() < 2):
            self.table_marchandise.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_marchandise.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_marchandise.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_marchandise.setObjectName(u"table_marchandise")
        self.table_marchandise.setStyleSheet(u"background-color: white;\n"
"color: #52796f;\n"
"selection-background-color: #a2d2ff;\n"
"selection-color:#2f3e46;\n"
"border-radius: 10px;")
        self.table_marchandise.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_marchandise.setAlternatingRowColors(True)
        self.table_marchandise.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_marchandise.horizontalHeader().setVisible(True)
        self.table_marchandise.horizontalHeader().setCascadingSectionResizes(False)
        self.table_marchandise.horizontalHeader().setMinimumSectionSize(30)
        self.table_marchandise.horizontalHeader().setHighlightSections(True)
        self.table_marchandise.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_marchandise.horizontalHeader().setStretchLastSection(True)
        self.table_marchandise.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.table_marchandise, 0, 0, 3, 1)

        self.verticalSpacer = QSpacerItem(20, 54, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nouveau_marchandise = QPushButton(self.frame_4)
        self.nouveau_marchandise.setObjectName(u"nouveau_marchandise")
        self.nouveau_marchandise.setFont(font1)
        self.nouveau_marchandise.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.verticalLayout.addWidget(self.nouveau_marchandise)

        self.modifier_marchandise = QPushButton(self.frame_4)
        self.modifier_marchandise.setObjectName(u"modifier_marchandise")
        self.modifier_marchandise.setFont(font1)
        self.modifier_marchandise.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.verticalLayout.addWidget(self.modifier_marchandise)

        self.supprimer_marchandise = QPushButton(self.frame_4)
        self.supprimer_marchandise.setObjectName(u"supprimer_marchandise")
        self.supprimer_marchandise.setFont(font1)
        self.supprimer_marchandise.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #ee2e31;\n"
"padding: 5px;\n"
"border: 2px solid #ee2e31;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #ee2e31;color: white;}\n"
"QPushButton:pressed{margin: 1px;}")

        self.verticalLayout.addWidget(self.supprimer_marchandise)

        self.fermer_marchandise = QPushButton(self.frame_4)
        self.fermer_marchandise.setObjectName(u"fermer_marchandise")
        self.fermer_marchandise.setFont(font1)
        self.fermer_marchandise.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #ee2e31;\n"
"padding: 5px;\n"
"border: 2px solid #ee2e31;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #ee2e31;color: white;}\n"
"QPushButton:pressed{margin: 1px;}")

        self.verticalLayout.addWidget(self.fermer_marchandise)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 53, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 4)

        self.verticalLayout_2.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nature Marchandise", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Recherche", None))
        ___qtablewidgetitem = self.table_marchandise.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Nature Marchandise", None));
        ___qtablewidgetitem1 = self.table_marchandise.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Description", None));
        self.nouveau_marchandise.setText(QCoreApplication.translate("Form", u"Nouveau", None))
        self.modifier_marchandise.setText(QCoreApplication.translate("Form", u"Modifier", None))
        self.supprimer_marchandise.setText(QCoreApplication.translate("Form", u"Supprimer", None))
        self.fermer_marchandise.setText(QCoreApplication.translate("Form", u"Fermer", None))
    # retranslateUi

