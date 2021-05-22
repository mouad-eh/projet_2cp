# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'navirechIiFd.ui'
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
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 131, 130);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
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
        self.label_2.setStyleSheet(u"color: rgb(0, 131, 130);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.rechercher_navire = QLineEdit(self.frame_3)
        self.rechercher_navire.setObjectName(u"rechercher_navire")
        self.rechercher_navire.setStyleSheet(u"border : 1px solid rgba(0,0,0,0);\n"
"border-bottom-color : rgba(46,82,101,255);")

        self.horizontalLayout_2.addWidget(self.rechercher_navire)

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
        self.navire_table = QTableWidget(self.frame_4)
        if (self.navire_table.columnCount() < 2):
            self.navire_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.navire_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.navire_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.navire_table.setObjectName(u"navire_table")
        self.navire_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.navire_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.navire_table.setAlternatingRowColors(False)
        self.navire_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.navire_table.horizontalHeader().setCascadingSectionResizes(False)
        self.navire_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.navire_table.horizontalHeader().setStretchLastSection(True)
        self.navire_table.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.navire_table, 0, 0, 3, 1)

        self.verticalSpacer = QSpacerItem(20, 54, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nouveau_navire = QPushButton(self.frame_4)
        self.nouveau_navire.setObjectName(u"nouveau_navire")
        self.nouveau_navire.setStyleSheet(u"background-color: rgb(0, 131, 130);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.nouveau_navire)

        self.modifier_navire = QPushButton(self.frame_4)
        self.modifier_navire.setObjectName(u"modifier_navire")
        self.modifier_navire.setStyleSheet(u"background-color: rgb(0, 131, 130);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.modifier_navire)

        self.supprimer_navire = QPushButton(self.frame_4)
        self.supprimer_navire.setObjectName(u"supprimer_navire")
        self.supprimer_navire.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.supprimer_navire)

        self.fermer_navire = QPushButton(self.frame_4)
        self.fermer_navire.setObjectName(u"fermer_navire")
        self.fermer_navire.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.fermer_navire)


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
        self.label.setText(QCoreApplication.translate("Form", u"Navire", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Recherche", None))
        ___qtablewidgetitem = self.navire_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Navire", None));
        ___qtablewidgetitem1 = self.navire_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Description", None));
        self.nouveau_navire.setText(QCoreApplication.translate("Form", u"Nouveau", None))
        self.modifier_navire.setText(QCoreApplication.translate("Form", u"Modifier", None))
        self.supprimer_navire.setText(QCoreApplication.translate("Form", u"Supprimer", None))
        self.fermer_navire.setText(QCoreApplication.translate("Form", u"Fermer", None))
    # retranslateUi

