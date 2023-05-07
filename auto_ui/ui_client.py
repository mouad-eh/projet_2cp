# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientQtwUyW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from auto_ui.ui_nv_client import *
from datetime import *
class Ui_client(object):
    def __init__(self):
        self.form = QWidget()
        self.setupUi(self.form)
        self.ajouter.clicked.connect(self.pushed)
        self.loaddata()
        self.rafraichir.clicked.connect(self.loaddata)
       # self.recherche.
        self.valider.clicked.connect(self.valid)
        self.modifier.clicked.connect(self.modif)
        self.supprimer.clicked.connect(self.supp)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(868, 691)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,0.3);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.utilisateurClientFrame = QFrame(self.frame)
        self.utilisateurClientFrame.setObjectName(u"utilisateurClientFrame")
        self.utilisateurClientFrame.setStyleSheet(u"\n"
                                                  "background-color: #2f3e46;\n"
                                                  "color: white;")
        self.utilisateurClientFrame.setFrameShape(QFrame.StyledPanel)
        self.utilisateurClientFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.utilisateurClientFrame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 10, 5, 10)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.nutilisateurLabel = QLabel(self.utilisateurClientFrame)
        self.nutilisateurLabel.setObjectName(u"nutilisateurLabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nutilisateurLabel.setFont(font)
        self.nutilisateurLabel.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.nutilisateurLabel, 0, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_27.addWidget(self.utilisateurClientFrame, 0, 0, 1, 1)

        self.subTabsFrame = QFrame(self.frame)
        self.subTabsFrame.setObjectName(u"subTabsFrame")
        self.subTabsFrame.setFrameShape(QFrame.StyledPanel)
        self.subTabsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.subTabsFrame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.subTabsFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 76))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.scrollArea.setPalette(palette)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 862, 637))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        font1 = QFont()
        font1.setFamily(u"Roman")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.frame_2.setFont(font1)
        self.frame_2.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_2.setStyleSheet(u"background-color: rgba(255,255,255,0.3);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.liste = QTableWidget(self.frame_2)
        if (self.liste.columnCount() < 5):
            self.liste.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.liste.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.liste.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.liste.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.liste.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.liste.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.liste.rowCount() < 21):
            self.liste.setRowCount(21)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.liste.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.liste.setVerticalHeaderItem(1, __qtablewidgetitem6)
        brush6 = QBrush(QColor(255, 170, 127, 255))
        brush6.setStyle(Qt.NoBrush)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setForeground(brush6);
        self.liste.setItem(0, 0, __qtablewidgetitem7)
        self.liste.setObjectName(u"liste")
        self.liste.setMinimumSize(QSize(321, 0))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.liste.setFont(font2)
        self.liste.setStyleSheet(u"\n"
                                 "background-color: white;\n"
                                 "color: #52796f;\n"
                                 "selection-background-color: #a2d2ff;\n"
                                 "selection-color:#2f3e46;\n"
                                 "border-radius: 10px;\n"
                                 "")
        self.liste.setTabKeyNavigation(False)
        self.liste.setProperty("showDropIndicator", False)
        self.liste.setDragDropOverwriteMode(False)
        self.liste.setAlternatingRowColors(False)
        self.liste.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.liste.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.liste.setGridStyle(Qt.SolidLine)
        self.liste.horizontalHeader().setMinimumSectionSize(33)
        self.liste.horizontalHeader().setDefaultSectionSize(100)
        self.liste.horizontalHeader().setStretchLastSection(True)
        self.liste.verticalHeader().setVisible(False)
        self.liste.verticalHeader().setMinimumSectionSize(25)
        self.liste.verticalHeader().setDefaultSectionSize(35)

        self.gridLayout_7.addWidget(self.liste, 1, 2, 1, 1)

        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.recherche = QLineEdit(self.frame_2)
        self.recherche.setObjectName(u"recherche")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recherche.sizePolicy().hasHeightForWidth())
        self.recherche.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        brush7 = QBrush(QColor(47, 62, 70, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush8 = QBrush(QColor(47, 62, 70, 128))
        brush8.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
        # endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush9 = QBrush(QColor(47, 62, 70, 128))
        brush9.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
        # endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush10 = QBrush(QColor(47, 62, 70, 128))
        brush10.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
        # endif
        self.recherche.setPalette(palette1)
        font3 = QFont()
        font3.setFamily(u"MS Sans Serif")
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        font3.setKerning(False)
        self.recherche.setFont(font3)
        self.recherche.setTabletTracking(False)
        self.recherche.setFocusPolicy(Qt.StrongFocus)
        self.recherche.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.recherche.setStyleSheet(u"background-color: white;\n"
                                     "color: #2f3e46;\n"
                                     "padding: 1px;\n"
                                     "border : 1px solid #52796f;\n"
                                     "border-radius: 10px;")
        self.recherche.setInputMethodHints(Qt.ImhNone)
        self.recherche.setFrame(True)
        self.recherche.setCursorPosition(0)
        self.recherche.setDragEnabled(False)
        self.recherche.setReadOnly(False)
        self.recherche.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.recherche.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.recherche)

        self.gridLayout_8.addLayout(self.horizontalLayout_2, 0, 1, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rechercher = QLabel(self.frame_2)
        self.rechercher.setObjectName(u"rechercher")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rechercher.sizePolicy().hasHeightForWidth())
        self.rechercher.setSizePolicy(sizePolicy1)
        palette2 = QPalette()
        brush11 = QBrush(QColor(82, 121, 111, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        brush12 = QBrush(QColor(82, 121, 111, 128))
        brush12.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
        # endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush13 = QBrush(QColor(82, 121, 111, 128))
        brush13.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
        # endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush14 = QBrush(QColor(82, 121, 111, 128))
        brush14.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
        # endif
        self.rechercher.setPalette(palette2)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setWeight(75)
        self.rechercher.setFont(font4)
        self.rechercher.setCursor(QCursor(Qt.CrossCursor))
        self.rechercher.setMouseTracking(True)
        self.rechercher.setStyleSheet(u"color: #52796f;\n"
                                      "\n"
                                      "")
        self.rechercher.setTextFormat(Qt.AutoText)

        self.horizontalLayout_3.addWidget(self.rechercher)

        self.gridLayout_8.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 8, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.modifier = QPushButton(self.frame_2)
        self.modifier.setObjectName(u"modifier")
        palette3 = QPalette()
        brush15 = QBrush(QColor(59, 178, 115, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush15)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush16 = QBrush(QColor(59, 178, 115, 128))
        brush16.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
        # endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush17 = QBrush(QColor(59, 178, 115, 128))
        brush17.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
        # endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush18 = QBrush(QColor(59, 178, 115, 128))
        brush18.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
        # endif
        self.modifier.setPalette(palette3)
        self.modifier.setFont(font2)
        self.modifier.setStyleSheet(u"\n"
                                    "QPushButton {\n"
                                    "background-color: white;\n"
                                    "color: #3bb273;\n"
                                    "padding: 6px;\n"
                                    "border: 2px solid #3bb273;\n"
                                    "border-radius: 10px;\n"
                                    "}\n"
                                    "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                    "QPushButton:pressed { margin: 1px; }\n"
                                    "")

        self.gridLayout_6.addWidget(self.modifier, 4, 1, 1, 1)

        self.valider = QPushButton(self.frame_2)
        self.valider.setObjectName(u"valider")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush15)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush19 = QBrush(QColor(59, 178, 115, 128))
        brush19.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
        # endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush20 = QBrush(QColor(59, 178, 115, 128))
        brush20.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
        # endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush21 = QBrush(QColor(59, 178, 115, 128))
        brush21.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
        # endif
        self.valider.setPalette(palette4)
        self.valider.setFont(font2)
        self.valider.setStyleSheet(u"\n"
                                   "QPushButton {\n"
                                   "background-color: white;\n"
                                   "color: #3bb273;\n"
                                   "padding: 6px;\n"
                                   "border: 2px solid #3bb273;\n"
                                   "border-radius: 10px;\n"
                                   "}\n"
                                   "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                   "QPushButton:pressed { margin: 1px; }\n"
                                   "")

        self.gridLayout_6.addWidget(self.valider, 2, 1, 1, 1)

        self.ajouter = QPushButton(self.frame_2)
        self.ajouter.setObjectName(u"ajouter")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush15)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush22 = QBrush(QColor(59, 178, 115, 128))
        brush22.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
        # endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush23 = QBrush(QColor(59, 178, 115, 128))
        brush23.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush23)
        # endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush24 = QBrush(QColor(59, 178, 115, 128))
        brush24.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush24)
        # endif
        self.ajouter.setPalette(palette5)
        self.ajouter.setFont(font2)
        self.ajouter.setStyleSheet(u"\n"
                                   "QPushButton {\n"
                                   "background-color: white;\n"
                                   "color: #3bb273;\n"
                                   "padding: 6px;\n"
                                   "border: 2px solid #3bb273;\n"
                                   "border-radius: 10px;\n"
                                   "}\n"
                                   "QPushButton:hover {background-color: #3bb273;color: white;}\n"
                                   "QPushButton:pressed { margin: 1px; }\n"
                                   "")

        self.gridLayout_6.addWidget(self.ajouter, 3, 1, 1, 1)

        self.fermer = QPushButton(self.frame_2)
        self.fermer.setObjectName(u"fermer")
        palette6 = QPalette()
        brush25 = QBrush(QColor(238, 46, 49, 255))
        brush25.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush25)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush25)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush25)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush26 = QBrush(QColor(238, 46, 49, 128))
        brush26.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush26)
        # endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush25)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush25)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush25)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush27 = QBrush(QColor(238, 46, 49, 128))
        brush27.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush27)
        # endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush25)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush25)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush25)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush28 = QBrush(QColor(238, 46, 49, 128))
        brush28.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush28)
        # endif
        self.fermer.setPalette(palette6)
        self.fermer.setFont(font2)
        self.fermer.setStyleSheet(u"\n"
                                  "QPushButton {\n"
                                  "background-color: white;\n"
                                  "color: #ee2e31;\n"
                                  "padding: 5px;\n"
                                  "border: 2px solid #ee2e31;\n"
                                  "border-radius: 10px;\n"
                                  "}\n"
                                  "QPushButton:hover {background-color: #ee2e31;color: white;}\n"
                                  "QPushButton:pressed{margin: 1px;}\n"
                                  "")

        self.gridLayout_6.addWidget(self.fermer, 7, 1, 1, 1)

        self.rafraichir = QPushButton(self.frame_2)
        self.rafraichir.setObjectName(u"rafraichir")
        self.rafraichir.setFont(font2)
        self.rafraichir.setStyleSheet(u"\n"
                                      "QPushButton {\n"
                                      "background-color: white;\n"
                                      "color: #3bb273;\n"
                                      "padding: 6px;\n"
                                      "border: 2px solid #3bb273;\n"
                                      "border-radius: 10px;\n"
                                      "}\n"
                                      "QPushButton:hover {background-color: #3bb274;color: white;}\n"
                                      "QPushButton:pressed { margin: 1px; }\n"
                                      "")

        self.gridLayout_6.addWidget(self.rafraichir, 5, 1, 1, 1)

        self.supprimer = QPushButton(self.frame_2)
        self.supprimer.setObjectName(u"supprimer")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush25)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush25)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush25)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush29 = QBrush(QColor(238, 46, 49, 128))
        brush29.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush29)
        # endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush25)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush25)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush25)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush30 = QBrush(QColor(238, 46, 49, 128))
        brush30.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush30)
        # endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush25)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush25)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush25)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush31 = QBrush(QColor(238, 46, 49, 128))
        brush31.setStyle(Qt.NoBrush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush31)
        # endif
        self.supprimer.setPalette(palette7)
        self.supprimer.setFont(font2)
        self.supprimer.setStyleSheet(u"\n"
                                     "QPushButton {\n"
                                     "background-color: white;\n"
                                     "color: #ee2e31;\n"
                                     "padding: 5px;\n"
                                     "border: 2px solid #ee2e31;\n"
                                     "border-radius: 10px;\n"
                                     "}\n"
                                     "QPushButton:hover {background-color: #ee2e31;color: white;}\n"
                                     "QPushButton:pressed{margin: 1px;}\n"
                                     "")

        self.gridLayout_6.addWidget(self.supprimer, 6, 1, 1, 1)

        self.gridLayout_8.addLayout(self.gridLayout_6, 1, 2, 1, 1)

        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.gridLayout_27.addWidget(self.subTabsFrame, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nutilisateurLabel.setText(QCoreApplication.translate("Form", u"CLIENT", None))
        ___qtablewidgetitem = self.liste.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"raison sociale", None));
        ___qtablewidgetitem1 = self.liste.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"expiration mandat", None));
        ___qtablewidgetitem2 = self.liste.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Nbr\\j\\v", None));
        ___qtablewidgetitem3 = self.liste.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Expiration RC", None));
        ___qtablewidgetitem4 = self.liste.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"NBR\\j\\v", None));
        ___qtablewidgetitem5 = self.liste.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem6 = self.liste.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"2", None));

        __sortingEnabled = self.liste.isSortingEnabled()
        self.liste.setSortingEnabled(False)
        self.liste.setSortingEnabled(__sortingEnabled)

        # if QT_CONFIG(tooltip)
        self.recherche.setToolTip(QCoreApplication.translate("Form",
                                                             u"<html><head/><body><p>hhhhhhhhhhhhhhhhhhhhggggg<span style=\" font-weight:600;\">gggg</span></p></body></html>",
                                                             None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.recherche.setWhatsThis(
            QCoreApplication.translate("Form", u"<html><head/><body><p>gggg</p></body></html>", None))
        # endif // QT_CONFIG(whatsthis)
        self.recherche.setText("")
        self.recherche.setPlaceholderText(QCoreApplication.translate("Form", u"   rechercher le nom ici .....", None))
        self.rechercher.setText(QCoreApplication.translate("Form", u"RECHERCHER", None))
        self.modifier.setText(QCoreApplication.translate("Form", u"Modifier", None))
        self.valider.setText(QCoreApplication.translate("Form", u"valider", None))
        self.ajouter.setText(QCoreApplication.translate("Form", u"Ajouter", None))
        self.fermer.setText(QCoreApplication.translate("Form", u"Fermer", None))
        self.rafraichir.setText(QCoreApplication.translate("Form", u"rafraichir", None))
        self.supprimer.setText(QCoreApplication.translate("Form", u"supprimer", None))

    # retranslateUi

    def pushed(self):
        self.form2 = QtWidgets.QWidget()
        self.nv_cl = Ui_ajout_client(self.form2)
        self.form2.show()
    def loaddata(self):
        sql = "SELECT * FROM client"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        tablerow = 0
        self.liste.setRowCount(mycursor.rowcount)
        self.ids = []

        for row in myresult:
            self.ids.append(row[0])
            sql = "SELECT nom FROM entreprise WHERE entreprise_id ="
            sql += str(row[1])
            mycursor.execute(sql)
            var = mycursor.fetchone()
            print(var[0])

            self.liste.setItem(tablerow, 0, QTableWidgetItem(var[0]))
            sql = "SELECT * FROM mandat WHERE mandat_id =  "
            sql += str(row[6])
            mycursor.execute(sql)
            var = mycursor.fetchone()
            sql = "SELECT * FROM document WHERE document_id = "
            sql += str(var[1])
            mycursor.execute(sql,var[1])
            doc_m = mycursor.fetchone()
            sql = "SELECT * FROM rc WHERE rc_id =  "
            sql += str(row[3])
            mycursor.execute(sql)
            var = mycursor.fetchone()
            sql = "SELECT * FROM document WHERE document_id = "
            sql += str(var[1])
            mycursor.execute(sql, var[1])
            doc_RC = mycursor.fetchone()
            alpha = doc_RC[3] - date.today()

            self.liste.setItem(tablerow,1,QTableWidgetItem(doc_RC[3].strftime("%d/%m/%Y")))
            self.liste.setItem(tablerow,2, QTableWidgetItem(str((doc_RC[3] - date.today()).days)))
            self.liste.setItem(tablerow,3,QTableWidgetItem(doc_m[3].strftime("%d/%m/%Y")))
            self.liste.setItem(tablerow,4, QTableWidgetItem(str((doc_m[3] - date.today()).days)))
            tablerow += 1
        print(self.ids)
    def rech(self):
        sql = "SELECT * FROM entreprise WHERE nom LIKE  '"
        sql += self.line_recherche_2.text()
        sql += "%'"

        mycursor.execute(sql)
        var = mycursor.fetchall()
        tablerow = 0
        self.liste.setRowCount(mycursor.rowcount)
        self.liste.clear()
        self.ids =  []
        print(var)
        for row in var:
            print(row[1])

            self.liste.setItem(tablerow, 0, QTableWidgetItem(row[1]))
            sql = "SELECT * FROM client WHERE entreprise_id="
            sql += str(row[0])
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            print(myresult[0])
            self.ids.append(myresult[0])
            sql = "SELECT * FROM mandat WHERE mandat_id =  "
            sql += str(myresult[6])
            mycursor.execute(sql)
            var2 = mycursor.fetchone()
            sql = "SELECT * FROM document WHERE document_id = "
            sql += str(var2[1])
            mycursor.execute(sql, var2[1])
            doc_m = mycursor.fetchone()
            sql = "SELECT * FROM rc WHERE rc_id =  "
            sql += str(myresult[3])
            mycursor.execute(sql)
            var2 = mycursor.fetchone()
            sql = "SELECT * FROM document WHERE document_id = "
            sql += str(var2[1])
            mycursor.execute(sql, var2[1])
            doc_RC = mycursor.fetchone()
            self.liste.setItem(tablerow, 1, QTableWidgetItem(doc_RC[3].strftime("%d/%m/%Y")))
            self.liste.setItem(tablerow, 2, QTableWidgetItem(str((doc_RC[3] - date.today()).days)))
            self.liste.setItem(tablerow, 3, QTableWidgetItem(doc_m[3].strftime("%d/%m/%Y")))
            self.liste.setItem(tablerow, 4, QTableWidgetItem(str((doc_m[3] - date.today()).days)))
            tablerow += 1
        print(self.ids)
    def valid(self):
        row = self.liste.currentRow()


        currentproductid = (self.liste.item(row,0).text())
        self.rowclient = (self.ids[self.liste.currentRow().numerator],currentproductid)
        #print(currentproductid)
        print(self.rowclient)


    def modif(self):
        id =  self.ids[self.liste.currentRow().numerator]
        self.form2 = QtWidgets.QWidget()
        self.nv_cl = Ui_ajout_client(self.form2)
        self.nv_cl.client.importer(id)
        self.nv_cl.line_code_postal.setText(str(self.nv_cl.client.code_postal))
        self.nv_cl.line_wilaya.setText(self.nv_cl.client.wilaya)
        self.nv_cl.line_num_NIS.setText(str(self.nv_cl.client.num_NIS))
        self.nv_cl.line_num_NIF.setText(str(self.nv_cl.client.num_NIF))
        self.nv_cl.line_num_succursale.setText(str(self.nv_cl.client.num_succursale))
        self.nv_cl.line_statut_juridique.setText(self.nv_cl.client.statut_juridique)
        self.nv_cl.line_art_imposition.setText(str(self.nv_cl.client.num_art_imposition))
        self.nv_cl.entreprise.class_entreprise.importer(self.nv_cl.client.entreprise_id)
        self.nv_cl.rc_md
        self.form2.show()
    def supp(self):
        id = self.ids[self.liste.currentRow().numerator]
        sql = "SELECT entreprise_id FROM client WHERE client_id="
        sql += str(id)
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        id_entreprise = myresult[0]
        sql = "DELETE FROM client WHERE client_id="
        sql += str(id)
        mycursor.execute(sql)
        mydb.commit()
        sql = "DELETE FROM entreprise WHERE entreprise_id="
        sql += str(id_entreprise)
        mycursor.execute(sql)
        mydb.commit()
        print("eee")
        self.loaddata()


if __name__ == "__main__":
    app = QApplication()
    widget = Ui_client()
    widget.form.show()
    app.exec_()