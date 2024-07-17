# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ItemInfotBuqkR.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ItemInfoWidget(object):
    def setupUi(self, ItemInfoWidget):
        if not ItemInfoWidget.objectName():
            ItemInfoWidget.setObjectName(u"ItemInfoWidget")
        ItemInfoWidget.resize(256, 313)
        self.verticalLayout_2 = QVBoxLayout(ItemInfoWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(ItemInfoWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.NameLabelInfo = QLabel(self.groupBox)
        self.NameLabelInfo.setObjectName(u"NameLabelInfo")
        font = QFont()
        font.setPointSize(10)
        self.NameLabelInfo.setFont(font)

        self.verticalLayout.addWidget(self.NameLabelInfo)

        self.NameLineEditInfo = QLineEdit(self.groupBox)
        self.NameLineEditInfo.setObjectName(u"NameLineEditInfo")
        self.NameLineEditInfo.setFont(font)
        self.NameLineEditInfo.setReadOnly(True)

        self.verticalLayout.addWidget(self.NameLineEditInfo)

        self.TypeLabelInfo = QLabel(self.groupBox)
        self.TypeLabelInfo.setObjectName(u"TypeLabelInfo")
        self.TypeLabelInfo.setFont(font)

        self.verticalLayout.addWidget(self.TypeLabelInfo)

        self.TypeLineEditInfo = QLineEdit(self.groupBox)
        self.TypeLineEditInfo.setObjectName(u"TypeLineEditInfo")
        self.TypeLineEditInfo.setFont(font)
        self.TypeLineEditInfo.setReadOnly(True)

        self.verticalLayout.addWidget(self.TypeLineEditInfo)

        self.ReccLabelInfo = QLabel(self.groupBox)
        self.ReccLabelInfo.setObjectName(u"ReccLabelInfo")
        self.ReccLabelInfo.setFont(font)

        self.verticalLayout.addWidget(self.ReccLabelInfo)

        self.ReccLineEditInfo = QLineEdit(self.groupBox)
        self.ReccLineEditInfo.setObjectName(u"ReccLineEditInfo")
        self.ReccLineEditInfo.setFont(font)
        self.ReccLineEditInfo.setReadOnly(True)

        self.verticalLayout.addWidget(self.ReccLineEditInfo)

        self.TagsLabelInfo = QLabel(self.groupBox)
        self.TagsLabelInfo.setObjectName(u"TagsLabelInfo")
        self.TagsLabelInfo.setFont(font)

        self.verticalLayout.addWidget(self.TagsLabelInfo)

        self.TagsLineEditInfo = QLineEdit(self.groupBox)
        self.TagsLineEditInfo.setObjectName(u"TagsLineEditInfo")
        self.TagsLineEditInfo.setFont(font)
        self.TagsLineEditInfo.setReadOnly(True)
        self.TagsLineEditInfo.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.TagsLineEditInfo)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(ItemInfoWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(ItemInfoWidget)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(ItemInfoWidget)
    # setupUi

    def retranslateUi(self, ItemInfoWidget):
        ItemInfoWidget.setWindowTitle(QCoreApplication.translate("ItemInfoWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("ItemInfoWidget", u"Info", None))
        self.NameLabelInfo.setText(QCoreApplication.translate("ItemInfoWidget", u"Name:", None))
        self.TypeLabelInfo.setText(QCoreApplication.translate("ItemInfoWidget", u"Type:", None))
        self.ReccLabelInfo.setText(QCoreApplication.translate("ItemInfoWidget", u"Recommended by:", None))
        self.TagsLabelInfo.setText(QCoreApplication.translate("ItemInfoWidget", u"Tags:", None))
        self.pushButton.setText(QCoreApplication.translate("ItemInfoWidget", u"Return", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("ItemInfoWidget", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

