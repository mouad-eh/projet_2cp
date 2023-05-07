# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Grille_Saisie_1rjVOOe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# import PySide6.QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.navire_test2 import *
from auto_ui.ui_client import *
from ui.file_monnaie2 import MonnaieWindow
from ui.file_pays2 import PaysWindow
from ui.declarant import DeclarantWindow
from datetime import *
class Ui_Form(object):
    def __init__(self):
            self.form = QWidget()
            self.setupUi(self.form)
            self.tabmarchandises = []
            #app2 = PySide6.QtWidgets.QApplication()
            self.valider.clicked.connect(self.suivant)
            self.stackedWidget.setCurrentIndex(0)
            self.money = MonnaieWindow()
            self.country = PaysWindow()
            self.dec = DeclarantWindow()
           # self.form2 = QtWidgets.QWidget()
            self.widg_client = Ui_client()
            self.widg_navire = NavireWindow()
            self.money.ui.valider_monnaie.clicked.connect(self.validmoney)
            self.country.ui.valider.clicked.connect(self.valicountry)
            self.dec.ui.valider.clicked.connect(self.validdec)
            self.widg_navire.ui.valider_navire.clicked.connect(self.validnav)
            self.pushButton_7.clicked.connect(self.retour2)
            self.pushButton_21.clicked.connect(self.nouveau)
            self.Monnaie.clicked.connect(self.create_monnaie)
            self.pays.clicked.connect(self.create_pays)
            self.Declarant.clicked.connect(self.create_declarant)
            self.navire.clicked.connect(self.create_navire)
            self.client.clicked.connect(self.clt)
            self.widg_client.valider.clicked.connect(self.validclt)
            self.montant_droits_taxes.textChanged.connect(self.change)
            self.pushButton_8.clicked.connect(self.validerfinal)
            self.lineEdit.textChanged.connect(self.couleurnumdossier)
            self.line_client.textChanged.connect(self.couleurclient)
            self.num_facture_3.textChanged.connect(self.couleurfacture)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(1786, 939)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.gridLayout_87 = QGridLayout(self.stackedWidgetPage1)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.gridLayout_87.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.stackedWidgetPage1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1762, 854))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"background-color: white")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1739, 862))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_7 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_20.addWidget(self.label_15, 0, 0, 1, 1)

        self.num_titre_transport = QLineEdit(self.frame_7)
        self.num_titre_transport.setObjectName(u"num_titre_transport")
        self.num_titre_transport.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                               "border-radius:10px;\n"
                                               "padding: 3px;\n"
                                               "background-color: white;\n"
                                               "color: #2f3e46;\n"
                                               "")

        self.gridLayout_20.addWidget(self.num_titre_transport, 1, 0, 1, 1)

        self.horizontalLayout_15.addLayout(self.gridLayout_20)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_15, 1, 2, 1, 1)

        self.line_navire = QLineEdit(self.frame_7)
        self.line_navire.setObjectName(u"line_navire")
        self.line_navire.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                       "border-radius:10px;\n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"
                                       "color: #2f3e46;\n"
                                       "")
        self.line_navire.setReadOnly(True)

        self.gridLayout_22.addWidget(self.line_navire, 1, 0, 1, 1)

        self.navire = QPushButton(self.frame_7)
        self.navire.setObjectName(u"navire")
        sizePolicy.setHeightForWidth(self.navire.sizePolicy().hasHeightForWidth())
        self.navire.setSizePolicy(sizePolicy)
        self.navire.setStyleSheet(u"\n"
                                  "QPushButton {\n"
                                  "background-color: white;\n"
                                  "color: #2f3e46;;\n"
                                  "padding: 6px;\n"
                                  "border: 2px solid #2f3e46;;\n"
                                  "border-radius: 10px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {background-color: #2f3e46;;color: white;}\n"
                                  "QPushButton:pressed { margin: 1px; }\n"
                                  "")

        self.gridLayout_22.addWidget(self.navire, 1, 1, 1, 1)

        self.gridLayout_19.addLayout(self.gridLayout_22, 1, 2, 1, 1)

        self.compagnie_transport = QLineEdit(self.frame_7)
        self.compagnie_transport.setObjectName(u"compagnie_transport")
        self.compagnie_transport.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                               "border-radius:10px;\n"
                                               "padding: 3px;\n"
                                               "background-color: white;\n"
                                               "color: #2f3e46;\n"
                                               "")

        self.gridLayout_19.addWidget(self.compagnie_transport, 1, 0, 1, 1)

        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: #2f3e46;\n"
                                    "\n"
                                    "")

        self.gridLayout_19.addWidget(self.label_18, 0, 2, 1, 1)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_19.addWidget(self.label_14, 0, 0, 1, 1)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.mode_transport = QLineEdit(self.frame_7)
        self.mode_transport.setObjectName(u"mode_transport")
        self.mode_transport.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"
                                          "color: #2f3e46;\n"
                                          "")

        self.gridLayout_24.addWidget(self.mode_transport, 1, 0, 1, 1)

        self.gridLayout_19.addLayout(self.gridLayout_24, 1, 1, 1, 1)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_19.addWidget(self.label_13, 0, 1, 1, 1)

        self.gridLayout_15.addLayout(self.gridLayout_19, 0, 0, 1, 1)

        self.horizontalLayout_15.addLayout(self.gridLayout_15)

        self.horizontalLayout_15.setStretch(1, 3)

        self.gridLayout_9.addLayout(self.horizontalLayout_15, 2, 0, 1, 1)

        self.line_2 = QFrame(self.frame_7)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_2, 9, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_26 = QLabel(self.frame_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_31.addWidget(self.label_26, 0, 0, 1, 1)

        self.bureau_douane = QLineEdit(self.frame_7)
        self.bureau_douane.setObjectName(u"bureau_douane")
        self.bureau_douane.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                         "border-radius:10px;\n"
                                         "padding: 3px;\n"
                                         "background-color: white;\n"
                                         "color: #2f3e46;\n"
                                         "")

        self.gridLayout_31.addWidget(self.bureau_douane, 1, 0, 1, 1)

        self.horizontalLayout_17.addLayout(self.gridLayout_31)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_36)

        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_32.addWidget(self.label_27, 0, 0, 1, 1)

        self.receveur_douanes = QLineEdit(self.frame_7)
        self.receveur_douanes.setObjectName(u"receveur_douanes")
        self.receveur_douanes.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                            "border-radius:10px;\n"
                                            "padding: 3px;\n"
                                            "background-color: white;\n"
                                            "color: #2f3e46;\n"
                                            "")

        self.gridLayout_32.addWidget(self.receveur_douanes, 1, 0, 1, 1)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_37, 1, 1, 1, 1)

        self.horizontalLayout_17.addLayout(self.gridLayout_32)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.label_28 = QLabel(self.frame_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_33.addWidget(self.label_28, 0, 0, 1, 1)

        self.num_gros = QLineEdit(self.frame_7)
        self.num_gros.setObjectName(u"num_gros")
        self.num_gros.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

        self.gridLayout_33.addWidget(self.num_gros, 1, 0, 1, 1)

        self.horizontalLayout_17.addLayout(self.gridLayout_33)

        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_62 = QLabel(self.frame_7)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_34.addWidget(self.label_62, 0, 0, 1, 1)

        self.num_article = QLineEdit(self.frame_7)
        self.num_article.setObjectName(u"num_article")
        self.num_article.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                       "border-radius:10px;\n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"
                                       "color: #2f3e46;\n"
                                       "")

        self.gridLayout_34.addWidget(self.num_article, 1, 0, 1, 1)

        self.horizontalLayout_17.addLayout(self.gridLayout_34)

        self.gridLayout_68 = QGridLayout()
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.label_63 = QLabel(self.frame_7)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_68.addWidget(self.label_63, 0, 0, 1, 1)

        self.num_bon_enlever = QLineEdit(self.frame_7)
        self.num_bon_enlever.setObjectName(u"num_bon_enlever")
        self.num_bon_enlever.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                           "border-radius:10px;\n"
                                           "padding: 3px;\n"
                                           "background-color: white;\n"
                                           "color: #2f3e46;\n"
                                           "")

        self.gridLayout_68.addWidget(self.num_bon_enlever, 1, 0, 1, 1)

        self.horizontalLayout_17.addLayout(self.gridLayout_68)

        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.label_64 = QLabel(self.frame_7)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_39.addWidget(self.label_64, 0, 0, 1, 1)

        self.SG = QLineEdit(self.frame_7)
        self.SG.setObjectName(u"SG")
        self.SG.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                              "border-radius:10px;\n"
                              "padding: 3px;\n"
                              "background-color: white;\n"
                              "color: #2f3e46;\n"
                              "")

        self.gridLayout_39.addWidget(self.SG, 1, 0, 1, 1)

        self.horizontalLayout_17.addLayout(self.gridLayout_39)

        self.horizontalLayout_17.setStretch(0, 2)
        self.horizontalLayout_17.setStretch(2, 3)
        self.horizontalLayout_17.setStretch(3, 1)
        self.horizontalLayout_17.setStretch(4, 1)
        self.horizontalLayout_17.setStretch(6, 1)

        self.gridLayout_9.addLayout(self.horizontalLayout_17, 5, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: #2f3e46;\n"
                                    "\n"
                                    "")

        self.gridLayout_26.addWidget(self.label_19, 0, 0, 1, 1)

        self.date_arrivee = QDateEdit(self.frame_7)
        self.date_arrivee.setObjectName(u"date_arrivee")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.date_arrivee.setFont(font)
        self.date_arrivee.setStyleSheet(u"border : 3px solid #52796f;\n"
                                        "\n"
                                        "padding: 3px;\n"
                                        "background-color: white;\n"
                                        "color: #2f3e46;\n"
                                        "")

        self.gridLayout_26.addWidget(self.date_arrivee, 1, 0, 1, 1)

        self.horizontalLayout_16.addLayout(self.gridLayout_26)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.datemain_levee = QDateEdit(self.frame_7)
        self.datemain_levee.setObjectName(u"datemain_levee")
        self.datemain_levee.setFont(font)
        self.datemain_levee.setStyleSheet(u"background-color: white;\n"
                                          "color: #2f3e46;\n"
                                          "padding: 3px;\n"
                                          "border : 3px solid #52796f;\n"
                                          "border-radius: 3px;\n"
                                          "")

        self.gridLayout_27.addWidget(self.datemain_levee, 1, 0, 1, 1)

        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_27.addWidget(self.label_20, 0, 0, 1, 1)

        self.horizontalLayout_16.addLayout(self.gridLayout_27)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.lieu_entreposage = QLineEdit(self.frame_7)
        self.lieu_entreposage.setObjectName(u"lieu_entreposage")
        self.lieu_entreposage.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                            "border-radius:10px;\n"
                                            "padding: 3px;\n"
                                            "background-color: white;\n"
                                            "color: #2f3e46;\n"
                                            "")

        self.gridLayout_30.addWidget(self.lieu_entreposage, 1, 0, 1, 1)

        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_30.addWidget(self.label_25, 0, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_20, 1, 1, 1, 1)

        self.horizontalLayout_16.addLayout(self.gridLayout_30)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(2, 4)

        self.gridLayout_9.addLayout(self.horizontalLayout_16, 3, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_9 = QPushButton(self.frame_7)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
                                        "background-color: white;\n"
                                        "color: #ee2e31;\n"
                                        "padding: 5px;\n"
                                        "border: 2px solid #ee2e31;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover {background-color: #ee2e31;color: white;}\n"
                                        "QPushButton:pressed{margin: 1px;}\n"
                                        "")

        self.horizontalLayout_19.addWidget(self.pushButton_9)

        self.valider = QPushButton(self.frame_7)
        self.valider.setObjectName(u"valider")
        sizePolicy.setHeightForWidth(self.valider.sizePolicy().hasHeightForWidth())
        self.valider.setSizePolicy(sizePolicy)
        self.valider.setStyleSheet(u"\n"
                                   "QPushButton {\n"
                                   "background-color: white;\n"
                                   "color: #3bb273;\n"
                                   "padding: 6px;\n"
                                   "border: 2px solid #3bb273;\n"
                                   "border-radius: 10px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                   "QPushButton:pressed { margin: 1px; }\n"
                                   "")

        self.horizontalLayout_19.addWidget(self.valider)

        self.gridLayout_9.addLayout(self.horizontalLayout_19, 11, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.label_46 = QLabel(self.frame_7)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_43.addWidget(self.label_46, 0, 0, 1, 1)

        self.date_acquittement_taxes = QDateEdit(self.frame_7)
        self.date_acquittement_taxes.setObjectName(u"date_acquittement_taxes")
        self.date_acquittement_taxes.setFont(font)
        self.date_acquittement_taxes.setStyleSheet(u"background-color: white;\n"
                                                   "color: #2f3e46;\n"
                                                   "padding: 3px;\n"
                                                   "border : 3px solid #52796f;\n"
                                                   "border-radius: 3px;\n"
                                                   "")

        self.gridLayout_43.addWidget(self.date_acquittement_taxes, 1, 0, 1, 1)

        self.horizontalLayout_13.addLayout(self.gridLayout_43)

        self.gridLayout_44 = QGridLayout()
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_44.addItem(self.horizontalSpacer_28, 1, 2, 1, 1)

        self.num_quittance_douane = QLineEdit(self.frame_7)
        self.num_quittance_douane.setObjectName(u"num_quittance_douane")
        self.num_quittance_douane.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                                "border-radius:10px;\n"
                                                "padding: 3px;\n"
                                                "background-color: white;\n"
                                                "color: #2f3e46;\n"
                                                "")

        self.gridLayout_44.addWidget(self.num_quittance_douane, 1, 0, 1, 1)

        self.label_47 = QLabel(self.frame_7)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_44.addWidget(self.label_47, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.parc_a_vide = QLineEdit(self.frame_7)
        self.parc_a_vide.setObjectName(u"parc_a_vide")
        self.parc_a_vide.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                       "border-radius:10px;\n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"
                                       "color: #2f3e46;\n"
                                       "")

        self.verticalLayout_3.addWidget(self.parc_a_vide)

        self.gridLayout_44.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.label_57 = QLabel(self.frame_7)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_44.addWidget(self.label_57, 0, 1, 1, 1)

        self.horizontalLayout_13.addLayout(self.gridLayout_44)

        self.gridLayout_9.addLayout(self.horizontalLayout_13, 8, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout_53 = QGridLayout()
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.label_54 = QLabel(self.frame_8)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_53.addWidget(self.label_54, 0, 1, 1, 1)

        self.date_livraison = QDateEdit(self.frame_8)
        self.date_livraison.setObjectName(u"date_livraison")
        self.date_livraison.setFont(font)
        self.date_livraison.setStyleSheet(u"background-color: white;\n"
                                          "color: #2f3e46;\n"
                                          "padding: 3px;\n"
                                          "border : 3px solid #52796f;\n"
                                          "border-radius: 3px;\n"
                                          "")

        self.gridLayout_53.addWidget(self.date_livraison, 1, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_12, 1, 0, 1, 1)

        self.horizontalLayout_9.addLayout(self.gridLayout_53)

        self.gridLayout_56 = QGridLayout()
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.label_56 = QLabel(self.frame_8)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_56.addWidget(self.label_56, 0, 0, 1, 1)

        self.lieu_livraison = QLineEdit(self.frame_8)
        self.lieu_livraison.setObjectName(u"lieu_livraison")
        self.lieu_livraison.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"
                                          "color: #2f3e46;\n"
                                          "")

        self.gridLayout_56.addWidget(self.lieu_livraison, 1, 0, 1, 1)

        self.horizontalLayout_9.addLayout(self.gridLayout_56)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_29)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)

        self.gridLayout_10.addLayout(self.horizontalLayout_9, 0, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 145, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_58 = QLabel(self.frame_8)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.verticalLayout_4.addWidget(self.label_58)

        self.observation_statique = QTextEdit(self.frame_8)
        self.observation_statique.setObjectName(u"observation_statique")

        self.verticalLayout_4.addWidget(self.observation_statique)

        self.gridLayout_10.addLayout(self.verticalLayout_4, 1, 1, 4, 1)

        self.gridLayout_66 = QGridLayout()
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.Declarant = QPushButton(self.frame_8)
        self.Declarant.setObjectName(u"Declarant")
        sizePolicy.setHeightForWidth(self.Declarant.sizePolicy().hasHeightForWidth())
        self.Declarant.setSizePolicy(sizePolicy)
        self.Declarant.setStyleSheet(u"\n"
                                     "QPushButton {\n"
                                     "background-color: white;\n"
                                     "color: #2f3e46;;\n"
                                     "padding: 6px;\n"
                                     "border: 2px solid #2f3e46;;\n"
                                     "border-radius: 10px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {background-color: #2f3e46;;color: white;}\n"
                                     "QPushButton:pressed { margin: 1px; }\n"
                                     "")

        self.gridLayout_66.addWidget(self.Declarant, 1, 1, 1, 1)

        self.line_declarant = QLineEdit(self.frame_8)
        self.line_declarant.setObjectName(u"line_declarant")
        self.line_declarant.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"
                                          "color: #2f3e46;\n"
                                          "")
        self.line_declarant.setReadOnly(True)

        self.gridLayout_66.addWidget(self.line_declarant, 1, 0, 1, 1)

        self.label_59 = QLabel(self.frame_8)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_66.addWidget(self.label_59, 0, 0, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_66.addItem(self.horizontalSpacer_33, 1, 2, 1, 1)

        self.gridLayout_10.addLayout(self.gridLayout_66, 2, 0, 1, 1)

        self.gridLayout_67 = QGridLayout()
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.label_60 = QLabel(self.frame_8)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_67.addWidget(self.label_60, 0, 0, 1, 1)

        self.observation_dynamique = QLineEdit(self.frame_8)
        self.observation_dynamique.setObjectName(u"observation_dynamique")
        self.observation_dynamique.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                                 "border-radius:10px;\n"
                                                 "padding: 3px;\n"
                                                 "background-color: white;\n"
                                                 "color: #2f3e46;\n"
                                                 "")

        self.gridLayout_67.addWidget(self.observation_dynamique, 1, 0, 1, 1)

        self.gridLayout_10.addLayout(self.gridLayout_67, 3, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 144, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_7, 4, 0, 1, 1)

        self.gridLayout_9.addWidget(self.frame_8, 10, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(40)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.horizontalLayout_12.addWidget(self.label_17)

        self.ref_client_dossier = QLineEdit(self.frame_7)
        self.ref_client_dossier.setObjectName(u"ref_client_dossier")
        self.ref_client_dossier.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                              "border-radius:10px;\n"
                                              "padding: 3px;\n"
                                              "background-color: white;\n"
                                              "color: #2f3e46;\n"
                                              "")

        self.horizontalLayout_12.addWidget(self.ref_client_dossier)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_12)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.nature_dossier = QLineEdit(self.frame_7)
        self.nature_dossier.setObjectName(u"nature_dossier")
        self.nature_dossier.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"
                                          "color: #2f3e46;\n"
                                          "")

        self.horizontalLayout_10.addWidget(self.nature_dossier)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_38)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")

        self.horizontalLayout_10.addLayout(self.gridLayout_23)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_61 = QLabel(self.frame_7)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"color: #2f3e46;\n"
                                    "\n"
                                    "")

        self.horizontalLayout_14.addWidget(self.label_61)

        self.situation_dossier = QLineEdit(self.frame_7)
        self.situation_dossier.setObjectName(u"situation_dossier")
        self.situation_dossier.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                             "border-radius:10px;\n"
                                             "padding: 3px;\n"
                                             "background-color: white;\n"
                                             "color: #2f3e46;\n"
                                             "")

        self.horizontalLayout_14.addWidget(self.situation_dossier)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_39)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_10.setStretch(0, 2)
        self.horizontalLayout_10.setStretch(5, 2)

        self.gridLayout_9.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.line = QFrame(self.frame_7)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line, 4, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.gridLayout_40 = QGridLayout()
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.label_65 = QLabel(self.frame_7)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_40.addWidget(self.label_65, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_40.addWidget(self.label_7, 0, 1, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_31, 1, 5, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_32, 1, 4, 1, 1)

        self.montant_droits_taxes = QLineEdit(self.frame_7)
        self.montant_droits_taxes.setObjectName(u"montant_droits_taxes")
        self.montant_droits_taxes.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                                "border-radius:10px;\n"
                                                "padding: 3px;\n"
                                                "background-color: white;\n"
                                                "color: #2f3e46;\n"
                                                "")

        self.gridLayout_40.addWidget(self.montant_droits_taxes, 1, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_30, 1, 7, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_27, 1, 6, 1, 1)

        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.valeur_da = QLineEdit(self.frame_7)
        self.valeur_da.setObjectName(u"valeur_da")
        self.valeur_da.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                     "border-radius:10px;\n"
                                     "padding: 3px;\n"
                                     "background-color: white;\n"
                                     "color: #2f3e46;\n"
                                     "")
        self.valeur_da.setReadOnly(True)

        self.gridLayout_38.addWidget(self.valeur_da, 1, 0, 1, 1)

        self.gridLayout_40.addLayout(self.gridLayout_38, 1, 3, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mine_monnaie = QLineEdit(self.frame_7)
        self.mine_monnaie.setObjectName(u"mine_monnaie")
        self.mine_monnaie.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                        "border-radius:10px;\n"
                                        "padding: 3px;\n"
                                        "background-color: white;\n"
                                        "color: #2f3e46;\n"
                                        "")
        self.mine_monnaie.setReadOnly(True)

        self.verticalLayout.addWidget(self.mine_monnaie)

        self.gridLayout_40.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.Monnaie = QPushButton(self.frame_7)
        self.Monnaie.setObjectName(u"Monnaie")
        sizePolicy.setHeightForWidth(self.Monnaie.sizePolicy().hasHeightForWidth())
        self.Monnaie.setSizePolicy(sizePolicy)
        self.Monnaie.setStyleSheet(u"\n"
                                   "QPushButton {\n"
                                   "background-color: white;\n"
                                   "color: #2f3e46;;\n"
                                   "padding: 6px;\n"
                                   "border: 2px solid #2f3e46;;\n"
                                   "border-radius: 10px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {background-color: #2f3e46;;color: white;}\n"
                                   "QPushButton:pressed { margin: 1px; }\n"
                                   "")

        self.gridLayout_40.addWidget(self.Monnaie, 1, 2, 1, 1)

        self.label_45 = QLabel(self.frame_7)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_40.addWidget(self.label_45, 0, 3, 1, 1)

        self.horizontalLayout_18.addLayout(self.gridLayout_40)

        self.gridLayout_51 = QGridLayout()
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_48 = QLabel(self.frame_7)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_51.addWidget(self.label_48, 0, 0, 1, 1)

        self.date_bon_enlever = QDateEdit(self.frame_7)
        self.date_bon_enlever.setObjectName(u"date_bon_enlever")
        self.date_bon_enlever.setFont(font)
        self.date_bon_enlever.setStyleSheet(u"background-color: white;\n"
                                            "color: #2f3e46;\n"
                                            "padding: 3px;\n"
                                            "border : 3px solid #52796f;\n"
                                            "border-radius: 3px;\n"
                                            "")

        self.gridLayout_51.addWidget(self.date_bon_enlever, 1, 0, 1, 1)

        self.horizontalLayout_18.addLayout(self.gridLayout_51)

        self.gridLayout_41 = QGridLayout()
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.label_66 = QLabel(self.frame_7)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_41.addWidget(self.label_66, 0, 0, 1, 1)

        self.date_visite_douane = QDateEdit(self.frame_7)
        self.date_visite_douane.setObjectName(u"date_visite_douane")
        self.date_visite_douane.setFont(font)
        self.date_visite_douane.setStyleSheet(u"background-color: white;\n"
                                              "color: #2f3e46;\n"
                                              "padding: 3px;\n"
                                              "border : 3px solid #52796f;\n"
                                              "border-radius: 3px;\n"
                                              "")

        self.gridLayout_41.addWidget(self.date_visite_douane, 1, 0, 1, 1)

        self.horizontalLayout_18.addLayout(self.gridLayout_41)

        self.gridLayout_42 = QGridLayout()
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.date_liquidation = QDateEdit(self.frame_7)
        self.date_liquidation.setObjectName(u"date_liquidation")
        self.date_liquidation.setFont(font)
        self.date_liquidation.setStyleSheet(u"background-color: white;\n"
                                            "color: #2f3e46;\n"
                                            "padding: 3px;\n"
                                            "border : 3px solid #52796f;\n"
                                            "border-radius: 3px;\n"
                                            "")

        self.gridLayout_42.addWidget(self.date_liquidation, 1, 0, 1, 1)

        self.label_67 = QLabel(self.frame_7)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_42.addWidget(self.label_67, 0, 0, 1, 1)

        self.horizontalLayout_18.addLayout(self.gridLayout_42)

        self.gridLayout_69 = QGridLayout()
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.label_68 = QLabel(self.frame_7)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_69.addWidget(self.label_68, 0, 0, 1, 1)

        self.date_cheque = QDateEdit(self.frame_7)
        self.date_cheque.setObjectName(u"date_cheque")
        self.date_cheque.setFont(font)
        self.date_cheque.setStyleSheet(u"background-color: white;\n"
                                       "color: #2f3e46;\n"
                                       "padding: 3px;\n"
                                       "border : 3px solid #52796f;\n"
                                       "border-radius: 2px;\n"
                                       "\n"
                                       "")

        self.gridLayout_69.addWidget(self.date_cheque, 1, 0, 1, 1)

        self.horizontalLayout_18.addLayout(self.gridLayout_69)

        self.gridLayout_9.addLayout(self.horizontalLayout_18, 7, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setVerticalSpacing(12)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: #2f3e46;\n"
                                   "\n"
                                   "")

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1)

        self.date_recu = QDateEdit(self.frame_7)
        self.date_recu.setObjectName(u"date_recu")
        self.date_recu.setFont(font)
        self.date_recu.setStyleSheet(u"background-color: white;\n"
                                     "color: #2f3e46;\n"
                                     "padding: 3px;\n"
                                     "border : 3px solid #52796f;\n"
                                     "border-radius: 3px;\n"
                                     "")

        self.gridLayout_11.addWidget(self.date_recu, 1, 0, 1, 1)

        self.horizontalLayout_20.addLayout(self.gridLayout_11)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.a = QLineEdit(self.frame_7)
        self.a.setObjectName(u"a")
        self.a.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                             "border-radius:10px;\n"
                             "padding: 3px;\n"
                             "background-color: white;\n"
                             "color: #2f3e46;\n"
                             "")

        self.gridLayout_12.addWidget(self.a, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: #2f3e46;\n"
                                   "\n"
                                   "")

        self.gridLayout_12.addWidget(self.label_6, 0, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_14, 1, 1, 1, 1)

        self.horizontalLayout_20.addLayout(self.gridLayout_12)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #2f3e46;\n"
                                   "")

        self.gridLayout_14.addWidget(self.label_8, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.num_facture_3 = QLineEdit(self.frame_7)
        self.num_facture_3.setObjectName(u"num_facture_3")
        self.num_facture_3.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                         "border-radius:10px;\n"
                                         "padding: 3px;\n"
                                         "background-color: white;\n"
                                         "color: #2f3e46;\n"
                                         "")
        self.num_facture_3.setReadOnly(False)

        self.gridLayout_14.addWidget(self.num_facture_3, 1, 0, 1, 1)

        self.horizontalLayout_20.addLayout(self.gridLayout_14)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 1)
        self.horizontalLayout_20.setStretch(2, 2)

        self.gridLayout_9.addLayout(self.horizontalLayout_20, 1, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_42 = QLabel(self.frame_7)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_35.addWidget(self.label_42, 0, 0, 1, 1)

        self.date_echange = QDateEdit(self.frame_7)
        self.date_echange.setObjectName(u"date_echange")
        self.date_echange.setFont(font)
        self.date_echange.setStyleSheet(u"background-color: white;\n"
                                        "color: #2f3e46;\n"
                                        "padding: 3px;\n"
                                        "border : 3px solid #52796f;\n"
                                        "border-radius: 3px;\n"
                                        "")

        self.gridLayout_35.addWidget(self.date_echange, 1, 0, 1, 1)

        self.horizontalLayout_11.addLayout(self.gridLayout_35)

        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_43 = QLabel(self.frame_7)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_36.addWidget(self.label_43, 0, 0, 1, 1)

        self.date_declaration = QDateEdit(self.frame_7)
        self.date_declaration.setObjectName(u"date_declaration")
        self.date_declaration.setFont(font)
        self.date_declaration.setStyleSheet(u"background-color: white;\n"
                                            "color: #2f3e46;\n"
                                            "padding: 3px;\n"
                                            "border : 3px solid #52796f;\n"
                                            "border-radius: 3px;\n"
                                            "\n"
                                            "")

        self.gridLayout_36.addWidget(self.date_declaration, 1, 0, 1, 1)

        self.horizontalLayout_11.addLayout(self.gridLayout_36)

        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.num_declaration = QLineEdit(self.frame_7)
        self.num_declaration.setObjectName(u"num_declaration")
        self.num_declaration.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                           "border-radius:10px;\n"
                                           "padding: 3px;\n"
                                           "background-color: white;\n"
                                           "color: #2f3e46;\n"
                                           "")

        self.gridLayout_37.addWidget(self.num_declaration, 1, 0, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_34, 1, 2, 1, 1)

        self.label_44 = QLabel(self.frame_7)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_37.addWidget(self.label_44, 0, 0, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_35, 1, 1, 1, 1)

        self.horizontalLayout_11.addLayout(self.gridLayout_37)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 2)

        self.gridLayout_9.addLayout(self.horizontalLayout_11, 6, 0, 1, 1)

        self.gridLayout_8.addWidget(self.frame_7, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_7.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_87.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.gridLayout_16 = QGridLayout(self.stackedWidgetPage2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.stackedWidgetPage2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1762, 854))
        self.gridLayout_25 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: white;\n"
                                    "border-radius: 10px ;\n"
                                    "\n"
                                    "")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_10)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_10)

        self.pushButton_7 = QPushButton(self.frame_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
                                        "background-color: white;\n"
                                        "color: #ee2e31;\n"
                                        "padding: 5px;\n"
                                        "border: 2px solid #ee2e31;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover {background-color: #ee2e31;color: white;}\n"
                                        "QPushButton:pressed{margin: 1px;}\n"
                                        "")

        self.horizontalLayout_38.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
                                        "background-color: white;\n"
                                        "color: #3bb273;\n"
                                        "padding: 6px;\n"
                                        "border: 2px solid #3bb273;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                        "QPushButton:pressed { margin: 1px; }")

        self.horizontalLayout_38.addWidget(self.pushButton_8)

        self.gridLayout_17.addLayout(self.horizontalLayout_38, 3, 0, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.gridLayout_88 = QGridLayout()
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.label_49 = QLabel(self.frame_10)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"color: #fffff\n"
                                    "\n"
                                    "")

        self.gridLayout_88.addWidget(self.label_49, 0, 0, 1, 1)

        self.gridLayout_89 = QGridLayout()
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.gridLayout_89.setHorizontalSpacing(6)
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_89.addItem(self.horizontalSpacer_25, 0, 5, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_89.addItem(self.horizontalSpacer_24, 0, 3, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_89.addItem(self.horizontalSpacer_26, 0, 2, 1, 1)

        self.pays_fournisseur = QLineEdit(self.frame_10)
        self.pays_fournisseur.setObjectName(u"pays_fournisseur")
        self.pays_fournisseur.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                            "border-radius:10px;\n"
                                            "padding: 3px;\n"
                                            "background-color: white;\n"
                                            "color: #2f3e46;\n"
                                            "")
        self.pays_fournisseur.setReadOnly(True)

        self.gridLayout_89.addWidget(self.pays_fournisseur, 0, 0, 1, 1)

        self.pays = QPushButton(self.frame_10)
        self.pays.setObjectName(u"pays")
        sizePolicy.setHeightForWidth(self.pays.sizePolicy().hasHeightForWidth())
        self.pays.setSizePolicy(sizePolicy)
        self.pays.setStyleSheet(u"\n"
                                "QPushButton {\n"
                                "background-color: white;\n"
                                "color: #2f3e46;;\n"
                                "padding: 6px;\n"
                                "border: 2px solid #2f3e46;;\n"
                                "border-radius: 10px;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {background-color: #2f3e46;;color: white;}\n"
                                "QPushButton:pressed { margin: 1px; }\n"
                                "")

        self.gridLayout_89.addWidget(self.pays, 0, 1, 1, 1)

        self.gridLayout_89.setColumnStretch(0, 1)

        self.gridLayout_88.addLayout(self.gridLayout_89, 1, 0, 1, 1)

        self.horizontalLayout_35.addLayout(self.gridLayout_88)

        self.gridLayout_90 = QGridLayout()
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.Fournisseur = QPushButton(self.frame_10)
        self.Fournisseur.setObjectName(u"Fournisseur")
        sizePolicy.setHeightForWidth(self.Fournisseur.sizePolicy().hasHeightForWidth())
        self.Fournisseur.setSizePolicy(sizePolicy)
        self.Fournisseur.setStyleSheet(u"\n"
                                       "QPushButton {\n"
                                       "background-color: white;\n"
                                       "color: #2f3e46;;\n"
                                       "padding: 6px;\n"
                                       "border: 2px solid #2f3e46;;\n"
                                       "border-radius: 10px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {background-color: #2f3e46;;color: white;}\n"
                                       "QPushButton:pressed { margin: 1px; }\n"
                                       "")

        self.gridLayout_13.addWidget(self.Fournisseur, 1, 3, 1, 1)

        self.label_2 = QLabel(self.frame_10)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_13.addWidget(self.label_2, 0, 0, 1, 1)

        self.fournisseur = QLineEdit(self.frame_10)
        self.fournisseur.setObjectName(u"fournisseur")
        self.fournisseur.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                       "border-radius:10px;\n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"
                                       "color: #2f3e46;\n"
                                       "")
        self.fournisseur.setReadOnly(True)

        self.gridLayout_13.addWidget(self.fournisseur, 1, 0, 1, 1)

        self.gridLayout_90.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.horizontalLayout_35.addLayout(self.gridLayout_90)

        self.gridLayout_91 = QGridLayout()
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.gridLayout_93 = QGridLayout()
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.lieu_de_transfert = QLineEdit(self.frame_10)
        self.lieu_de_transfert.setObjectName(u"lieu_de_transfert")
        self.lieu_de_transfert.setFont(font)
        self.lieu_de_transfert.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                             "border-radius:10px;\n"
                                             "padding: 3px;\n"
                                             "background-color: white;\n"
                                             "color: #2f3e46;\n"
                                             "")

        self.gridLayout_93.addWidget(self.lieu_de_transfert, 1, 0, 1, 1)

        self.label_105 = QLabel(self.frame_10)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setStyleSheet(u"color: #fffff\n"
                                     "\n"
                                     "")

        self.gridLayout_93.addWidget(self.label_105, 0, 0, 1, 1)

        self.gridLayout_91.addLayout(self.gridLayout_93, 0, 0, 1, 1)

        self.horizontalLayout_35.addLayout(self.gridLayout_91)

        self.horizontalSpacer_18 = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_18)

        self.horizontalLayout_35.setStretch(0, 2)
        self.horizontalLayout_35.setStretch(1, 2)
        self.horizontalLayout_35.setStretch(2, 3)

        self.gridLayout_17.addLayout(self.horizontalLayout_35, 0, 0, 1, 1)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.gridLayout_92 = QGridLayout()
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.gridLayout_59 = QGridLayout()
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_73 = QGridLayout()
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.poids_net = QLineEdit(self.frame_10)
        self.poids_net.setObjectName(u"poids_net")
        self.poids_net.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                     "border-radius:10px;\n"
                                     "padding: 3px;\n"
                                     "background-color: white;\n"
                                     "color: #2f3e46;\n"
                                     "")

        self.gridLayout_73.addWidget(self.poids_net, 1, 0, 1, 1)

        self.gridLayout_59.addLayout(self.gridLayout_73, 1, 3, 1, 1)

        self.label_53 = QLabel(self.frame_10)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"color: #fffff\n"
                                    "")

        self.gridLayout_59.addWidget(self.label_53, 0, 0, 1, 1)

        self.label_51 = QLabel(self.frame_10)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"color: #fffff\n"
                                    "\n"
                                    "")

        self.gridLayout_59.addWidget(self.label_51, 0, 1, 1, 1)

        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: #2f3e46;\n"
                                    "")

        self.gridLayout_59.addWidget(self.label_16, 0, 3, 1, 1)

        self.gridLayout_58 = QGridLayout()
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.poids_brut = QLineEdit(self.frame_10)
        self.poids_brut.setObjectName(u"poids_brut")
        self.poids_brut.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                      "border-radius:10px;\n"
                                      "padding: 3px;\n"
                                      "background-color: white;\n"
                                      "color: #2f3e46;\n"
                                      "")
        self.poids_brut.setReadOnly(False)

        self.gridLayout_58.addWidget(self.poids_brut, 0, 0, 1, 1)

        self.gridLayout_59.addLayout(self.gridLayout_58, 1, 2, 1, 1)

        self.gridLayout_57 = QGridLayout()
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.nbr_colis = QLineEdit(self.frame_10)
        self.nbr_colis.setObjectName(u"nbr_colis")
        self.nbr_colis.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                     "border-radius:10px;\n"
                                     "padding: 3px;\n"
                                     "background-color: white;\n"
                                     "color: #2f3e46;\n"
                                     "")
        self.nbr_colis.setReadOnly(False)

        self.gridLayout_57.addWidget(self.nbr_colis, 1, 0, 1, 1)

        self.gridLayout_59.addLayout(self.gridLayout_57, 1, 1, 1, 1)

        self.label_52 = QLabel(self.frame_10)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"color: #fffff\n"
                                    "")

        self.gridLayout_59.addWidget(self.label_52, 0, 2, 1, 1)

        self.designation_marchandise = QLineEdit(self.frame_10)
        self.designation_marchandise.setObjectName(u"designation_marchandise")
        self.designation_marchandise.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                                   "border-radius:10px;\n"
                                                   "padding: 3px;\n"
                                                   "background-color: white;\n"
                                                   "color: #2f3e46;\n"
                                                   "")
        self.designation_marchandise.setReadOnly(False)

        self.gridLayout_59.addWidget(self.designation_marchandise, 1, 0, 1, 1)

        self.gridLayout_92.addLayout(self.gridLayout_59, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.nature_marchandise = QLineEdit(self.frame_10)
        self.nature_marchandise.setObjectName(u"nature_marchandise")
        self.nature_marchandise.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                              "border-radius:10px;\n"
                                              "padding: 3px;\n"
                                              "background-color: white;\n"
                                              "color: #2f3e46;\n"
                                              "")
        self.nature_marchandise.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.nature_marchandise)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_19)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_17)

        self.gridLayout_92.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.label_104 = QLabel(self.frame_10)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setStyleSheet(u"color: #fffff\n"
                                     "")

        self.gridLayout_92.addWidget(self.label_104, 2, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_92.addItem(self.horizontalSpacer_16, 3, 1, 1, 1)

        self.Pieces_jointes = QLineEdit(self.frame_10)
        self.Pieces_jointes.setObjectName(u"Pieces_jointes")
        self.Pieces_jointes.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"
                                          "color: #2f3e46;\n"
                                          "")
        self.Pieces_jointes.setReadOnly(False)

        self.gridLayout_92.addWidget(self.Pieces_jointes, 3, 0, 1, 1)

        self.horizontalLayout_36.addLayout(self.gridLayout_92)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_21)

        self.horizontalLayout_36.setStretch(0, 4)

        self.gridLayout_17.addLayout(self.horizontalLayout_36, 1, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalSpacer_5 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_5, 2, 2, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_22, 1, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_6, 0, 2, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(26, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_23, 1, 3, 1, 1)

        self.tableau_marchandise = QTableWidget(self.frame_10)
        if (self.tableau_marchandise.columnCount() < 5):
            self.tableau_marchandise.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableau_marchandise.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableau_marchandise.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableau_marchandise.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableau_marchandise.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableau_marchandise.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableau_marchandise.setObjectName(u"tableau_marchandise")
        self.tableau_marchandise.setStyleSheet(u"border : 0px solid #2f3e46;\n"
                                               "border-radius:0px;\n"
                                               "background-color: white\n"
                                               ";\n"
                                               "color: #fffff;\n"
                                               "selection-background-color:#2f3e46; ;\n"
                                               "selection-color : white;\n"
                                               "border-radius: 8px;")
        self.tableau_marchandise.setAlternatingRowColors(True)
        self.tableau_marchandise.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableau_marchandise.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableau_marchandise.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_18.addWidget(self.tableau_marchandise, 0, 0, 3, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_21 = QPushButton(self.frame_10)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setStyleSheet(u"QPushButton {\n"
                                         "background-color: white;\n"
                                         "color: #3bb273;\n"
                                         "padding: 6px;\n"
                                         "border: 2px solid #3bb273;\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                         "QPushButton:pressed { margin: 1px; }\n"
                                         "\n"
                                         "")

        self.verticalLayout_12.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame_10)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setStyleSheet(u"QPushButton {\n"
                                         "background-color: white;\n"
                                         "color: #3bb273;\n"
                                         "padding: 6px;\n"
                                         "border: 2px solid #3bb273;\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                         "QPushButton:pressed { margin: 1px; }")

        self.verticalLayout_12.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.frame_10)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setStyleSheet(u"QPushButton {\n"
                                         "background-color: white;\n"
                                         "color: #ee2e31;\n"
                                         "padding: 5px;\n"
                                         "border: 2px solid #ee2e31;\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover {background-color: #ee2e31;color: white;}\n"
                                         "QPushButton:pressed{margin: 1px;}\n"
                                         "")

        self.verticalLayout_12.addWidget(self.pushButton_23)

        self.gridLayout_18.addLayout(self.verticalLayout_12, 1, 2, 1, 1)

        self.gridLayout_18.setColumnStretch(0, 4)

        self.gridLayout_17.addLayout(self.gridLayout_18, 2, 0, 1, 1)

        self.gridLayout_25.addWidget(self.frame_10, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_16.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage2)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #2f3e46;\n"
                                   "color: white;\n"
                                   "")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: white")

        self.horizontalLayout.addWidget(self.label_9)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color:rgba(0,0,0,0) ;\n"
                                   "color:rgba(255,255,255,255)")

        self.horizontalLayout.addWidget(self.label_4)

        self.line_client = QLineEdit(self.frame_2)
        self.line_client.setObjectName(u"line_client")
        self.line_client.setFont(font)
        self.line_client.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                       "border-radius:10px;\n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"
                                       "color: #2f3e46;\n"
                                       "")
        self.line_client.setReadOnly(True)

        self.horizontalLayout.addWidget(self.line_client)

        self.client = QPushButton(self.frame_2)
        self.client.setObjectName(u"client")
        sizePolicy.setHeightForWidth(self.client.sizePolicy().hasHeightForWidth())
        self.client.setSizePolicy(sizePolicy)
        self.client.setStyleSheet(u"\n"
                                  "QPushButton {\n"
                                  "background-color: white;\n"
                                  "color: #2f3e46;;\n"
                                  "padding: 6px;\n"
                                  "border: 2px solid #2f3e46;;\n"
                                  "border-radius: 10px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {background-color: #2f3e46;;color: white;}\n"
                                  "QPushButton:pressed { margin: 1px; }\n"
                                  "")

        self.horizontalLayout.addWidget(self.client)

        self.horizontalSpacer = QSpacerItem(48, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)
        # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"dossier", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"  N\u00b0 Titre de transport ", None))
        self.navire.setText(QCoreApplication.translate("Form", u"       navire       ", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"  Navire ", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"  Compagnie de transport ", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"  Mode du transport ", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"  Bureau de Douane ", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"  Receveur des Douanes", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"  N\u00b0 Gros ", None))
        self.label_62.setText(QCoreApplication.translate("Form", u"  N\u00b0 Article ", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"  N\u00b0  Bon \u00e0 enlever ", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"  S/G ", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"    Date d'Arriv\u00e9e ", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"  Date Main Lev\u00e9e ", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"  Lieu d'entreposage ", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"retour en arri\u00e8re", None))
        self.valider.setText(QCoreApplication.translate("Form", u"valider", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"  Date Acquittement Droits Taxes ", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"  N\u00b0  Quittance Douane ", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"  Parc \u00e0 Vide ", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"  Date de Livraison ", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"  Lieu de Livraison ", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"  Observation Statique ", None))
        self.Declarant.setText(QCoreApplication.translate("Form", u"    D\u00e9clarant     ", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"  D\u00e9clarant ", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"  Observation Dynamique ", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"  R\u00e9f\u00e9rence Client du Dossier ", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"  Nature du dossier ", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"  Situation du Dossier", None))
        self.label_65.setText(QCoreApplication.translate("Form", u"  Montant des Droits et Taxes ", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Monnaie", None))
        self.Monnaie.setText(QCoreApplication.translate("Form", u"Monnaie", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"  Valeur DA ", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"  Date Bon \u00e0 enlever ", None))
        self.label_66.setText(QCoreApplication.translate("Form", u"  Date Visite Douane ", None))
        self.label_67.setText(QCoreApplication.translate("Form", u"  Date de Liquidation ", None))
        self.label_68.setText(QCoreApplication.translate("Form", u"  Date Recevabilit\u00e9 Ch\u00e8que ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"  Dossier re\u00e7u le ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"  \u00e0 ", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"  N\u00b0 Facture ", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"  Date d'\u00e9change ", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"  Date de la D\u00e9claration ", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"  N\u00b0  D\u00e9claration ", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"retour en arri\u00e8re", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"valider", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"  Pays de Fournisseur", None))
        self.pays.setText(QCoreApplication.translate("Form", u"pays", None))
        self.Fournisseur.setText(QCoreApplication.translate("Form", u"Fournisseur", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Fournisseur", None))
        self.label_105.setText(QCoreApplication.translate("Form", u"  Lieu de Transfert", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"  D\u00e9signation Marchandise", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"  Nbr Colis", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Poids Net", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"  Poids Brut", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nature marchandise", None))
        self.label_104.setText(QCoreApplication.translate("Form", u"  Pi\u00e8ces Jointes", None))
        ___qtablewidgetitem = self.tableau_marchandise.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"designation", None));
        ___qtablewidgetitem1 = self.tableau_marchandise.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"NB/QTE", None));
        ___qtablewidgetitem2 = self.tableau_marchandise.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Poids Bruit", None));
        ___qtablewidgetitem3 = self.tableau_marchandise.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Poids Net", None));
        ___qtablewidgetitem4 = self.tableau_marchandise.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"type marchandise", None));
        self.pushButton_21.setText(QCoreApplication.translate("Form", u"Nouveau", None))
        self.pushButton_22.setText(QCoreApplication.translate("Form", u"Modifier", None))
        self.pushButton_23.setText(QCoreApplication.translate("Form", u"Supprimer", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"N\u00b0 DOSSIER", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"CLIENT", None))
        self.line_client.setText("")
        self.client.setText(QCoreApplication.translate("Form", u"        client        ", None))

    # retranslateUi

    def suivant(self):
            v = 0
            if (self.line_declarant.text() == ""):
                self.line_declarant.setStyleSheet(u"border : 3px solid #ee2e31;\n"
                                       "border-radius:10px;\n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"
                                       
                                       "") #ee2e31
                v = 1
            if (self.mine_monnaie.text() == ""):
                self.mine_monnaie.setStyleSheet(u"border : 3px solid #ee2e31;\n"
                                                  "border-radius:10px;\n"
                                                  "padding: 3px;\n"
                                                  "background-color: white;\n"

                                                  "")  # ee2e31
                v = 1
            if (self.montant_droits_taxes.text() == ""):
                self.montant_droits_taxes.setStyleSheet(u"border : 3px solid #ee2e31;\n"
                                                  "border-radius:10px;\n"
                                                  "padding: 3px;\n"
                                                  "background-color: white;\n"

                                                  "")  # ee2e31
                v = 1
            if (self.line_navire.text() == ""):
                self.line_navire.setStyleSheet(u"border : 3px solid #ee2e31;\n"
                                                  "border-radius:10px;\n"
                                                  "padding: 3px;\n"
                                                  "background-color: white;\n"

                                                  "")  # ee2e31
                v = 1
            if (self.num_facture_3.text() == ""):
                self.num_facture_3.setStyleSheet(u"border : 3px solid #ee2e31;\n"
                                                  "border-radius:10px;\n"
                                                  "padding: 3px;\n"
                                                  "background-color: white;\n"

                                                  "")  # ee2e31
                v = 1
            if (v == 0):
               self.stackedWidget.setCurrentIndex(1)
    def retour2(self):
            self.stackedWidget.setCurrentIndex(0)
    def nouveau(self):
       val = (self.designation_marchandise.text(),self.nbr_colis.text(),self.poids_brut.text(),self.poids_net.text(),self.nature_marchandise.text())
       self.tabmarchandises.append(val)

       tablerow = 0
       self.tableau_marchandise.setRowCount(len(self.tabmarchandises))
       for row in self.tabmarchandises:
            print(row[0])
            self.tableau_marchandise.setItem(tablerow,0, QTableWidgetItem(row[0]))
            self.tableau_marchandise.setItem(tablerow,1, QTableWidgetItem(row[1]))
            self.tableau_marchandise.setItem(tablerow,2, QTableWidgetItem(row[2]))
            self.tableau_marchandise.setItem(tablerow,3, QTableWidgetItem(row[3]))
            self.tableau_marchandise.setItem(tablerow,4, QTableWidgetItem(row[4]))
            tablerow += 1
       self.designation_marchandise.clear()
       self.nbr_colis.clear()
       self.poids_brut.clear()
       self.poids_net.clear()
       self.nature_marchandise.clear()
    def create_navire(self):
        self.widg_navire.show()
    def validnav(self):
        self.line_navire.setText(self.widg_navire.rownavire[1])
        self.line_navire.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"

                                          "")
    def clt(self):

        self.widg_client.form.show()
    def create_monnaie(self):
        self.money.show()
    def validmoney(self):
        self.mine_monnaie.setText(self.money.rowmonnaie[1])
        self.mine_monnaie.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"

                                          "")
    def create_pays(self):
        self.country.show()
    def valicountry(self):
        self.pays_fournisseur.setText(self.country.rowpays[1])
        self.pays_fournisseur.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"

                                          "")

    def create_declarant(self):
        self.dec.show()
    def validdec(self):
        self.line_declarant.setText(self.dec.rowdeclarant[1]+" "+self.dec.rowdeclarant[2])
        self.line_declarant.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"

                                          "")
    def validclt(self):
        self.line_client.setText(self.widg_client.rowclient[1])
        self.widg_client.form.close()
    def change(self):
        if (self.mine_monnaie.text() != ""):
            self.valeur_da.setText(str(float(self.montant_droits_taxes.text())*float(self.money.rowmonnaie[2])))
        else:
            self.valeur_da.setText("0")
    def validerfinal(self):
        v = 0
        if (self.lineEdit.text() == ""):
            self.lineEdit.setStyleSheet(u"border : 3px solid #ee2e31;\n"
                                              "border-radius:10px;\n"
                                              "padding: 3px;\n"
                                              "background-color: white;\n"

                                              "")  # ee2e31
            v = 1
        if (self.line_client.text() == ""):
                self.line_client.setStyleSheet(u"border : 3px solid #ee2e31;\n"
                                                  "border-radius:10px;\n"
                                                  "padding: 3px;\n"
                                                  "background-color: white;\n"

                                                  "")  # ee2e31
                v = 1
        if (self.pays_fournisseur.text() == ""):
            self.pays_fournisseur.setStyleSheet(u"border : 3px solid #ee2e31;\n"
                                              "border-radius:10px;\n"
                                              "padding: 3px;\n"
                                              "background-color: white;\n"

                                              "")  # ee2e31
            v = 1
        if (v == 0):
          for row in self.tabmarchandises:
            sql = "INSERT INTO table_marchandises(id_dossier,marchandise,type_marchandise,nbr_colis,poids_brut,poids_net) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (int(self.lineEdit.text()),row[0],row[4],int(row[1]),int(row[2]),int(row[3]))
            mycursor.execute(sql,val)
            mydb.commit()
            print("insertion avec succes !")
          sql ="INSERT INTO dossier(dossier_id,client_id,ref_client_dossier,sit_dossier,date_reception,lieu_reception,num_facture,monnaie,nature_dossier,mode_transport,compagnie_transport,num_titre_transport,navire,date_arrivee,date_main_levee,lieu_entreposage,bureau_douane,receveur_douane,num_gros,num_article,S_G,date_echange,date_declaration,num_declaration,valeur_da,montant_droits_taxes,date_visite_douane,date_liquidation,date_recevabilite_cheque,date_aquittement_droits_taxes,num_quittance_douane,date_bon_enlever,num_bon_enlever,date_livraison,lieu_livraison,parc_vide,observation_dynamique,declarant,observation_statique,id_pays_fournisseur,id_fournisseur,lieu_transfert,pieces_jointes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          val = (int(self.lineEdit.text()),int(self.widg_client.rowclient[0]),self.ref_client_dossier.text(),self.situation_dossier.text(),self.date_recu.date().toString(Qt.ISODate),self.a.text(),int(self.num_facture_3.text()),int(self.money.rowmonnaie[0]),self.nature_dossier.text(),self.mode_transport.text(),self.compagnie_transport.text(),self.num_titre_transport.text(),int(self.widg_navire.rownavire[0]),self.date_arrivee.date().toString(Qt.ISODate),self.datemain_levee.date().toString(Qt.ISODate),self.lieu_entreposage.text(),self.bureau_douane.text()
          ,self.receveur_douanes.text(),self.num_gros.text(),self.num_article.text(),self.SG.text(),self.date_echange.date().toString(Qt.ISODate),self.date_declaration.date().toString(Qt.ISODate),self.num_declaration.text(),0,int(self.montant_droits_taxes.text()),self.date_visite_douane.date().toString(Qt.ISODate),self.date_liquidation.date().toString(Qt.ISODate),self.date_cheque.date().toString(Qt.ISODate),self.date_acquittement_taxes.date().toString(Qt.ISODate),self.num_quittance_douane.text(),self.date_bon_enlever.date().toString(Qt.ISODate) ,self.num_bon_enlever.text(),self.date_livraison.date().toString(Qt.ISODate),self.lieu_livraison.text(),self.parc_a_vide.text()
          , self.observation_dynamique.text() , int(self.dec.rowdeclarant[0]) ,"eeeeeee",int(self.country.rowpays[0]) ,66,self.lieu_de_transfert.text(),self.Pieces_jointes.text())
          print(val)
          print(self.date_echange.date().toString(Qt.ISODate))
          mycursor.execute(sql,val)
          print("insertion hhhh")
          mydb.commit()
    def couleurnumdossier(self):
        self.lineEdit.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "padding: 3px;\n"
                                          "color: black ; \n"
                                          "background-color: white;\n"

                                          "")
    def couleurclient(self):
        self.line_client.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                          "border-radius:10px;\n"
                                          "color: black ; \n"
                                          "padding: 3px;\n"
                                          "background-color: white;\n"

                                          "")
    def couleurfacture(self):
        self.num_facture_3.setStyleSheet(u"border : 3px solid #2f3e46;\n"
                                       "border-radius:10px;\n"
                                       "color: black ; \n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"

                                       "")

if __name__ == "__main__":
    app = QApplication()
    widget = Ui_Form()
    widget.form.show()
    app.exec_()