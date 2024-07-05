# Contains both the code for the UI and the code for the Table function
#  -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designereEOVLe.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainTableWidget(object):
    def setupUi(self, MainTableWidget):
        if not MainTableWidget.objectName():
            MainTableWidget.setObjectName(u"MainTableWidget")
        MainTableWidget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(MainTableWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainTable = QTableView(MainTableWidget)
        self.MainTable.setObjectName(u"MainTable")

        self.verticalLayout.addWidget(self.MainTable)

        self.retranslateUi(MainTableWidget)

        QMetaObject.connectSlotsByName(MainTableWidget)
    # setupUi

    def retranslateUi(self, MainTableWidget):
        MainTableWidget.setWindowTitle(QCoreApplication.translate("MainTableWidget", u"Form", None))
    # retranslateUi

