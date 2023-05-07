# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowVPFZXd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.test_dossier_global import DossierGlobalWindow
from ui.test_facture_globale import FactureGlobalWindow
from ui.test_ressources_materielles import RessourcesMateriellesWindow
from ui.test_ressources_humaines import RessourcesHumainesWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(607, 342)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #2f3e46;\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.dossiers_2 = QPushButton(self.frame)
        self.dossiers_2.setObjectName(u"dossiers_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dossiers_2.setFont(font)
        self.dossiers_2.setStyleSheet(u"QPushButton {\n"
"background-color: #2f3e46;\n"
"color: white;\n"
"padding: 6px;\n"
"border: 2px solid #2f3e46;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #2f3e46;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout.addWidget(self.dossiers_2)

        self.factures_2 = QPushButton(self.frame)
        self.factures_2.setObjectName(u"factures_2")
        self.factures_2.setFont(font)
        self.factures_2.setStyleSheet(u"QPushButton {\n"
"background-color: #2f3e46;\n"
"color: white;\n"
"padding: 6px;\n"
"border: 2px solid #2f3e46;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #2f3e46;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout.addWidget(self.factures_2)

        self.res_humaines_2 = QPushButton(self.frame)
        self.res_humaines_2.setObjectName(u"res_humaines_2")
        self.res_humaines_2.setFont(font)
        self.res_humaines_2.setStyleSheet(u"QPushButton {\n"
"background-color: #2f3e46;\n"
"color: white;\n"
"padding: 6px;\n"
"border: 2px solid #2f3e46;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #2f3e46;}\n"
"QPushButton:pressed { margin: 1px; }\n"
"")

        self.verticalLayout.addWidget(self.res_humaines_2)

        self.res_materielles_2 = QPushButton(self.frame)
        self.res_materielles_2.setObjectName(u"res_materielles_2")
        self.res_materielles_2.setFont(font)
        self.res_materielles_2.setStyleSheet(u"QPushButton {\n"
"background-color: #2f3e46;\n"
"color: white;\n"
"padding: 6px;\n"
"border: 2px solid #2f3e46;\n"
"}\n"
"QPushButton:hover {background-color: white;color: #2f3e46;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.verticalLayout.addWidget(self.res_materielles_2)

        self.verticalSpacer = QSpacerItem(20, 205, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dossiers = DossierGlobalWindow()
        self.dossiers.setObjectName(u"dossiers")
        self.stackedWidget.addWidget(self.dossiers)
        self.factures = FactureGlobalWindow()
        self.factures.setObjectName(u"factures")
        self.stackedWidget.addWidget(self.factures)
        self.res_humaines = RessourcesHumainesWindow()
        self.res_humaines.setObjectName(u"res_humaines")
        self.stackedWidget.addWidget(self.res_humaines)
        self.res_materielles = RessourcesMateriellesWindow()
        self.res_materielles.setObjectName(u"res_materielles")
        self.stackedWidget.addWidget(self.res_materielles)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dossiers_2.setText(QCoreApplication.translate("MainWindow", u"Dossiers", None))
        self.factures_2.setText(QCoreApplication.translate("MainWindow", u"Factures", None))
        self.res_humaines_2.setText(QCoreApplication.translate("MainWindow", u"Ressources\n"
"humaines", None))
        self.res_materielles_2.setText(QCoreApplication.translate("MainWindow", u"Ressources\n"
"mat\u00e9rielles", None))
    # retranslateUi

