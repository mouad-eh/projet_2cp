# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajout_emballagevYvepb.ui'
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
        Form.resize(624, 397)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #2f3e46;\n"
"color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(258, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(255,255,255,0.3);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #52796f;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.num = QLineEdit(self.frame_2)
        self.num.setObjectName(u"num")
        self.num.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border: 1px solid #52796f;\n"
"border-radius: 3px;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.num)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.valider = QPushButton(self.frame_2)
        self.valider.setObjectName(u"valider")
        self.valider.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #3bb273;\n"
"padding: 6px;\n"
"width: 65px;\n"
"border: 2px solid #3bb273;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #3bb273;color: white;}\n"
"QPushButton:pressed { margin: 1px; }")

        self.verticalLayout_3.addWidget(self.valider)

        self.annuler = QPushButton(self.frame_2)
        self.annuler.setObjectName(u"annuler")
        self.annuler.setStyleSheet(u"QPushButton {\n"
"background-color: white;\n"
"color: #ee2e31;\n"
"padding: 5px;\n"
"width: 65px;\n"
"border: 2px solid #ee2e31;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {background-color: #ee2e31;color: white;}\n"
"QPushButton:pressed{margin: 1px;}\n"
"")

        self.verticalLayout_3.addWidget(self.annuler)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 4, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #52796f;")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.num_emballage = QLineEdit(self.frame_2)
        self.num_emballage.setObjectName(u"num_emballage")
        self.num_emballage.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border: 1px solid #52796f;\n"
"border-radius: 3px;")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.num_emballage)


        self.gridLayout_2.addLayout(self.formLayout_2, 1, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #52796f;")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.genre_emballage = QLineEdit(self.frame_2)
        self.genre_emballage.setObjectName(u"genre_emballage")
        self.genre_emballage.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border: 1px solid #52796f;\n"
"border-radius: 3px;\n"
"")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.genre_emballage)


        self.gridLayout_2.addLayout(self.formLayout_3, 2, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: #52796f;")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.pieds = QLineEdit(self.frame_2)
        self.pieds.setObjectName(u"pieds")
        self.pieds.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border: 1px solid #52796f;\n"
"border-radius: 3px;")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.pieds)


        self.gridLayout_2.addLayout(self.formLayout_4, 3, 0, 1, 1)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: #52796f;")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.type_emballage = QLineEdit(self.frame_2)
        self.type_emballage.setObjectName(u"type_emballage")
        self.type_emballage.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border: 1px solid #52796f;\n"
"border-radius: 3px;")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.type_emballage)


        self.gridLayout_2.addLayout(self.formLayout_5, 4, 0, 1, 1)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: #52796f;")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.date_livraison = QDateEdit(self.frame_2)
        self.date_livraison.setObjectName(u"date_livraison")
        self.date_livraison.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border: 1px solid #52796f;\n"
"border-radius: 3px;")
        self.date_livraison.setWrapping(False)
        self.date_livraison.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_livraison.setCalendarPopup(False)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.date_livraison)


        self.gridLayout_2.addLayout(self.formLayout_8, 5, 0, 1, 1)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: #52796f")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.date_restitution = QDateEdit(self.frame_2)
        self.date_restitution.setObjectName(u"date_restitution")
        self.date_restitution.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border: 1px solid #52796f;\n"
"border-radius: 3px;")
        self.date_restitution.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.date_restitution)


        self.gridLayout_2.addLayout(self.formLayout_6, 6, 0, 1, 1)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #52796f;")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.num_bon = QLineEdit(self.frame_2)
        self.num_bon.setObjectName(u"num_bon")
        self.num_bon.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border: 1px solid #52796f;\n"
"border-radius: 3px;")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.num_bon)


        self.gridLayout_2.addLayout(self.formLayout_7, 7, 0, 1, 1)

        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: #52796f;")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.description = QTextEdit(self.frame_2)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"background-color: white;\n"
"color: #2f3e46;\n"
"padding: 3px;\n"
"border: 1px solid #52796f;\n"
"border-radius: 3px;")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.description)


        self.gridLayout_2.addLayout(self.formLayout_9, 8, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ajout Emballage", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"N\u00b0", None))
        self.valider.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.annuler.setText(QCoreApplication.translate("Form", u"Annuler", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"N\u00b0 Emballage", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Genre d'emballage", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Pieds", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Type d'emballage", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Date de livraison", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Date de R\u00e9stitution", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"N\u00b0 Bon/ Facture de R\u00e9stitution", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Description", None))
    # retranslateUi

