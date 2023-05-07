# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nv_clientySyBKE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from ui.entreprise import *
from auto_ui.rcmandat import *
class Ui_ajout_client(object):
    def __init__(self,forms):
            self.form = forms
            self.form2 = QtWidgets.QWidget()
            self.form3 = QtWidgets.QWidget()
            self.entreprise = Ui_Form(self.form2)
            self.rc_md = Ui_rcmandat(self.form3)
            self.setupUi(self.form)
            self.confirmer.clicked.connect(self.conf)
            self.retour_en_arriere.clicked.connect(self.retour)
            self.info_entreprise.clicked.connect(self.info_entr)
            self.info_mandat_rc.clicked.connect(self.info_rcmd)
            self.client = Client()

    def setupUi(self, Form):
            if not Form.objectName():
                    Form.setObjectName(u"Form")
            Form.resize(1070, 527)
            self.gridLayout = QGridLayout(Form)
            self.gridLayout.setObjectName(u"gridLayout")
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.frame = QFrame(Form)
            self.frame.setObjectName(u"frame")
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.frame.setFrameShadow(QFrame.Raised)
            self.verticalLayout_8 = QVBoxLayout(self.frame)
            self.verticalLayout_8.setObjectName(u"verticalLayout_8")
            self.frame_3 = QFrame(self.frame)
            self.frame_3.setObjectName(u"frame_3")
            self.frame_3.setStyleSheet(u"background-color: #2f3e40; /*#2f3e46,1a535c;1d3557;233d4d*/\n"
                                       "color: rgb(255, 255, 255);")
            self.frame_3.setFrameShape(QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QFrame.Raised)
            self.horizontalLayout = QHBoxLayout(self.frame_3)
            self.horizontalLayout.setObjectName(u"horizontalLayout")
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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

            self.frame_2 = QFrame(self.frame)
            self.frame_2.setObjectName(u"frame_2")
            self.frame_2.setFrameShape(QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
            self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
            self.info_entreprise = QPushButton(self.frame_2)
            self.info_entreprise.setObjectName(u"info_entreprise")
            self.info_entreprise.setFont(font)
            self.info_entreprise.setStyleSheet(u"QPushButton {width: 65px;\n"
                                               "background-color: white;\n"
                                               "border: 2px solid #3bb273;\n"
                                               "color: #3bb273;\n"
                                               "padding: 6px;\n"
                                               "border-radius: 10px;}\n"
                                               "\n"
                                               "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                               "QPushButton:pressed { margin: 1px; }\n"
                                               "")

            self.horizontalLayout_2.addWidget(self.info_entreprise)

            self.info_mandat_rc = QPushButton(self.frame_2)
            self.info_mandat_rc.setObjectName(u"info_mandat_rc")
            self.info_mandat_rc.setFont(font)
            self.info_mandat_rc.setStyleSheet(u"QPushButton {width: 65px;\n"
                                              "background-color: white;\n"
                                              "border: 2px solid #3bb273;\n"
                                              "color: #3bb273;\n"
                                              "padding: 6px;\n"
                                              "border-radius: 10px;}\n"
                                              "\n"
                                              "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                              "QPushButton:pressed { margin: 1px; }\n"
                                              "")

            self.horizontalLayout_2.addWidget(self.info_mandat_rc)

            self.verticalLayout_8.addWidget(self.frame_2)

            self.frame_4 = QFrame(self.frame)
            self.frame_4.setObjectName(u"frame_4")
            self.frame_4.setFrameShape(QFrame.StyledPanel)
            self.frame_4.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
            self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
            self.frame_5 = QFrame(self.frame_4)
            self.frame_5.setObjectName(u"frame_5")
            self.frame_5.setFrameShape(QFrame.StyledPanel)
            self.frame_5.setFrameShadow(QFrame.Raised)
            self.verticalLayout = QVBoxLayout(self.frame_5)
            self.verticalLayout.setObjectName(u"verticalLayout")
            self.label = QLabel(self.frame_5)
            self.label.setObjectName(u"label")
            font1 = QFont()
            font1.setBold(True)
            font1.setWeight(75)
            self.label.setFont(font1)
            self.label.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout.addWidget(self.label)

            self.code_postale = QLineEdit(self.frame_5)
            self.code_postale.setObjectName(u"code_postale")
            self.code_postale.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                            "border-radius:10px;\n"
                                            "padding: 3px;\n"
                                            "background-color: white;\n"
                                            "color: #2f3e46;\n"
                                            "")

            self.verticalLayout.addWidget(self.code_postale)

            self.horizontalLayout_3.addWidget(self.frame_5)

            self.frame_6 = QFrame(self.frame_4)
            self.frame_6.setObjectName(u"frame_6")
            self.frame_6.setFrameShape(QFrame.StyledPanel)
            self.frame_6.setFrameShadow(QFrame.Raised)
            self.verticalLayout_2 = QVBoxLayout(self.frame_6)
            self.verticalLayout_2.setObjectName(u"verticalLayout_2")
            self.label_3 = QLabel(self.frame_6)
            self.label_3.setObjectName(u"label_3")
            self.label_3.setFont(font1)
            self.label_3.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_2.addWidget(self.label_3)

            self.num_nif = QLineEdit(self.frame_6)
            self.num_nif.setObjectName(u"num_nif")
            self.num_nif.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                       "border-radius:10px;\n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"
                                       "color: #2f3e46;\n"
                                       "")

            self.verticalLayout_2.addWidget(self.num_nif)

            self.horizontalLayout_3.addWidget(self.frame_6)

            self.frame_7 = QFrame(self.frame_4)
            self.frame_7.setObjectName(u"frame_7")
            self.frame_7.setFrameShape(QFrame.StyledPanel)
            self.frame_7.setFrameShadow(QFrame.Raised)
            self.verticalLayout_3 = QVBoxLayout(self.frame_7)
            self.verticalLayout_3.setObjectName(u"verticalLayout_3")
            self.label_4 = QLabel(self.frame_7)
            self.label_4.setObjectName(u"label_4")
            self.label_4.setFont(font1)
            self.label_4.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_3.addWidget(self.label_4)

            self.num_nis = QLineEdit(self.frame_7)
            self.num_nis.setObjectName(u"num_nis")
            self.num_nis.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                       "border-radius:10px;\n"
                                       "padding: 3px;\n"
                                       "background-color: white;\n"
                                       "color: #2f3e46;\n"
                                       "")

            self.verticalLayout_3.addWidget(self.num_nis)

            self.horizontalLayout_3.addWidget(self.frame_7)

            self.frame_8 = QFrame(self.frame_4)
            self.frame_8.setObjectName(u"frame_8")
            self.frame_8.setFrameShape(QFrame.StyledPanel)
            self.frame_8.setFrameShadow(QFrame.Raised)
            self.verticalLayout_4 = QVBoxLayout(self.frame_8)
            self.verticalLayout_4.setObjectName(u"verticalLayout_4")
            self.label_5 = QLabel(self.frame_8)
            self.label_5.setObjectName(u"label_5")
            self.label_5.setFont(font1)
            self.label_5.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_4.addWidget(self.label_5)

            self.statut_juridique = QLineEdit(self.frame_8)
            self.statut_juridique.setObjectName(u"statut_juridique")
            self.statut_juridique.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                                "border-radius:10px;\n"
                                                "padding: 3px;\n"
                                                "background-color: white;\n"
                                                "color: #2f3e46;\n"
                                                "")

            self.verticalLayout_4.addWidget(self.statut_juridique)

            self.horizontalLayout_3.addWidget(self.frame_8)

            self.verticalLayout_8.addWidget(self.frame_4)

            self.frame_9 = QFrame(self.frame)
            self.frame_9.setObjectName(u"frame_9")
            self.frame_9.setFrameShape(QFrame.StyledPanel)
            self.frame_9.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
            self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
            self.frame_10 = QFrame(self.frame_9)
            self.frame_10.setObjectName(u"frame_10")
            self.frame_10.setFrameShape(QFrame.StyledPanel)
            self.frame_10.setFrameShadow(QFrame.Raised)
            self.verticalLayout_5 = QVBoxLayout(self.frame_10)
            self.verticalLayout_5.setObjectName(u"verticalLayout_5")
            self.wilaya_3 = QLabel(self.frame_10)
            self.wilaya_3.setObjectName(u"wilaya_3")
            self.wilaya_3.setFont(font1)
            self.wilaya_3.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_5.addWidget(self.wilaya_3)

            self.wilaya = QLineEdit(self.frame_10)
            self.wilaya.setObjectName(u"wilaya")
            self.wilaya.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                      "border-radius:10px;\n"
                                      "padding: 3px;\n"
                                      "background-color: white;\n"
                                      "color: #2f3e46;\n"
                                      "")

            self.verticalLayout_5.addWidget(self.wilaya)

            self.horizontalLayout_4.addWidget(self.frame_10)

            self.frame_11 = QFrame(self.frame_9)
            self.frame_11.setObjectName(u"frame_11")
            self.frame_11.setFrameShape(QFrame.StyledPanel)
            self.frame_11.setFrameShadow(QFrame.Raised)
            self.verticalLayout_6 = QVBoxLayout(self.frame_11)
            self.verticalLayout_6.setObjectName(u"verticalLayout_6")
            self.numerosuccursale = QLabel(self.frame_11)
            self.numerosuccursale.setObjectName(u"numerosuccursale")
            self.numerosuccursale.setFont(font1)
            self.numerosuccursale.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_6.addWidget(self.numerosuccursale)

            self.num_succursale = QLineEdit(self.frame_11)
            self.num_succursale.setObjectName(u"num_succursale")
            self.num_succursale.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                              "border-radius:10px;\n"
                                              "padding: 3px;\n"
                                              "background-color: white;\n"
                                              "color: #2f3e46;\n"
                                              "")

            self.verticalLayout_6.addWidget(self.num_succursale)

            self.horizontalLayout_4.addWidget(self.frame_11)

            self.frame_12 = QFrame(self.frame_9)
            self.frame_12.setObjectName(u"frame_12")
            self.frame_12.setFrameShape(QFrame.StyledPanel)
            self.frame_12.setFrameShadow(QFrame.Raised)
            self.verticalLayout_7 = QVBoxLayout(self.frame_12)
            self.verticalLayout_7.setObjectName(u"verticalLayout_7")
            self.numeroartimposition = QLabel(self.frame_12)
            self.numeroartimposition.setObjectName(u"numeroartimposition")
            self.numeroartimposition.setFont(font1)
            self.numeroartimposition.setStyleSheet(u"color: #2f3e46;")

            self.verticalLayout_7.addWidget(self.numeroartimposition)

            self.num_art_imposition = QLineEdit(self.frame_12)
            self.num_art_imposition.setObjectName(u"num_art_imposition")
            self.num_art_imposition.setStyleSheet(u"border : 1px solid #2f3e46;\n"
                                                  "border-radius:10px;\n"
                                                  "padding: 3px;\n"
                                                  "background-color: white;\n"
                                                  "color: #2f3e46;\n"
                                                  "")

            self.verticalLayout_7.addWidget(self.num_art_imposition)

            self.horizontalLayout_4.addWidget(self.frame_12)

            self.verticalLayout_8.addWidget(self.frame_9)

            self.frame_13 = QFrame(self.frame)
            self.frame_13.setObjectName(u"frame_13")
            self.frame_13.setFrameShape(QFrame.StyledPanel)
            self.frame_13.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
            self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
            self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

            self.confirmer = QPushButton(self.frame_13)
            self.confirmer.setObjectName(u"confirmer")
            self.confirmer.setFont(font)
            self.confirmer.setStyleSheet(u"QPushButton {width: 65px;\n"
                                         "background-color: white;\n"
                                         "border: 2px solid #3bb273;\n"
                                         "color: #3bb273;\n"
                                         "padding: 6px;\n"
                                         "border-radius: 10px;}\n"
                                         "\n"
                                         "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                         "QPushButton:pressed { margin: 1px; }\n"
                                         "")

            self.horizontalLayout_5.addWidget(self.confirmer)

            self.retour_en_arriere = QPushButton(self.frame_13)
            self.retour_en_arriere.setObjectName(u"retour_en_arriere")
            self.retour_en_arriere.setFont(font)
            self.retour_en_arriere.setStyleSheet(u"QPushButton {background-color: white;\n"
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

            self.horizontalLayout_5.addWidget(self.retour_en_arriere)

            self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

            self.verticalLayout_8.addWidget(self.frame_13)

            self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

            self.retranslateUi(Form)

            QMetaObject.connectSlotsByName(Form)
            # setupUi

    def retranslateUi(self, Form):
            Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
            self.label_2.setText(QCoreApplication.translate("Form", u"Ajouter nouveau client", None))
            self.info_entreprise.setText(QCoreApplication.translate("Form", u"Information de l'entreprise", None))
            self.info_mandat_rc.setText(
                    QCoreApplication.translate("Form", u"Information mandat et registre de commerce", None))
            self.label.setText(QCoreApplication.translate("Form", u"Code postale", None))
            self.label_3.setText(QCoreApplication.translate("Form", u"Num\u00e9ro NIF", None))
            self.label_4.setText(QCoreApplication.translate("Form", u"Num\u00e9ro NIS", None))
            self.label_5.setText(QCoreApplication.translate("Form", u"Statut juridique", None))
            self.wilaya_3.setText(QCoreApplication.translate("Form", u"Wilaya", None))
            self.numerosuccursale.setText(QCoreApplication.translate("Form", u"num\u00e9ro succursale", None))
            self.numeroartimposition.setText(QCoreApplication.translate("Form", u"num\u00e9ro art imposition", None))
            self.confirmer.setText(QCoreApplication.translate("Form", u"Confirmer", None))
            self.retour_en_arriere.setText(QCoreApplication.translate("Form", u"Retour en arri\u00e8re", None))

    # retranslateUi

    def conf(self):
            self.id = self.entreprise.class_entreprise.inserer()

            print(self.rc_md.mandat.mandat_id)
            self.client.init(self.id,int(self.code_postale.text()),self.rc_md.RC.rc_id,self.wilaya.text(),self.statut_juridique.text(),self.rc_md.mandat.mandat_id,self.num_succursale.text(),self.num_nif.text(),self.num_nis.text(),self.num_art_imposition.text())
            self.rc_md.mandat.inserer()
            self.rc_md.RC.inserer()
            self.client.inserer()
            self.form.hide()
    def info_entr(self):
            self.form2.show()
    def info_rcmd(self):
            self.form3.show()
    def retour(self):
            self.form.hide()