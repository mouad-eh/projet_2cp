# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suivi_emballageshmWREJ.ui'
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
        Form.resize(587, 399)
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
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)

        self.num_dossier = QLineEdit(self.frame_2)
        self.num_dossier.setObjectName(u"num_dossier")
        self.num_dossier.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.num_dossier)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_2)

        self.client = QLineEdit(self.frame_2)
        self.client.setObjectName(u"client")
        self.client.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.client)

        self.horizontalSpacer = QSpacerItem(59, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout.setStretch(3, 5)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.tabWidget.setFont(font1)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(12)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.recherche_approfondie = QPushButton(self.frame_3)
        self.recherche_approfondie.setObjectName(u"recherche_approfondie")
        self.recherche_approfondie.setFont(font)
        self.recherche_approfondie.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.gridLayout_3.addWidget(self.recherche_approfondie, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(249, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.valider = QPushButton(self.frame_3)
        self.valider.setObjectName(u"valider")
        self.valider.setFont(font)
        self.valider.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.gridLayout_3.addWidget(self.valider, 0, 2, 1, 1)

        self.fermer = QPushButton(self.frame_3)
        self.fermer.setObjectName(u"fermer")
        self.fermer.setFont(font)
        self.fermer.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #ee2e31;\n"
"padding: 5px;\n"
"border: 2px solid #ee2e31;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #ee2e31;color: white;}\n"
"QPushButton:pressed{margin: 1px;}")

        self.gridLayout_3.addWidget(self.fermer, 0, 3, 1, 1)

        self.emballage_table = QTableWidget(self.frame_3)
        if (self.emballage_table.columnCount() < 9):
            self.emballage_table.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.emballage_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.emballage_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.emballage_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.emballage_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.emballage_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.emballage_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.emballage_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.emballage_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.emballage_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.emballage_table.setObjectName(u"emballage_table")
        self.emballage_table.setStyleSheet(u"background-color: white;\n"
"color: #52796f;\n"
"selection-background-color: #a2d2ff;\n"
"selection-color:#2f3e46;\n"
"border-radius: 10px;")
        self.emballage_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.emballage_table.setAlternatingRowColors(True)
        self.emballage_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.emballage_table.horizontalHeader().setStretchLastSection(True)
        self.emballage_table.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.emballage_table, 1, 0, 5, 3)

        self.verticalSpacer = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 3, 1, 1)

        self.nouveau = QPushButton(self.frame_3)
        self.nouveau.setObjectName(u"nouveau")
        self.nouveau.setFont(font)
        self.nouveau.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.gridLayout_3.addWidget(self.nouveau, 2, 3, 1, 1)

        self.modifier = QPushButton(self.frame_3)
        self.modifier.setObjectName(u"modifier")
        self.modifier.setFont(font)
        self.modifier.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.gridLayout_3.addWidget(self.modifier, 3, 3, 1, 1)

        self.supprimer = QPushButton(self.frame_3)
        self.supprimer.setObjectName(u"supprimer")
        self.supprimer.setFont(font)
        self.supprimer.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #ee2e31;\n"
"padding: 5px;\n"
"border: 2px solid #ee2e31;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #ee2e31;color: white;}\n"
"QPushButton:pressed{margin: 1px;}")

        self.gridLayout_3.addWidget(self.supprimer, 4, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 3, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"N\u00b0 Dossier", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Client", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Information G\u00e9n\u00e9rales", None))
        self.recherche_approfondie.setText(QCoreApplication.translate("Form", u"Recherche Approfondie", None))
        self.valider.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.fermer.setText(QCoreApplication.translate("Form", u"Fermer", None))
        ___qtablewidgetitem = self.emballage_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"N\u00b0", None));
        ___qtablewidgetitem1 = self.emballage_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"N\u00b0 Emballage", None));
        ___qtablewidgetitem2 = self.emballage_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Genre d'emballage", None));
        ___qtablewidgetitem3 = self.emballage_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Pieds", None));
        ___qtablewidgetitem4 = self.emballage_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Type d'emballage", None));
        ___qtablewidgetitem5 = self.emballage_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Date de livraison", None));
        ___qtablewidgetitem6 = self.emballage_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Date de Restitution", None));
        ___qtablewidgetitem7 = self.emballage_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"N\u00b0 Bon/ Facture Restitution", None));
        ___qtablewidgetitem8 = self.emballage_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Description", None));
        self.nouveau.setText(QCoreApplication.translate("Form", u"Nouveau", None))
        self.modifier.setText(QCoreApplication.translate("Form", u"Modifier", None))
        self.supprimer.setText(QCoreApplication.translate("Form", u"Supprimer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Suivi Emballages", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Grille de saisie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Grille de saisie (DSTR)", None))
    # retranslateUi

