# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutWindowUMkoyx.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(518, 284)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        AboutDialog.setAcceptDrops(False)
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AboutLabel = QLabel(AboutDialog)
        self.AboutLabel.setObjectName(u"AboutLabel")
        self.AboutLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.AboutLabel)

        self.AboutAcceptButton = QPushButton(AboutDialog)
        self.AboutAcceptButton.setObjectName(u"AboutAcceptButton")
        font = QFont()
        font.setBold(True)
        font.setKerning(True)
        self.AboutAcceptButton.setFont(font)
        self.AboutAcceptButton.setAutoRepeat(False)
        self.AboutAcceptButton.setAutoExclusive(False)
        self.AboutAcceptButton.setAutoDefault(False)
        self.AboutAcceptButton.setFlat(False)

        self.verticalLayout.addWidget(self.AboutAcceptButton, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(AboutDialog)

        self.AboutAcceptButton.setDefault(True)


        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.AboutLabel.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">About the App</span></h1><p>Media Database is a learning project application designed to help organize the media that you plan to watch/listen in the future, organizing it by different criteria that can be searched later. </p><p>A key aspect is the ability to recommend you what to watch based on the criteria that you are interested in that moment, so you dont have to spend countless hours deciding. </p><h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700;\">License</span></h2><p>This application is licensed under the GNU Lesser General Public License (LGPL). For more information, please visit the <a href=\"https://www.gnu.org/licenses/lgpl-3.0.html\"><span style=\" text-decoration: underline; color"
                        ":#0078d7;\">LGPL License Page</span></a>.</p></body></html>", None))
        self.AboutAcceptButton.setText(QCoreApplication.translate("AboutDialog", u"Accept", None))
#if QT_CONFIG(shortcut)
        self.AboutAcceptButton.setShortcut(QCoreApplication.translate("AboutDialog", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

