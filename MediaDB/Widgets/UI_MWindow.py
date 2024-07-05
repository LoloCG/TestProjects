# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowronrUm.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainAppWindow(object):
    def setupUi(self, MainAppWindow):
        if not MainAppWindow.objectName():
            MainAppWindow.setObjectName(u"MainAppWindow")
        MainAppWindow.resize(508, 354)
        self.actionMusic = QAction(MainAppWindow)
        self.actionMusic.setObjectName(u"actionMusic")
        self.actionMovie = QAction(MainAppWindow)
        self.actionMovie.setObjectName(u"actionMovie")
        self.actionSeries = QAction(MainAppWindow)
        self.actionSeries.setObjectName(u"actionSeries")
        self.actionDark_Theme = QAction(MainAppWindow)
        self.actionDark_Theme.setObjectName(u"actionDark_Theme")
        self.actionDark_Theme.setCheckable(True)
        self.actionLight_Theme = QAction(MainAppWindow)
        self.actionLight_Theme.setObjectName(u"actionLight_Theme")
        self.actionLight_Theme.setCheckable(True)
        self.actionAbout = QAction(MainAppWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setCheckable(False)
        self.actionAbout.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.CentralWidget = QWidget(MainAppWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.verticalLayout = QVBoxLayout(self.CentralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.CentralWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold"])
        font.setPointSize(16)
        font.setBold(True)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.MainWindowPlaceholder = QWidget(self.CentralWidget)
        self.MainWindowPlaceholder.setObjectName(u"MainWindowPlaceholder")
        self.MainWindowPlaceholder.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindowPlaceholder.sizePolicy().hasHeightForWidth())
        self.MainWindowPlaceholder.setSizePolicy(sizePolicy)
        self.MainWindowPlaceholder.setMinimumSize(QSize(0, 0))
        self.MainWindowPlaceholder.setSizeIncrement(QSize(3, 3))
        self.MainWindowPlaceholder.setBaseSize(QSize(2, 2))

        self.verticalLayout.addWidget(self.MainWindowPlaceholder)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MainW_Button1 = QPushButton(self.CentralWidget)
        self.MainW_Button1.setObjectName(u"MainW_Button1")

        self.horizontalLayout.addWidget(self.MainW_Button1)

        self.MainW_Button2 = QPushButton(self.CentralWidget)
        self.MainW_Button2.setObjectName(u"MainW_Button2")

        self.horizontalLayout.addWidget(self.MainW_Button2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SearchLineEdit = QLineEdit(self.CentralWidget)
        self.SearchLineEdit.setObjectName(u"SearchLineEdit")

        self.horizontalLayout_2.addWidget(self.SearchLineEdit)

        self.SearchButton = QPushButton(self.CentralWidget)
        self.SearchButton.setObjectName(u"SearchButton")

        self.horizontalLayout_2.addWidget(self.SearchButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainAppWindow.setCentralWidget(self.CentralWidget)
        self.menuBar = QMenuBar(MainAppWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 508, 22))
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuTheme = QMenu(self.menuSettings)
        self.menuTheme.setObjectName(u"menuTheme")
        self.menuAdd_new = QMenu(self.menuBar)
        self.menuAdd_new.setObjectName(u"menuAdd_new")
        MainAppWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuAdd_new.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.actionAbout)
        self.menuSettings.addAction(self.menuTheme.menuAction())
        self.menuTheme.addAction(self.actionDark_Theme)
        self.menuTheme.addAction(self.actionLight_Theme)
        self.menuAdd_new.addAction(self.actionMusic)
        self.menuAdd_new.addAction(self.actionMovie)

        self.retranslateUi(MainAppWindow)

        QMetaObject.connectSlotsByName(MainAppWindow)
    # setupUi

    def retranslateUi(self, MainAppWindow):
        MainAppWindow.setWindowTitle(QCoreApplication.translate("MainAppWindow", u"MainWindow", None))
        self.actionMusic.setText(QCoreApplication.translate("MainAppWindow", u"Music", None))
        self.actionMovie.setText(QCoreApplication.translate("MainAppWindow", u"Film/Series", None))
        self.actionSeries.setText(QCoreApplication.translate("MainAppWindow", u"Series", None))
        self.actionDark_Theme.setText(QCoreApplication.translate("MainAppWindow", u"Dark Theme", None))
        self.actionLight_Theme.setText(QCoreApplication.translate("MainAppWindow", u"Light Theme", None))
        self.actionAbout.setText(QCoreApplication.translate("MainAppWindow", u"About", None))
        self.label.setText(QCoreApplication.translate("MainAppWindow", u"All Saved Media", None))
        self.MainW_Button1.setText(QCoreApplication.translate("MainAppWindow", u"Button1", None))
        self.MainW_Button2.setText(QCoreApplication.translate("MainAppWindow", u"Button2", None))
        self.SearchButton.setText(QCoreApplication.translate("MainAppWindow", u"Search", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainAppWindow", u"Settings", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainAppWindow", u"Theme", None))
        self.menuAdd_new.setTitle(QCoreApplication.translate("MainAppWindow", u"Add new", None))
    # retranslateUi

