# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoQueryvrdQoo.ui'
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
    QVBoxLayout, QWidget)

class Ui_VideoForm(object):
    def setupUi(self, VideoForm):
        if not VideoForm.objectName():
            VideoForm.setObjectName(u"VideoForm")
        VideoForm.setWindowModality(Qt.WindowModality.NonModal)
        VideoForm.setEnabled(True)
        VideoForm.resize(299, 318)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(VideoForm.sizePolicy().hasHeightForWidth())
        VideoForm.setSizePolicy(sizePolicy)
        VideoForm.setMinimumSize(QSize(280, 297))
        VideoForm.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.widget = QWidget(VideoForm)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 281, 301))
        self.MainVerticalLayout = QVBoxLayout(self.widget)
        self.MainVerticalLayout.setSpacing(10)
        self.MainVerticalLayout.setObjectName(u"MainVerticalLayout")
        self.MainVerticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.MainVerticalLayout.setContentsMargins(2, 2, 0, 2)
        self.MainLabel = QLabel(self.widget)
        self.MainLabel.setObjectName(u"MainLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainLabel.sizePolicy().hasHeightForWidth())
        self.MainLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.MainLabel.setFont(font)
        self.MainLabel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.MainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.MainVerticalLayout.addWidget(self.MainLabel)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Name_Label = QLabel(self.widget)
        self.Name_Label.setObjectName(u"Name_Label")

        self.verticalLayout_3.addWidget(self.Name_Label)

        self.Name_LineEdit = QLineEdit(self.widget)
        self.Name_LineEdit.setObjectName(u"Name_LineEdit")

        self.verticalLayout_3.addWidget(self.Name_LineEdit)


        self.MainVerticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Type_Label = QLabel(self.widget)
        self.Type_Label.setObjectName(u"Type_Label")

        self.verticalLayout_2.addWidget(self.Type_Label)

        self.Type_ComboBox = QComboBox(self.widget)
        self.Type_ComboBox.setObjectName(u"Type_ComboBox")
        sizePolicy1.setHeightForWidth(self.Type_ComboBox.sizePolicy().hasHeightForWidth())
        self.Type_ComboBox.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.Type_ComboBox)


        self.MainVerticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Recommendatio_Label = QLabel(self.widget)
        self.Recommendatio_Label.setObjectName(u"Recommendatio_Label")

        self.verticalLayout_4.addWidget(self.Recommendatio_Label)

        self.Recommendation_LineEdit = QLineEdit(self.widget)
        self.Recommendation_LineEdit.setObjectName(u"Recommendation_LineEdit")

        self.verticalLayout_4.addWidget(self.Recommendation_LineEdit)


        self.MainVerticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Tags_Label = QLabel(self.widget)
        self.Tags_Label.setObjectName(u"Tags_Label")

        self.verticalLayout_5.addWidget(self.Tags_Label)

        self.Tags_LineEdit = QLineEdit(self.widget)
        self.Tags_LineEdit.setObjectName(u"Tags_LineEdit")

        self.verticalLayout_5.addWidget(self.Tags_LineEdit)


        self.MainVerticalLayout.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.SubmitButton = QPushButton(self.widget)
        self.SubmitButton.setObjectName(u"SubmitButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SubmitButton.sizePolicy().hasHeightForWidth())
        self.SubmitButton.setSizePolicy(sizePolicy2)
        self.SubmitButton.setSizeIncrement(QSize(1, 0))
        self.SubmitButton.setBaseSize(QSize(2, 0))
        font1 = QFont()
        font1.setBold(True)
        self.SubmitButton.setFont(font1)

        self.horizontalLayout_5.addWidget(self.SubmitButton)

        self.CancelButton = QPushButton(self.widget)
        self.CancelButton.setObjectName(u"CancelButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy3)
        self.CancelButton.setSizeIncrement(QSize(0, 0))
        self.CancelButton.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setStrikeOut(False)
        self.CancelButton.setFont(font2)
        self.CancelButton.setAutoFillBackground(False)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.CancelButton.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.CancelButton)


        self.MainVerticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(VideoForm)

        QMetaObject.connectSlotsByName(VideoForm)
    # setupUi

    def retranslateUi(self, VideoForm):
        VideoForm.setWindowTitle(QCoreApplication.translate("VideoForm", u"Video entry form", None))
        self.MainLabel.setText(QCoreApplication.translate("VideoForm", u"Video entry form", None))
        self.Name_Label.setText(QCoreApplication.translate("VideoForm", u"Name:", None))
        self.Type_Label.setText(QCoreApplication.translate("VideoForm", u"Type:", None))
        self.Recommendatio_Label.setText(QCoreApplication.translate("VideoForm", u"Recommended by:", None))
        self.Tags_Label.setText(QCoreApplication.translate("VideoForm", u"Tags:", None))
        self.SubmitButton.setText(QCoreApplication.translate("VideoForm", u"Submit", None))
        self.CancelButton.setText(QCoreApplication.translate("VideoForm", u"Cancel", None))
    # retranslateUi

