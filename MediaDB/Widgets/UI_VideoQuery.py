# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoQueryPsLllx.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_VideoForm(object):
    def setupUi(self, VideoForm):
        if not VideoForm.objectName():
            VideoForm.setObjectName(u"VideoForm")
        VideoForm.setWindowModality(Qt.WindowModality.NonModal)
        VideoForm.setEnabled(True)
        VideoForm.resize(301, 352)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(VideoForm.sizePolicy().hasHeightForWidth())
        VideoForm.setSizePolicy(sizePolicy)
        VideoForm.setMinimumSize(QSize(301, 352))
        VideoForm.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.layoutWidget = QWidget(VideoForm)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 289, 331))
        self.MainVerticalLayout = QVBoxLayout(self.layoutWidget)
        self.MainVerticalLayout.setSpacing(10)
        self.MainVerticalLayout.setObjectName(u"MainVerticalLayout")
        self.MainVerticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.MainVerticalLayout.setContentsMargins(2, 2, 0, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CancelButton = QPushButton(self.layoutWidget)
        self.CancelButton.setObjectName(u"CancelButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy1)
        self.CancelButton.setMinimumSize(QSize(0, 0))
        self.CancelButton.setSizeIncrement(QSize(0, 0))
        self.CancelButton.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setStrikeOut(False)
        self.CancelButton.setFont(font)
        self.CancelButton.setAutoFillBackground(False)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.CancelButton.setIcon(icon)
        self.CancelButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.CancelButton)

        self.horizontalSpacer = QSpacerItem(200, 15, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.MainVerticalLayout.addLayout(self.horizontalLayout)

        self.MainLabel = QLabel(self.layoutWidget)
        self.MainLabel.setObjectName(u"MainLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.MainLabel.sizePolicy().hasHeightForWidth())
        self.MainLabel.setSizePolicy(sizePolicy2)
        self.MainLabel.setBaseSize(QSize(2, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.MainLabel.setFont(font1)
        self.MainLabel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.MainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.MainVerticalLayout.addWidget(self.MainLabel)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Name_Label = QLabel(self.layoutWidget)
        self.Name_Label.setObjectName(u"Name_Label")

        self.verticalLayout_3.addWidget(self.Name_Label)

        self.Name_LineEdit = QLineEdit(self.layoutWidget)
        self.Name_LineEdit.setObjectName(u"Name_LineEdit")

        self.verticalLayout_3.addWidget(self.Name_LineEdit)


        self.MainVerticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Type_Label = QLabel(self.layoutWidget)
        self.Type_Label.setObjectName(u"Type_Label")

        self.verticalLayout_2.addWidget(self.Type_Label)

        self.Type_ComboBox = QComboBox(self.layoutWidget)
        self.Type_ComboBox.setObjectName(u"Type_ComboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Type_ComboBox.sizePolicy().hasHeightForWidth())
        self.Type_ComboBox.setSizePolicy(sizePolicy3)
        self.Type_ComboBox.setEditable(True)
        self.Type_ComboBox.setMaxVisibleItems(5)

        self.verticalLayout_2.addWidget(self.Type_ComboBox)


        self.MainVerticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Recommendation_Label = QLabel(self.layoutWidget)
        self.Recommendation_Label.setObjectName(u"Recommendation_Label")

        self.verticalLayout_4.addWidget(self.Recommendation_Label)

        self.Recommendation_LineEdit = QLineEdit(self.layoutWidget)
        self.Recommendation_LineEdit.setObjectName(u"Recommendation_LineEdit")

        self.verticalLayout_4.addWidget(self.Recommendation_LineEdit)


        self.MainVerticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Tags_Label = QLabel(self.layoutWidget)
        self.Tags_Label.setObjectName(u"Tags_Label")

        self.verticalLayout_5.addWidget(self.Tags_Label)

        self.Tags_LineEdit = QLineEdit(self.layoutWidget)
        self.Tags_LineEdit.setObjectName(u"Tags_LineEdit")

        self.verticalLayout_5.addWidget(self.Tags_LineEdit)


        self.MainVerticalLayout.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ApplySubmitButton = QPushButton(self.layoutWidget)
        self.ApplySubmitButton.setObjectName(u"ApplySubmitButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ApplySubmitButton.sizePolicy().hasHeightForWidth())
        self.ApplySubmitButton.setSizePolicy(sizePolicy4)
        self.ApplySubmitButton.setSizeIncrement(QSize(1, 0))
        self.ApplySubmitButton.setBaseSize(QSize(1, 1))
        font2 = QFont()
        font2.setBold(True)
        self.ApplySubmitButton.setFont(font2)

        self.horizontalLayout_5.addWidget(self.ApplySubmitButton)

        self.AcceptSubmitButton = QPushButton(self.layoutWidget)
        self.AcceptSubmitButton.setObjectName(u"AcceptSubmitButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.AcceptSubmitButton.sizePolicy().hasHeightForWidth())
        self.AcceptSubmitButton.setSizePolicy(sizePolicy5)
        self.AcceptSubmitButton.setSizeIncrement(QSize(1, 0))
        self.AcceptSubmitButton.setBaseSize(QSize(1, 0))
        self.AcceptSubmitButton.setFont(font2)
        self.AcceptSubmitButton.setAutoDefault(True)

        self.horizontalLayout_5.addWidget(self.AcceptSubmitButton)


        self.MainVerticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(VideoForm)

        self.CancelButton.setDefault(False)
        self.AcceptSubmitButton.setDefault(True)


        QMetaObject.connectSlotsByName(VideoForm)
    # setupUi

    def retranslateUi(self, VideoForm):
        VideoForm.setWindowTitle(QCoreApplication.translate("VideoForm", u"Video entry form", None))
        self.CancelButton.setText(QCoreApplication.translate("VideoForm", u"Return", None))
#if QT_CONFIG(shortcut)
        self.CancelButton.setShortcut(QCoreApplication.translate("VideoForm", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.MainLabel.setText(QCoreApplication.translate("VideoForm", u"Video entry form", None))
        self.Name_Label.setText(QCoreApplication.translate("VideoForm", u"Name:", None))
        self.Type_Label.setText(QCoreApplication.translate("VideoForm", u"Type:", None))
        self.Recommendation_Label.setText(QCoreApplication.translate("VideoForm", u"Recommended by:", None))
        self.Tags_Label.setText(QCoreApplication.translate("VideoForm", u"Tags:", None))
        self.ApplySubmitButton.setText(QCoreApplication.translate("VideoForm", u"Apply", None))
        self.AcceptSubmitButton.setText(QCoreApplication.translate("VideoForm", u"Accept", None))
#if QT_CONFIG(shortcut)
        self.AcceptSubmitButton.setShortcut(QCoreApplication.translate("VideoForm", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

