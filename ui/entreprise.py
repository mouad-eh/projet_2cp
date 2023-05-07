import mysql.connector
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PyQt5 import *
import sys
mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="rotage2015002",
   database="projet_beta"
)
mycursor = mydb.cursor()

class Ui_Form(object):
    def __init__(self,forms):
        self.form = forms
        self.setupUi(self.form)
        self.class_entreprise = Entreprise()
        self.valider.clicked.connect(self.valid)
        self.retour.clicked.connect(self.ret)

    def setupUi(self, Form):
            if not Form.objectName():
                Form.setObjectName(u"Form")
            Form.resize(1046, 764)
            self.gridLayout = QGridLayout(Form)
            self.gridLayout.setObjectName(u"gridLayout")
            self.frame = QFrame(Form)
            self.frame.setObjectName(u"frame")
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.frame.setFrameShadow(QFrame.Raised)
            self.verticalLayout_10 = QVBoxLayout(self.frame)
            self.verticalLayout_10.setObjectName(u"verticalLayout_10")
            self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
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

            self.verticalLayout_10.addWidget(self.frame_3)

            self.frame_4 = QFrame(self.frame)
            self.frame_4.setObjectName(u"frame_4")
            self.frame_4.setFrameShape(QFrame.StyledPanel)
            self.frame_4.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
            self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
            self.frame_2 = QFrame(self.frame_4)
            self.frame_2.setObjectName(u"frame_2")
            self.frame_2.setFrameShape(QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QFrame.Raised)
            self.verticalLayout = QVBoxLayout(self.frame_2)
            self.verticalLayout.setObjectName(u"verticalLayout")
            self.label = QLabel(self.frame_2)
            self.label.setObjectName(u"label")
            font1 = QFont()
            font1.setBold(True)
            font1.setWeight(75)
            self.label.setFont(font1)
            self.label.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout.addWidget(self.label)

            self.nom = QLineEdit(self.frame_2)
            self.nom.setObjectName(u"nom")
            self.nom.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                   "border-radius:10px;\n"
                                   "padding: 3px;\n"
                                   "background-color: white;\n"
                                   "color: #2f3e46;\n"
                                   "")

            self.verticalLayout.addWidget(self.nom)

            self.horizontalLayout_2.addWidget(self.frame_2)

            self.frame_8 = QFrame(self.frame_4)
            self.frame_8.setObjectName(u"frame_8")
            self.frame_8.setFrameShape(QFrame.StyledPanel)
            self.frame_8.setFrameShadow(QFrame.Raised)
            self.verticalLayout_5 = QVBoxLayout(self.frame_8)
            self.verticalLayout_5.setObjectName(u"verticalLayout_5")
            self.label_6 = QLabel(self.frame_8)
            self.label_6.setObjectName(u"label_6")
            self.label_6.setFont(font1)
            self.label_6.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_5.addWidget(self.label_6)

            self.adresse = QLineEdit(self.frame_8)
            self.adresse.setObjectName(u"adresse")
            self.adresse.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                       "border-radius:10px;\n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"
                                       "color: #2f3e46;\n"
                                       "")

            self.verticalLayout_5.addWidget(self.adresse)

            self.horizontalLayout_2.addWidget(self.frame_8)

            self.frame_7 = QFrame(self.frame_4)
            self.frame_7.setObjectName(u"frame_7")
            self.frame_7.setFrameShape(QFrame.StyledPanel)
            self.frame_7.setFrameShadow(QFrame.Raised)
            self.verticalLayout_4 = QVBoxLayout(self.frame_7)
            self.verticalLayout_4.setObjectName(u"verticalLayout_4")
            self.label_5 = QLabel(self.frame_7)
            self.label_5.setObjectName(u"label_5")
            self.label_5.setFont(font1)
            self.label_5.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_4.addWidget(self.label_5)

            self.site_web = QLineEdit(self.frame_7)
            self.site_web.setObjectName(u"site_web")
            self.site_web.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                        "border-radius:10px;\n"
                                        "padding: 3px;\n"
                                        "background-color: white;\n"
                                        "color: #2f3e46;\n"
                                        "")

            self.verticalLayout_4.addWidget(self.site_web)

            self.horizontalLayout_2.addWidget(self.frame_7)

            self.frame_10 = QFrame(self.frame_4)
            self.frame_10.setObjectName(u"frame_10")
            self.frame_10.setFrameShape(QFrame.StyledPanel)
            self.frame_10.setFrameShadow(QFrame.Raised)
            self.verticalLayout_7 = QVBoxLayout(self.frame_10)
            self.verticalLayout_7.setObjectName(u"verticalLayout_7")
            self.label_8 = QLabel(self.frame_10)
            self.label_8.setObjectName(u"label_8")
            self.label_8.setFont(font1)
            self.label_8.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_7.addWidget(self.label_8)

            self.type = QLineEdit(self.frame_10)
            self.type.setObjectName(u"type")
            self.type.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

            self.verticalLayout_7.addWidget(self.type)

            self.horizontalLayout_2.addWidget(self.frame_10)

            self.verticalLayout_10.addWidget(self.frame_4)

            self.frame_9 = QFrame(self.frame)
            self.frame_9.setObjectName(u"frame_9")
            self.frame_9.setFrameShape(QFrame.StyledPanel)
            self.frame_9.setFrameShadow(QFrame.Raised)
            self.verticalLayout_2 = QVBoxLayout(self.frame_9)
            self.verticalLayout_2.setObjectName(u"verticalLayout_2")
            self.frame_5 = QFrame(self.frame_9)
            self.frame_5.setObjectName(u"frame_5")
            self.frame_5.setFrameShape(QFrame.StyledPanel)
            self.frame_5.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
            self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
            self.frame_6 = QFrame(self.frame_5)
            self.frame_6.setObjectName(u"frame_6")
            self.frame_6.setFrameShape(QFrame.StyledPanel)
            self.frame_6.setFrameShadow(QFrame.Raised)
            self.verticalLayout_3 = QVBoxLayout(self.frame_6)
            self.verticalLayout_3.setObjectName(u"verticalLayout_3")
            self.label_4 = QLabel(self.frame_6)
            self.label_4.setObjectName(u"label_4")
            self.label_4.setFont(font1)
            self.label_4.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_3.addWidget(self.label_4)

            self.tel1 = QLineEdit(self.frame_6)
            self.tel1.setObjectName(u"tel1")
            self.tel1.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

            self.verticalLayout_3.addWidget(self.tel1)

            self.horizontalLayout_3.addWidget(self.frame_6)

            self.frame_11 = QFrame(self.frame_5)
            self.frame_11.setObjectName(u"frame_11")
            self.frame_11.setFrameShape(QFrame.StyledPanel)
            self.frame_11.setFrameShadow(QFrame.Raised)
            self.verticalLayout_8 = QVBoxLayout(self.frame_11)
            self.verticalLayout_8.setObjectName(u"verticalLayout_8")
            self.label_9 = QLabel(self.frame_11)
            self.label_9.setObjectName(u"label_9")
            self.label_9.setFont(font1)
            self.label_9.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_8.addWidget(self.label_9)

            self.tel2 = QLineEdit(self.frame_11)
            self.tel2.setObjectName(u"tel2")
            self.tel2.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

            self.verticalLayout_8.addWidget(self.tel2)

            self.horizontalLayout_3.addWidget(self.frame_11)

            self.frame_12 = QFrame(self.frame_5)
            self.frame_12.setObjectName(u"frame_12")
            self.frame_12.setFrameShape(QFrame.StyledPanel)
            self.frame_12.setFrameShadow(QFrame.Raised)
            self.verticalLayout_9 = QVBoxLayout(self.frame_12)
            self.verticalLayout_9.setObjectName(u"verticalLayout_9")
            self.label_10 = QLabel(self.frame_12)
            self.label_10.setObjectName(u"label_10")
            self.label_10.setFont(font1)
            self.label_10.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_9.addWidget(self.label_10)

            self.tel3 = QLineEdit(self.frame_12)
            self.tel3.setObjectName(u"tel3")
            self.tel3.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

            self.verticalLayout_9.addWidget(self.tel3)

            self.horizontalLayout_3.addWidget(self.frame_12)

            self.verticalLayout_2.addWidget(self.frame_5)

            self.frame_14 = QFrame(self.frame_9)
            self.frame_14.setObjectName(u"frame_14")
            self.frame_14.setFrameShape(QFrame.StyledPanel)
            self.frame_14.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_4 = QHBoxLayout(self.frame_14)
            self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
            self.frame_15 = QFrame(self.frame_14)
            self.frame_15.setObjectName(u"frame_15")
            self.frame_15.setFrameShape(QFrame.StyledPanel)
            self.frame_15.setFrameShadow(QFrame.Raised)
            self.verticalLayout_11 = QVBoxLayout(self.frame_15)
            self.verticalLayout_11.setObjectName(u"verticalLayout_11")
            self.label_12 = QLabel(self.frame_15)
            self.label_12.setObjectName(u"label_12")
            self.label_12.setFont(font1)
            self.label_12.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_11.addWidget(self.label_12)

            self.mob1 = QLineEdit(self.frame_15)
            self.mob1.setObjectName(u"mob1")
            self.mob1.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

            self.verticalLayout_11.addWidget(self.mob1)

            self.horizontalLayout_4.addWidget(self.frame_15)

            self.frame_16 = QFrame(self.frame_14)
            self.frame_16.setObjectName(u"frame_16")
            self.frame_16.setFrameShape(QFrame.StyledPanel)
            self.frame_16.setFrameShadow(QFrame.Raised)
            self.verticalLayout_12 = QVBoxLayout(self.frame_16)
            self.verticalLayout_12.setObjectName(u"verticalLayout_12")
            self.label_13 = QLabel(self.frame_16)
            self.label_13.setObjectName(u"label_13")
            self.label_13.setFont(font1)
            self.label_13.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_12.addWidget(self.label_13)

            self.mob2 = QLineEdit(self.frame_16)
            self.mob2.setObjectName(u"mob2")
            self.mob2.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

            self.verticalLayout_12.addWidget(self.mob2)

            self.horizontalLayout_4.addWidget(self.frame_16)

            self.frame_17 = QFrame(self.frame_14)
            self.frame_17.setObjectName(u"frame_17")
            self.frame_17.setFrameShape(QFrame.StyledPanel)
            self.frame_17.setFrameShadow(QFrame.Raised)
            self.verticalLayout_13 = QVBoxLayout(self.frame_17)
            self.verticalLayout_13.setObjectName(u"verticalLayout_13")
            self.label_14 = QLabel(self.frame_17)
            self.label_14.setObjectName(u"label_14")
            self.label_14.setFont(font1)
            self.label_14.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_13.addWidget(self.label_14)

            self.mob3 = QLineEdit(self.frame_17)
            self.mob3.setObjectName(u"mob3")
            self.mob3.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

            self.verticalLayout_13.addWidget(self.mob3)

            self.horizontalLayout_4.addWidget(self.frame_17)

            self.verticalLayout_2.addWidget(self.frame_14)

            self.frame_18 = QFrame(self.frame_9)
            self.frame_18.setObjectName(u"frame_18")
            self.frame_18.setFrameShape(QFrame.StyledPanel)
            self.frame_18.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_5 = QHBoxLayout(self.frame_18)
            self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
            self.frame_19 = QFrame(self.frame_18)
            self.frame_19.setObjectName(u"frame_19")
            self.frame_19.setFrameShape(QFrame.StyledPanel)
            self.frame_19.setFrameShadow(QFrame.Raised)
            self.verticalLayout_14 = QVBoxLayout(self.frame_19)
            self.verticalLayout_14.setObjectName(u"verticalLayout_14")
            self.label_15 = QLabel(self.frame_19)
            self.label_15.setObjectName(u"label_15")
            self.label_15.setFont(font1)
            self.label_15.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_14.addWidget(self.label_15)

            self.fax1 = QLineEdit(self.frame_19)
            self.fax1.setObjectName(u"fax1")
            self.fax1.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

            self.verticalLayout_14.addWidget(self.fax1)

            self.horizontalLayout_5.addWidget(self.frame_19)

            self.frame_20 = QFrame(self.frame_18)
            self.frame_20.setObjectName(u"frame_20")
            self.frame_20.setFrameShape(QFrame.StyledPanel)
            self.frame_20.setFrameShadow(QFrame.Raised)
            self.verticalLayout_15 = QVBoxLayout(self.frame_20)
            self.verticalLayout_15.setObjectName(u"verticalLayout_15")
            self.label_16 = QLabel(self.frame_20)
            self.label_16.setObjectName(u"label_16")
            self.label_16.setFont(font1)
            self.label_16.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_15.addWidget(self.label_16)

            self.fax2 = QLineEdit(self.frame_20)
            self.fax2.setObjectName(u"fax2")
            self.fax2.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                    "border-radius:10px;\n"
                                    "padding: 3px;\n"
                                    "background-color: white;\n"
                                    "color: #2f3e46;\n"
                                    "")

            self.verticalLayout_15.addWidget(self.fax2)

            self.horizontalLayout_5.addWidget(self.frame_20)

            self.frame_21 = QFrame(self.frame_18)
            self.frame_21.setObjectName(u"frame_21")
            self.frame_21.setFrameShape(QFrame.StyledPanel)
            self.frame_21.setFrameShadow(QFrame.Raised)
            self.verticalLayout_16 = QVBoxLayout(self.frame_21)
            self.verticalLayout_16.setObjectName(u"verticalLayout_16")
            self.label_17 = QLabel(self.frame_21)
            self.label_17.setObjectName(u"label_17")
            self.label_17.setFont(font1)
            self.label_17.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_16.addWidget(self.label_17)

            self.email = QLineEdit(self.frame_21)
            self.email.setObjectName(u"email")
            self.email.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                     "border-radius:10px;\n"
                                     "padding: 3px;\n"
                                     "background-color: white;\n"
                                     "color: #2f3e46;\n"
                                     "")

            self.verticalLayout_16.addWidget(self.email)

            self.horizontalLayout_5.addWidget(self.frame_21)

            self.verticalLayout_2.addWidget(self.frame_18)

            self.verticalLayout_10.addWidget(self.frame_9)

            self.frame_13 = QFrame(self.frame)
            self.frame_13.setObjectName(u"frame_13")
            self.frame_13.setFrameShape(QFrame.StyledPanel)
            self.frame_13.setFrameShadow(QFrame.Raised)
            self.verticalLayout_6 = QVBoxLayout(self.frame_13)
            self.verticalLayout_6.setObjectName(u"verticalLayout_6")
            self.label_11 = QLabel(self.frame_13)
            self.label_11.setObjectName(u"label_11")
            self.label_11.setFont(font1)
            self.label_11.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_6.addWidget(self.label_11)

            self.observation = QTextEdit(self.frame_13)
            self.observation.setObjectName(u"observation")
            self.observation.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                           "border-radius:10px;\n"
                                           "padding: 3px;\n"
                                           "background-color: white;\n"
                                           "color: #2f3e46;\n"
                                           "")

            self.verticalLayout_6.addWidget(self.observation)

            self.verticalLayout_10.addWidget(self.frame_13)

            self.frame_22 = QFrame(self.frame)
            self.frame_22.setObjectName(u"frame_22")
            self.frame_22.setFrameShape(QFrame.StyledPanel)
            self.frame_22.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_6 = QHBoxLayout(self.frame_22)
            self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
            self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

            self.valider = QPushButton(self.frame_22)
            self.valider.setObjectName(u"valider")
            self.valider.setFont(font)
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

            self.horizontalLayout_6.addWidget(self.valider)

            self.retour = QPushButton(self.frame_22)
            self.retour.setObjectName(u"retour")
            self.retour.setFont(font)
            self.retour.setStyleSheet(u"QPushButton {background-color: white;\n"
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
                                      "/*#ee2e31*/\n"
                                      "")

            self.horizontalLayout_6.addWidget(self.retour)

            self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

            self.verticalLayout_10.addWidget(self.frame_22)

            self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

            self.retranslateUi(Form)

            QMetaObject.connectSlotsByName(Form)

        # setupUi

    def retranslateUi(self, Form):
            Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
            self.label_2.setText(QCoreApplication.translate("Form", u"Information de l'entreprise", None))
            self.label.setText(QCoreApplication.translate("Form", u"Nom", None))
            self.label_6.setText(QCoreApplication.translate("Form", u"Adresse", None))
            self.label_5.setText(QCoreApplication.translate("Form", u"Site web", None))
            self.label_8.setText(QCoreApplication.translate("Form", u"Type", None))
            self.label_4.setText(QCoreApplication.translate("Form", u"tel1", None))
            self.label_9.setText(QCoreApplication.translate("Form", u"tel2", None))
            self.label_10.setText(QCoreApplication.translate("Form", u"tel3", None))
            self.label_12.setText(QCoreApplication.translate("Form", u"mob1", None))
            self.label_13.setText(QCoreApplication.translate("Form", u"mob2", None))
            self.label_14.setText(QCoreApplication.translate("Form", u"mob3", None))
            self.label_15.setText(QCoreApplication.translate("Form", u"fax1", None))
            self.label_16.setText(QCoreApplication.translate("Form", u"fax2", None))
            self.label_17.setText(QCoreApplication.translate("Form", u"email", None))
            self.label_11.setText(QCoreApplication.translate("Form", u"observation", None))
            self.valider.setText(QCoreApplication.translate("Form", u"Valider", None))
            self.retour.setText(QCoreApplication.translate("Form", u"Retour en arri\u00e8re", None))
        # retranslateUi
    def valid(self):
        self.class_entreprise.init(self.nom.text(), self.adresse.text(),self.type.text(), self.tel1.text(), self.tel2.text(), self.tel3.text(), self.mob1.text(),
               self.mob2.text(), self.mob3.text(), self.fax1.text(), self.fax2.text(), self.email.text(), self.site_web.text(),
               "aaa")
        print("click")
        self.form.hide()
    def ret(self):
        self.form.hide()


#La classe parent
class Entreprise:

   def init(self,  nom, adresse,type,tel1,tel2,tel3,mob1,mob2,mob3,fax1,fax2,email,siteweb,observation):
      self.nom = nom
      self.adresse = adresse
      self.type = type
      self.tel1 = tel1
      self.tel2 = tel2
      self.tel3 = tel3
      self.mob1 = mob1
      self.mob2 = mob2
      self.mob3 = mob3
      self.fax1 = fax1
      self.fax2 = fax2
      self.email = email
      self.siteweb = siteweb
      self.observation = observation
   def existe(self):
      sql = "SELECT * FROM entreprise WHERE entreprise_id = %s"
      mycursor.execute(sql, (self.entreprise_id, ))
      myresult = mycursor.fetchall()
      row_count = mycursor.rowcount

      if row_count == 0:  # s'il n'existe pas
         bool = False
      else:  # s'il existe
         bool = True
      return bool
   def inserer(self):
         sql = "INSERT INTO entreprise(nom, adresse,type,tel1,tel2,tel3,mob1,mob2,mob3,fax1,fax2,email,siteweb,observation) VALUES (%s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s)"
         values = (self.nom,self.adresse,self.type,self.tel1,self.tel2,self.tel3,self.mob1,self.mob2,self.mob3,self.fax1,self.fax2,self.email,self.siteweb,self.observation)
         mycursor.execute(sql, values)
         mydb.commit()
         print("Insertion avec succes!")
         return mycursor.lastrowid
   def importer(self,id_entreprise):
      sql = "SELECT * FROM entreprise WHERE entreprise_id = %s"
      self.entreprise_id = id_entreprise
      mycursor.execute(sql,(id_entreprise,))
      myresult = mycursor.fetchone()
      self.nom = myresult[1]
      self.adresse = myresult[2]
      self.type = myresult[3]
      self.tel1 = myresult[4]
      self.tel2 = myresult[5]
      self.tel3 = myresult[6]
      self.mob1 = myresult[7]
      self.mob2 = myresult[8]
      self.mob3 = myresult[9]
      self.fax1 = myresult[10]
      self.fax2 = myresult[11]
      self.email = myresult[12]
      self.siteweb = myresult[13]
      self.observation = myresult[14]
   def modifier(self):
      sql = "UPDATE entreprise SET nom =%s, adresse=%s,tel1=%s ,tel2=%s,tel3=%s,mob1=%s,mob2=%s,mob3=%s,fax1=%s,fax2=%s,email=%s,siteweb=%s,observation=%s WHERE entreprise_id=%s"
      values = (self.nom, self.adresse,self.type, self.tel1, self.tel2, self.tel3, self.mob1, self.mob2, self.mob3,self.fax1, self.fax2, self.email, self.siteweb, self.observation,self.entreprise_id)
      mycursor.execute(sql,values)
      mydb.commit()



class Client(Entreprise):

   def existe(self):
      sql = "SELECT * FROM client WHERE client_id = %s"
      mycursor.execute(sql, (self.client_id, ))
      myresult = mycursor.fetchall()
      row_count = mycursor.rowcount

      if row_count == 0:  # s'il n'existe pas
         bool = False
      else:  # s'il existe
         bool = True
      return bool
   def init(self,entreprise_id,code_postal,id_rc,wilaya,statut_juridique,id_mandat,num_succursale,num_NIF,num_NIS,num_art_imposition):
      Entreprise.importer(self,entreprise_id)
      self.code_postal =code_postal
      self.num_RC = id_rc
      self.id_mandat =  id_mandat
      self.wilaya = wilaya
      self.statut_juridique = statut_juridique
      self.num_succursale = num_succursale
      self.num_NIF = num_NIF
      self.num_NIS = num_NIS
      self.num_art_imposition = num_art_imposition
   def inserer(self):
      #Entreprise.inserer(self)
      sql ="INSERT INTO client (entreprise_id ,code_postal,num_RC,wilaya,statut_juridique,mandat_id,num_succursale,num_NIF,num_NIS,num_art_imposition) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      value =(self.entreprise_id,self.code_postal,self.num_RC,self.wilaya,self.statut_juridique,self.id_mandat,self.num_succursale,self.num_NIF,self.num_NIS,self.num_art_imposition)
      mycursor.execute(sql, value)
      mydb.commit()
   def importer(self,client_id):
      self.client_id = client_id
      sql = "SELECT * FROM client WHERE client_id = %s"
      mycursor.execute(sql,(self.client_id,))
      myresult = mycursor.fetchone()

      self.entreprise_id = myresult[1]
      self.code_postal = myresult[2]
      self.num_RC = myresult[3]
      self.wilaya = myresult[4]
      self.statut_juridique = myresult[5]
      self.id_mandat = myresult[6]
      self.num_succursale = myresult[7]
      self.num_NIF = myresult[8]
      self.num_NIS = myresult[9]
      self.num_art_imposition = myresult[10]
      Entreprise.importer(self,self.entreprise_id)
   def modifier(self):
      sql = "UPDATE client SET entreprise_id=%s,code_postal=%s,num_RC=%s,wilaya=%s,statut_juridique=%s,num_succursale=%s,num_NIF=%s,num_NIS=%s,num_art_imposition=%s WHERE client_id = %s"
      value =(self.entreprise_id,self.code_postal,self.num_RC,self.wilaya,self.statut_juridique,self.num_succursale,self.num_NIF,self.num_NIS,self.num_art_imposition,self.client_id)
      mycursor.execute(sql, value)
      mydb.commit()
class contact(Entreprise):
   def existe(self):
      sql = "SELECT * FROM contact WHERE contact_id = %s"
      mycursor.execute(sql, (self.contact_id, ))
      myresult = mycursor.fetchall()
      row_count = mycursor.rowcount

      if row_count == 0:  # s'il n'existe pas
         bool = False
      else:  # s'il existe
         bool = True
      return bool
   def init(self,contact_id,type,entreprise_id):
       self.contact_id = contact_id
       Entreprise.importer(self,self.entreprise_id)
       self.type = type

   def inserer(self):
      sql = "INSERT INTO contact (contact_id,type,entreprise_id) VALUES (%s,%s,%s)"
      value = (self.contact_id,self.type,self.entreprise_id)
      mycursor.execute(sql, value)
      mydb.commit()
   def importer(self,contact_id):
      self.contact_id = contact_id
      sql = "SELECT * FROM contact WHERE contact_id = %s"
      mycursor.execute(sql, (self.contact_id,))
      myresult = mycursor.fetchone()
      self.type = myresult[1]
      self.entreprise_id = myresult[2]
      Entreprise.importer(self,self.entreprise_id)
   def modifier(self):
      sql = "UPDATE contact SET type=%s , entreprise_id = %s WHERE contact_id =%s"
      value = (self.entreprise_id,self.type,self.contact_id)
      mycursor.execute(sql, value)
      mydb.commit()


class fournisseur(Entreprise):
   def existe(self):
      sql = "SELECT * FROM fournisseur WHERE fournisseur_id = %s"
      mycursor.execute(sql, (self.fournisseur_id,))
      myresult = mycursor.fetchall()
      row_count = mycursor.rowcount

      if row_count == 0:  # s'il n'existe pas
         bool = False
      else:  # s'il existe
         bool = True
      return bool

   def init(self, fournisseur_id,entreprise_id):
      self.fournisseur_id = fournisseur_id
      Entreprise.importer(self, self.entreprise_id)

   def inserer(self):
      sql = "INSERT INTO fournisseur (fournisseur_id,type,entreprise_id) VALUES (%s,%s,%s)"
      value = (self.fournisseur_id, self.type, self.entreprise_id)
      mycursor.execute(sql, value)
      mydb.commit()

   def importer(self, fournisseur_id):
      self.fournisseur_id = fournisseur_id
      sql = "SELECT * FROM fournisseur WHERE fournisseur_id = %s"
      mycursor.execute(sql, (self.fournisseur_id,))
      myresult = mycursor.fetchone()
      self.entreprise_id = myresult[1]
      Entreprise.importer(self, self.entreprise_id)

   def modifier(self):
      sql = "UPDATE contact SET type=%s , fournisseur_id = %s WHERE fournisseur_id =%s"
      value = (self.entreprise_id, self.fournisseur_id)
      mycursor.execute(sql, value)
      mydb.commit()

class Document:
    # le constructeur de la classe Document
    def init(self,nbr_clients,date_document,date_exp_document ):
        self.nbr_clients = nbr_clients
        self.date_document = date_document
        self.date_exp_document= date_exp_document


    def existe(self):
        sql = "SELECT * FROM document WHERE document_id = %s"
        mycursor.execute(sql, (self.id_document,))
        myresult = mycursor.fetchall()
        row_count = mycursor.rowcount

        if row_count == 0:  # s'il n'existe pas
            bool = False
        else:  # s'il existe
            bool = True
        return bool


    def inserer(self):
            sql = "INSERT INTO document(nbr_clients,date_document,date_exp_document) VALUES(%s,%s,%s) "
            sauv = (self.nbr_clients,self.date_document,self.date_exp_document)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Insertion avec succes!")
            return mycursor.lastrowid

    def importer(self,id_document):
        sql = "SELECT * FROM entreprise WHERE entreprise_id = %s"
        self.id_document = id_document
        mycursor.execute(sql, (id_document,))
        myresult = mycursor.fetchone()
        self.nbr_clients = myresult[1]
        self.date_document = myresult[2]
        self.date_exp_document = myresult[3]
    def sup(self):
        if Document.existe(self):
            sql = "DELETE FROM document WHERE document_id = %s"
            mycursor.execute(sql, (self.document_id,))
            mydb.commit()
            print("Suppression avec succes!")
        else:
            print("Suppression avec echec :  c'est inexistant!")

class Mandat(Document):
    # le constructeur de la classe Mandat
    def init(self, mandat_id, document_id ):
        self.mandat_id = mandat_id
        self.document_id = document_id

    def existe(self):
        sql = "SELECT * FROM mandat WHERE mandat_id = %s"
        mycursor.execute(sql, (self.mandat_id,))
        myresult = mycursor.fetchall()
        row_count = mycursor.rowcount

        if row_count == 0:  # s'il n'existe pas
            bool = False
        else:  # s'il existe
            bool = True
        return bool

    def inserer(self):

        if not Mandat.existe(self):  # ss'il n'existe pas
            sql = "INSERT INTO mandat  ( mandat_id, document_id) VALUES (%s,%s )"
            sauv = (self.mandat_id, self.document_id)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Insertion avec succes!")
        else:
            print("Insertion avec echec : C'est existant!")

    def sup(self):
        if Mandat.existe(self):
            sql = "DELETE FROM mandat WHERE mandat_id = %s"
            mycursor.execute(sql, (self.mandat_id,))
            mydb.commit()
            print("Suppression avec succes!")
        else:
            print("Suppression avec echec :  c'est inexistant!")


class Rc(Document):
    # le constructeur de la classe Rc
    def init(self, rc_id, document_id ):
        self.rc_id = rc_id
        self.document_id = document_id

    def existe(self):
        sql = "SELECT * FROM rc WHERE rc_id = %s"
        mycursor.execute(sql, (self.rc_id,))
        myresult = mycursor.fetchall()
        row_count = mycursor.rowcount

        if row_count == 0:  # s'il n'existe pas
            bool = False
        else:  # s'il existe
            bool = True
        return bool

    def inserer(self):

        if not Rc.existe(self):  # ss'il n'existe pas
            sql = "INSERT INTO  rc (rc_id, document_id) VALUES (%s,%s )"
            sauv = (self.rc_id, self.document_id)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Insertion avec succes!")
        else:
            print("Insertion avec echec : C'est existant!")

    def sup(self):
        if Rc.existe(self):
            sql = "DELETE FROM rc WHERE rc_id = %s"
            mycursor.execute(sql, (self.rc_id,))
            mydb.commit()
            print("Suppression avec succes!")
        else:
            print("Suppression avec echec :  c'est inexistant!")
