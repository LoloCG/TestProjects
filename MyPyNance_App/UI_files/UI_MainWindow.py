# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sidebar v1XRPebb.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import MW_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(783, 524)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.SideIconQWidget = QWidget(self.centralwidget)
        self.SideIconQWidget.setObjectName(u"SideIconQWidget")
        self.SideIconQWidget.setMinimumSize(QSize(60, 450))
        self.SideIconQWidget.setMaximumSize(QSize(60, 500))
        self.SideIconQWidget.setBaseSize(QSize(60, 0))
        self.verticalLayout_3 = QVBoxLayout(self.SideIconQWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 0, 5)
        self.Logo1 = QLabel(self.SideIconQWidget)
        self.Logo1.setObjectName(u"Logo1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo1.sizePolicy().hasHeightForWidth())
        self.Logo1.setSizePolicy(sizePolicy)
        self.Logo1.setMinimumSize(QSize(50, 50))
        self.Logo1.setMaximumSize(QSize(50, 50))
        self.Logo1.setBaseSize(QSize(50, 50))
        self.Logo1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Logo1.setPixmap(QPixmap(u":/MainIcon/MainIcon.jpg"))
        self.Logo1.setScaledContents(True)
        self.Logo1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Logo1.setMargin(0)

        self.verticalLayout_3.addWidget(self.Logo1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 4, -1, -1)
        self.SidebarButton = QPushButton(self.SideIconQWidget)
        self.SidebarButton.setObjectName(u"SidebarButton")
        sizePolicy.setHeightForWidth(self.SidebarButton.sizePolicy().hasHeightForWidth())
        self.SidebarButton.setSizePolicy(sizePolicy)
        self.SidebarButton.setMinimumSize(QSize(50, 25))
        self.SidebarButton.setMaximumSize(QSize(50, 25))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/menu-4-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SidebarButton.setIcon(icon)
        self.SidebarButton.setIconSize(QSize(20, 20))
        self.SidebarButton.setCheckable(True)
        self.SidebarButton.setChecked(False)
        self.SidebarButton.setAutoExclusive(False)
        self.SidebarButton.setFlat(False)

        self.verticalLayout.addWidget(self.SidebarButton)

        self.HomeSideButton = QPushButton(self.SideIconQWidget)
        self.HomeSideButton.setObjectName(u"HomeSideButton")
        sizePolicy.setHeightForWidth(self.HomeSideButton.sizePolicy().hasHeightForWidth())
        self.HomeSideButton.setSizePolicy(sizePolicy)
        self.HomeSideButton.setMinimumSize(QSize(50, 25))
        self.HomeSideButton.setMaximumSize(QSize(50, 25))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/home-7-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HomeSideButton.setIcon(icon1)
        self.HomeSideButton.setIconSize(QSize(20, 20))
        self.HomeSideButton.setCheckable(True)
        self.HomeSideButton.setAutoExclusive(True)
        self.HomeSideButton.setFlat(False)

        self.verticalLayout.addWidget(self.HomeSideButton)

        self.GraphSideButton = QPushButton(self.SideIconQWidget)
        self.GraphSideButton.setObjectName(u"GraphSideButton")
        sizePolicy.setHeightForWidth(self.GraphSideButton.sizePolicy().hasHeightForWidth())
        self.GraphSideButton.setSizePolicy(sizePolicy)
        self.GraphSideButton.setMinimumSize(QSize(50, 25))
        self.GraphSideButton.setMaximumSize(QSize(50, 25))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/icons/combo-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.GraphSideButton.setIcon(icon2)
        self.GraphSideButton.setIconSize(QSize(20, 20))
        self.GraphSideButton.setCheckable(True)
        self.GraphSideButton.setAutoExclusive(True)
        self.GraphSideButton.setFlat(False)

        self.verticalLayout.addWidget(self.GraphSideButton)

        self.SpendsSideButton = QPushButton(self.SideIconQWidget)
        self.SpendsSideButton.setObjectName(u"SpendsSideButton")
        sizePolicy.setHeightForWidth(self.SpendsSideButton.sizePolicy().hasHeightForWidth())
        self.SpendsSideButton.setSizePolicy(sizePolicy)
        self.SpendsSideButton.setMinimumSize(QSize(50, 25))
        self.SpendsSideButton.setMaximumSize(QSize(50, 25))
        self.SpendsSideButton.setSizeIncrement(QSize(50, 25))
        self.SpendsSideButton.setBaseSize(QSize(50, 25))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/icons/banknotes-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SpendsSideButton.setIcon(icon3)
        self.SpendsSideButton.setIconSize(QSize(20, 20))
        self.SpendsSideButton.setCheckable(True)
        self.SpendsSideButton.setAutoExclusive(True)
        self.SpendsSideButton.setFlat(False)

        self.verticalLayout.addWidget(self.SpendsSideButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.SettingsSideButton = QPushButton(self.SideIconQWidget)
        self.SettingsSideButton.setObjectName(u"SettingsSideButton")
        self.SettingsSideButton.setMinimumSize(QSize(50, 25))
        self.SettingsSideButton.setMaximumSize(QSize(50, 25))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/icons/settings-5-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingsSideButton.setIcon(icon4)
        self.SettingsSideButton.setIconSize(QSize(20, 20))
        self.SettingsSideButton.setCheckable(False)
        self.SettingsSideButton.setFlat(False)

        self.verticalLayout_3.addWidget(self.SettingsSideButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.SideIconQWidget, 0, 0, 1, 1)

        self.SideMenuQWidget = QWidget(self.centralwidget)
        self.SideMenuQWidget.setObjectName(u"SideMenuQWidget")
        sizePolicy.setHeightForWidth(self.SideMenuQWidget.sizePolicy().hasHeightForWidth())
        self.SideMenuQWidget.setSizePolicy(sizePolicy)
        self.SideMenuQWidget.setMinimumSize(QSize(130, 450))
        self.SideMenuQWidget.setMaximumSize(QSize(130, 500))
        self.verticalLayout_4 = QVBoxLayout(self.SideMenuQWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.Logo2 = QLabel(self.SideMenuQWidget)
        self.Logo2.setObjectName(u"Logo2")
        sizePolicy.setHeightForWidth(self.Logo2.sizePolicy().hasHeightForWidth())
        self.Logo2.setSizePolicy(sizePolicy)
        self.Logo2.setMinimumSize(QSize(50, 50))
        self.Logo2.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(6)
        self.Logo2.setFont(font)
        self.Logo2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.Logo2.setPixmap(QPixmap(u":/MainIcon/MainIcon.jpg"))
        self.Logo2.setScaledContents(True)
        self.Logo2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.Logo2)

        self.SidebarLabel = QLabel(self.SideMenuQWidget)
        self.SidebarLabel.setObjectName(u"SidebarLabel")
        sizePolicy.setHeightForWidth(self.SidebarLabel.sizePolicy().hasHeightForWidth())
        self.SidebarLabel.setSizePolicy(sizePolicy)
        self.SidebarLabel.setMinimumSize(QSize(75, 50))
        self.SidebarLabel.setMaximumSize(QSize(75, 50))
        font1 = QFont()
        font1.setFamilies([u"Sitka Small"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.SidebarLabel.setFont(font1)
        self.SidebarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.SidebarLabel)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 4, -1, -1)
        self.SidebarButton2 = QPushButton(self.SideMenuQWidget)
        self.SidebarButton2.setObjectName(u"SidebarButton2")
        self.SidebarButton2.setMinimumSize(QSize(90, 25))
        self.SidebarButton2.setMaximumSize(QSize(90, 25))
        self.SidebarButton2.setIcon(icon)
        self.SidebarButton2.setIconSize(QSize(20, 16))
        self.SidebarButton2.setCheckable(True)
        self.SidebarButton2.setChecked(False)
        self.SidebarButton2.setAutoExclusive(False)
        self.SidebarButton2.setFlat(False)

        self.verticalLayout_2.addWidget(self.SidebarButton2)

        self.HomeSideButton2 = QPushButton(self.SideMenuQWidget)
        self.HomeSideButton2.setObjectName(u"HomeSideButton2")
        self.HomeSideButton2.setMinimumSize(QSize(90, 25))
        self.HomeSideButton2.setMaximumSize(QSize(90, 25))
        self.HomeSideButton2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.HomeSideButton2.setIcon(icon1)
        self.HomeSideButton2.setCheckable(True)
        self.HomeSideButton2.setAutoExclusive(True)
        self.HomeSideButton2.setFlat(False)

        self.verticalLayout_2.addWidget(self.HomeSideButton2)

        self.GraphSideButton2 = QPushButton(self.SideMenuQWidget)
        self.GraphSideButton2.setObjectName(u"GraphSideButton2")
        self.GraphSideButton2.setMinimumSize(QSize(90, 25))
        self.GraphSideButton2.setMaximumSize(QSize(90, 25))
        self.GraphSideButton2.setIcon(icon2)
        self.GraphSideButton2.setCheckable(True)
        self.GraphSideButton2.setAutoExclusive(True)
        self.GraphSideButton2.setFlat(False)

        self.verticalLayout_2.addWidget(self.GraphSideButton2)

        self.SpendsSideButton2 = QPushButton(self.SideMenuQWidget)
        self.SpendsSideButton2.setObjectName(u"SpendsSideButton2")
        self.SpendsSideButton2.setMinimumSize(QSize(90, 25))
        self.SpendsSideButton2.setMaximumSize(QSize(90, 25))
        self.SpendsSideButton2.setIcon(icon3)
        self.SpendsSideButton2.setIconSize(QSize(16, 16))
        self.SpendsSideButton2.setCheckable(True)
        self.SpendsSideButton2.setAutoExclusive(True)
        self.SpendsSideButton2.setFlat(False)

        self.verticalLayout_2.addWidget(self.SpendsSideButton2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.SettingsSideButton2 = QPushButton(self.SideMenuQWidget)
        self.SettingsSideButton2.setObjectName(u"SettingsSideButton2")
        self.SettingsSideButton2.setMinimumSize(QSize(90, 25))
        self.SettingsSideButton2.setMaximumSize(QSize(90, 25))
        self.SettingsSideButton2.setIcon(icon4)
        self.SettingsSideButton2.setFlat(False)

        self.verticalLayout_4.addWidget(self.SettingsSideButton2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.SideMenuQWidget, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.CentralQWidget = QWidget(self.centralwidget)
        self.CentralQWidget.setObjectName(u"CentralQWidget")
        self.gridLayout_2 = QGridLayout(self.CentralQWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.CentralQWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.verticalLayout_5 = QVBoxLayout(self.HomePage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.HomePageLabel = QLabel(self.HomePage)
        self.HomePageLabel.setObjectName(u"HomePageLabel")
        font2 = QFont()
        font2.setPointSize(28)
        self.HomePageLabel.setFont(font2)
        self.HomePageLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.HomePageLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.HomePageLabel.setLineWidth(1)
        self.HomePageLabel.setMidLineWidth(0)
        self.HomePageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.HomePageLabel)

        self.stackedWidget.addWidget(self.HomePage)
        self.SpendsPage = QWidget()
        self.SpendsPage.setObjectName(u"SpendsPage")
        self.verticalLayout_6 = QVBoxLayout(self.SpendsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.SpendsPageLabel = QLabel(self.SpendsPage)
        self.SpendsPageLabel.setObjectName(u"SpendsPageLabel")
        self.SpendsPageLabel.setFont(font2)
        self.SpendsPageLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.SpendsPageLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.SpendsPageLabel.setLineWidth(1)
        self.SpendsPageLabel.setMidLineWidth(0)
        self.SpendsPageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.SpendsPageLabel)

        self.stackedWidget.addWidget(self.SpendsPage)
        self.GraphPage = QWidget()
        self.GraphPage.setObjectName(u"GraphPage")
        self.verticalLayout_7 = QVBoxLayout(self.GraphPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.GraphPageLabel = QLabel(self.GraphPage)
        self.GraphPageLabel.setObjectName(u"GraphPageLabel")
        self.GraphPageLabel.setFont(font2)
        self.GraphPageLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.GraphPageLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.GraphPageLabel.setLineWidth(1)
        self.GraphPageLabel.setMidLineWidth(0)
        self.GraphPageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.GraphPageLabel)

        self.stackedWidget.addWidget(self.GraphPage)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.CentralQWidget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.HomeSideButton.toggled.connect(self.HomeSideButton2.setChecked)
        self.GraphSideButton.toggled.connect(self.GraphSideButton2.setChecked)
        self.SpendsSideButton.toggled.connect(self.SpendsSideButton2.setChecked)
        self.HomeSideButton2.toggled.connect(self.HomeSideButton.setChecked)
        self.GraphSideButton2.toggled.connect(self.GraphSideButton.setChecked)
        self.SpendsSideButton2.toggled.connect(self.SpendsSideButton.setChecked)
        self.SidebarButton2.toggled.connect(self.SideMenuQWidget.setVisible)
        self.SidebarButton2.toggled.connect(self.SideIconQWidget.setHidden)
        self.SidebarButton.toggled.connect(self.SideMenuQWidget.setVisible)
        self.SidebarButton.toggled.connect(self.SideIconQWidget.setHidden)
        self.SettingsSideButton.toggled.connect(self.SettingsSideButton2.click)
        self.SettingsSideButton2.toggled.connect(self.SettingsSideButton.click)
        self.SidebarButton2.toggled.connect(self.SidebarButton.setChecked)
        self.SidebarButton.toggled.connect(self.SidebarButton2.setChecked)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SidebarButton.setText("")
        self.HomeSideButton.setText("")
        self.GraphSideButton.setText("")
        self.SpendsSideButton.setText("")
        self.SettingsSideButton.setText("")
        self.Logo2.setText("")
        self.SidebarLabel.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.SidebarButton2.setText("")
        self.HomeSideButton2.setText(QCoreApplication.translate("MainWindow", u"Home page", None))
        self.GraphSideButton2.setText(QCoreApplication.translate("MainWindow", u"Graphs", None))
        self.SpendsSideButton2.setText(QCoreApplication.translate("MainWindow", u"Spends", None))
        self.SettingsSideButton2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.HomePageLabel.setText(QCoreApplication.translate("MainWindow", u"Home page", None))
        self.SpendsPageLabel.setText(QCoreApplication.translate("MainWindow", u"Spends page", None))
        self.GraphPageLabel.setText(QCoreApplication.translate("MainWindow", u"Graph page", None))
    # retranslateUi

