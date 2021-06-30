# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'navireYiTqOR.ui'
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
        Form.resize(526, 380)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,0.3);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.groupBox)
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
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(530, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #52796f;")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.rechercher_navire = QLineEdit(self.frame_3)
        self.rechercher_navire.setObjectName(u"rechercher_navire")
        font2 = QFont()
        font2.setPointSize(8)
        self.rechercher_navire.setFont(font2)
        self.rechercher_navire.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border : 1px solid #52796f;\n"
"border-radius: 3px;\n"
"")

        self.horizontalLayout_2.addWidget(self.rechercher_navire)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 2)

        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.navire_table = QTableWidget(self.groupBox_2)
        if (self.navire_table.columnCount() < 2):
            self.navire_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.navire_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.navire_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.navire_table.setObjectName(u"navire_table")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setWeight(50)
        self.navire_table.setFont(font3)
        self.navire_table.setStyleSheet(u"background-color: white;\n"
"color: #52796f;\n"
"selection-background-color: #a2d2ff;\n"
"selection-color:#2f3e46;\n"
"border-radius: 10px;\n"
"")
        self.navire_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.navire_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.navire_table.setAlternatingRowColors(True)
        self.navire_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.navire_table.horizontalHeader().setCascadingSectionResizes(False)
        self.navire_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.navire_table.horizontalHeader().setStretchLastSection(True)
        self.navire_table.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.navire_table, 0, 0, 3, 1)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nouveau_navire = QPushButton(self.groupBox_2)
        self.nouveau_navire.setObjectName(u"nouveau_navire")
        self.nouveau_navire.setMinimumSize(QSize(81, 30))
        self.nouveau_navire.setFont(font1)
        self.nouveau_navire.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.verticalLayout.addWidget(self.nouveau_navire)

        self.modifier_navire = QPushButton(self.groupBox_2)
        self.modifier_navire.setObjectName(u"modifier_navire")
        self.modifier_navire.setMinimumSize(QSize(81, 30))
        self.modifier_navire.setFont(font1)
        self.modifier_navire.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.verticalLayout.addWidget(self.modifier_navire)

        self.supprimer_navire = QPushButton(self.groupBox_2)
        self.supprimer_navire.setObjectName(u"supprimer_navire")
        self.supprimer_navire.setMinimumSize(QSize(81, 30))
        self.supprimer_navire.setFont(font1)
        self.supprimer_navire.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #ee2e31;\n"
"padding: 5px;\n"
"border: 2px solid #ee2e31;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #ee2e31;color: white;}\n"
"QPushButton:pressed{margin: 1px;}")

        self.verticalLayout.addWidget(self.supprimer_navire)

        self.fermer_navire = QPushButton(self.groupBox_2)
        self.fermer_navire.setObjectName(u"fermer_navire")
        self.fermer_navire.setMinimumSize(QSize(81, 30))
        self.fermer_navire.setFont(font1)
        self.fermer_navire.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #ee2e31;\n"
"padding: 5px;\n"
"border: 2px solid #ee2e31;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #ee2e31;color: white;}\n"
"QPushButton:pressed{margin: 1px;}")

        self.verticalLayout.addWidget(self.fermer_navire)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 2, 1, 2)

        self.gridLayout_2.setColumnStretch(0, 4)

        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Form", u"Navire", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Recherche", None))
        self.groupBox_2.setTitle("")
        ___qtablewidgetitem = self.navire_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Navire", None));
        ___qtablewidgetitem1 = self.navire_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Description", None));
        self.nouveau_navire.setText(QCoreApplication.translate("Form", u"Nouveau", None))
        self.modifier_navire.setText(QCoreApplication.translate("Form", u"Modifier", None))
        self.supprimer_navire.setText(QCoreApplication.translate("Form", u"Supprimer", None))
        self.fermer_navire.setText(QCoreApplication.translate("Form", u"Fermer", None))
    # retranslateUi

