# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowbUDXkZ.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainAppWindow(object):
    def setupUi(self, MainAppWindow):
        if not MainAppWindow.objectName():
            MainAppWindow.setObjectName(u"MainAppWindow")
        MainAppWindow.resize(509, 358)
        self.MusicQueryMenuButton = QAction(MainAppWindow)
        self.MusicQueryMenuButton.setObjectName(u"MusicQueryMenuButton")
        self.MusicQueryMenuButton.setEnabled(False)
        self.VideoQueryMenuButton = QAction(MainAppWindow)
        self.VideoQueryMenuButton.setObjectName(u"VideoQueryMenuButton")
        self.actionSeries = QAction(MainAppWindow)
        self.actionSeries.setObjectName(u"actionSeries")
        self.DarkThemeAction = QAction(MainAppWindow)
        self.DarkThemeAction.setObjectName(u"DarkThemeAction")
        self.DarkThemeAction.setCheckable(True)
        self.DarkThemeAction.setChecked(False)
        self.LightThemeAction = QAction(MainAppWindow)
        self.LightThemeAction.setObjectName(u"LightThemeAction")
        self.LightThemeAction.setCheckable(True)
        self.AboutMenuButton = QAction(MainAppWindow)
        self.AboutMenuButton.setObjectName(u"AboutMenuButton")
        self.AboutMenuButton.setCheckable(False)
        self.AboutMenuButton.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.Delete_selectedMenuButton = QAction(MainAppWindow)
        self.Delete_selectedMenuButton.setObjectName(u"Delete_selectedMenuButton")
        self.NeonThemeAction = QAction(MainAppWindow)
        self.NeonThemeAction.setObjectName(u"NeonThemeAction")
        self.NeonThemeAction.setCheckable(True)
        self.CentralWidget = QWidget(MainAppWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.verticalLayout = QVBoxLayout(self.CentralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainWindowLabel = QLabel(self.CentralWidget)
        self.MainWindowLabel.setObjectName(u"MainWindowLabel")
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold"])
        font.setPointSize(16)
        font.setBold(True)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.MainWindowLabel.setFont(font)
        self.MainWindowLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MainWindowLabel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.MainWindowLabel.setFrameShape(QFrame.Shape.NoFrame)
        self.MainWindowLabel.setFrameShadow(QFrame.Shadow.Plain)
        self.MainWindowLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.MainWindowLabel)

        self.verticalSpacer = QSpacerItem(1, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SearchLineEdit = QLineEdit(self.CentralWidget)
        self.SearchLineEdit.setObjectName(u"SearchLineEdit")
        self.SearchLineEdit.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.SearchLineEdit)

        self.SearchButton = QPushButton(self.CentralWidget)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.SearchButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.MainTableWidget = QTableWidget(self.CentralWidget)
        self.MainTableWidget.setObjectName(u"MainTableWidget")
        self.MainTableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MainTableWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.MainTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.MainTableWidget.setDragDropOverwriteMode(False)
        self.MainTableWidget.setAlternatingRowColors(True)
        self.MainTableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.MainTableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.MainTableWidget.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.MainTableWidget.setShowGrid(False)
        self.MainTableWidget.setSortingEnabled(True)
        self.MainTableWidget.setWordWrap(False)
        self.MainTableWidget.horizontalHeader().setStretchLastSection(False)
        self.MainTableWidget.verticalHeader().setVisible(True)
        self.MainTableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.MainTableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AddNewButton = QPushButton(self.CentralWidget)
        self.AddNewButton.setObjectName(u"AddNewButton")

        self.horizontalLayout.addWidget(self.AddNewButton)

        self.PrintSelectedButton = QPushButton(self.CentralWidget)
        self.PrintSelectedButton.setObjectName(u"PrintSelectedButton")

        self.horizontalLayout.addWidget(self.PrintSelectedButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Show_RandomButton = QPushButton(self.CentralWidget)
        self.Show_RandomButton.setObjectName(u"Show_RandomButton")

        self.verticalLayout.addWidget(self.Show_RandomButton)

        MainAppWindow.setCentralWidget(self.CentralWidget)
        self.menuBar = QMenuBar(MainAppWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 509, 22))
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.ThemeMenuButton = QMenu(self.menuSettings)
        self.ThemeMenuButton.setObjectName(u"ThemeMenuButton")
        self.ThemeMenuButton.setEnabled(True)
        self.menuAdd_new = QMenu(self.menuBar)
        self.menuAdd_new.setObjectName(u"menuAdd_new")
        MainAppWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuAdd_new.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.AboutMenuButton)
        self.menuSettings.addAction(self.ThemeMenuButton.menuAction())
        self.ThemeMenuButton.addAction(self.DarkThemeAction)
        self.ThemeMenuButton.addAction(self.LightThemeAction)
        self.ThemeMenuButton.addAction(self.NeonThemeAction)
        self.menuAdd_new.addAction(self.Delete_selectedMenuButton)
        self.menuAdd_new.addAction(self.VideoQueryMenuButton)
        self.menuAdd_new.addAction(self.MusicQueryMenuButton)

        self.retranslateUi(MainAppWindow)

        QMetaObject.connectSlotsByName(MainAppWindow)
    # setupUi

    def retranslateUi(self, MainAppWindow):
        MainAppWindow.setWindowTitle(QCoreApplication.translate("MainAppWindow", u"MainWindow", None))
        self.MusicQueryMenuButton.setText(QCoreApplication.translate("MainAppWindow", u"Music", None))
        self.VideoQueryMenuButton.setText(QCoreApplication.translate("MainAppWindow", u"Add Film/Series", None))
        self.actionSeries.setText(QCoreApplication.translate("MainAppWindow", u"Series", None))
        self.DarkThemeAction.setText(QCoreApplication.translate("MainAppWindow", u"Dark Theme", None))
        self.LightThemeAction.setText(QCoreApplication.translate("MainAppWindow", u"Light Theme", None))
        self.AboutMenuButton.setText(QCoreApplication.translate("MainAppWindow", u"About", None))
        self.Delete_selectedMenuButton.setText(QCoreApplication.translate("MainAppWindow", u"Delete selected", None))
#if QT_CONFIG(shortcut)
        self.Delete_selectedMenuButton.setShortcut(QCoreApplication.translate("MainAppWindow", u"Ctrl+Del", None))
#endif // QT_CONFIG(shortcut)
        self.NeonThemeAction.setText(QCoreApplication.translate("MainAppWindow", u"Neon Theme", None))
        self.MainWindowLabel.setText(QCoreApplication.translate("MainAppWindow", u"Media DataBase", None))
        self.SearchButton.setText(QCoreApplication.translate("MainAppWindow", u"Search", None))
        self.AddNewButton.setText(QCoreApplication.translate("MainAppWindow", u"Add New", None))
        self.PrintSelectedButton.setText(QCoreApplication.translate("MainAppWindow", u"Print Selected", None))
        self.Show_RandomButton.setText(QCoreApplication.translate("MainAppWindow", u"Show Random", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainAppWindow", u"Settings", None))
        self.ThemeMenuButton.setTitle(QCoreApplication.translate("MainAppWindow", u"Theme", None))
        self.menuAdd_new.setTitle(QCoreApplication.translate("MainAppWindow", u"Media", None))
    # retranslateUi

