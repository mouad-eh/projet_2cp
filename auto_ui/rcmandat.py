# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designereCQYxw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.entreprise import *

class Ui_rcmandat(object):
    def __init__(self,forms):
            self.form = forms
            self.setupUi(self.form)
            self.valider.clicked.connect(self.valid)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(722, 343)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
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

        self.verticalLayout_8.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame_5)
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

        self.num_rc = QLineEdit(self.frame_2)
        self.num_rc.setObjectName(u"num_rc")
        self.num_rc.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                  "border-radius:10px;\n"
                                  "padding: 3px;\n"
                                  "background-color: white;\n"
                                  "color: #2f3e46;\n"
                                  "")

        self.verticalLayout.addWidget(self.num_rc)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

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

        self.date_rc = QDateEdit(self.frame_6)
        self.date_rc.setObjectName(u"date_rc")

        self.verticalLayout_3.addWidget(self.date_rc)

        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
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

        self.date_exp_rc = QDateEdit(self.frame_7)
        self.date_exp_rc.setObjectName(u"date_exp_rc")

        self.verticalLayout_4.addWidget(self.date_exp_rc)

        self.horizontalLayout_2.addWidget(self.frame_7)

        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.frame_10)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #2f3e46;")

        self.verticalLayout_2.addWidget(self.label_3)

        self.num_mandat = QLineEdit(self.frame_4)
        self.num_mandat.setObjectName(u"num_mandat")
        self.num_mandat.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                      "border-radius:10px;\n"
                                      "padding: 3px;\n"
                                      "background-color: white;\n"
                                      "color: #2f3e46;\n"
                                      "")

        self.verticalLayout_2.addWidget(self.num_mandat)

        self.horizontalLayout_3.addWidget(self.frame_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.frame_8 = QFrame(self.frame_10)
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

        self.date_mandat = QDateEdit(self.frame_8)
        self.date_mandat.setObjectName(u"date_mandat")

        self.verticalLayout_5.addWidget(self.date_mandat)

        self.horizontalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_10)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: #2f3e46;")

        self.verticalLayout_7.addWidget(self.label_8)

        self.date_exp_mandat = QDateEdit(self.frame_9)
        self.date_exp_mandat.setObjectName(u"date_exp_mandat")

        self.verticalLayout_7.addWidget(self.date_exp_mandat)

        self.horizontalLayout_3.addWidget(self.frame_9)

        self.verticalLayout_8.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.valider = QPushButton(self.frame_11)
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

        self.horizontalLayout_4.addWidget(self.valider)

        self.fermer = QPushButton(self.frame_11)
        self.fermer.setObjectName(u"fermer")
        self.fermer.setFont(font)
        self.fermer.setStyleSheet(u"QPushButton {background-color: white;\n"
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

        self.horizontalLayout_4.addWidget(self.fermer)

        self.verticalLayout_8.addWidget(self.frame_11)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Information registre de commerce", None))
        self.label.setText(QCoreApplication.translate("Form", u"Num\u00e9ro RC", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Date RC", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Date expiration RC", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Num\u00e9ro mandat", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Date mandat", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Date expiration mandat", None))
        self.valider.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.fermer.setText(QCoreApplication.translate("Form", u"Fermer", None))

    # retranslateUi

    def valid(self):
            docs = Document()
            self.mandat = Mandat()
            self.RC = Rc()
            print(self.date_mandat.date().toPython())
            docs.init(10,self.date_rc.date().toPython(),self.date_exp_rc.date().toPython())
            id = docs.inserer()
            self.mandat.init(self.num_mandat.text(),id)
            docs.init(10, self.date_mandat.date().toPython(), self.date_exp_mandat.date().toPython())
            id = docs.inserer()
            self.RC.init(self.num_rc.text(),id)
            self.form.hide()
            
