# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main1020JJUhKP.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(539, 674)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop:0 rgb(81, 43, 152), stop:1 rgb(219, 21, 189));\n"
"border-radius:20px ")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 36)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(381, 481))
        self.frame_4.setMaximumSize(QSize(381, 481))
        self.frame_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 381, 481))
        self.frame_2.setMinimumSize(QSize(381, 481))
        self.frame_2.setMaximumSize(QSize(381, 481))
        self.frame_2.setStyleSheet(u"QFrame{image: url(:/svg/\u672a\u6807\u9898-1.png);\n"
"\n"
"background-color: rgba(255, 255, 255, 0);}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 20, 341, 441))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	image: none;\n"
"background-color: rgba(255, 255, 255, 20%);\n"
"border-radius:6px \n"
"}\n"
"QLabel{\n"
"\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(24, 24, 24, 8)
        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 64))
        self.widget.setStyleSheet(u"image: url(:/svg/img/svg/\u5973\u5b691.png);")
        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(120, 10, 48, 48))
        self.pushButton_9.setMinimumSize(QSize(48, 48))
        self.pushButton_9.setMaximumSize(QSize(48, 48))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	border-radius:24px ;\n"
"	background-color: rgba(251, 252, 255, 0);\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/logossw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QSize(48, 48))

        self.verticalLayout_3.addWidget(self.widget)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 24)
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 26777))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.label_2 = QLabel(self.frame_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 42))
        self.frame_7.setStyleSheet(u"border-radius:16px ;\n"
"background-color: rgba(255, 255, 255, 51);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.widget_2 = QWidget(self.frame_7)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(18, 18))
        self.widget_2.setStyleSheet(u"image: url(:/images/img/buttom_white/\u95ad\ue1bb\u6b22\u9359\u6226\u20ac\u4f79\u579a\u9354\u7108email-successfully.svg);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_6.addWidget(self.widget_2)

        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	selection-color: rgb(34, 34, 34);\n"
"}")

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 9)

        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 42))
        self.frame_8.setStyleSheet(u"border-radius:16px ;\n"
"background-color: rgba(255, 255, 255, 51);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.widget_3 = QWidget(self.frame_8)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(18, 18))
        self.widget_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/images/img/buttom_white/\u9422\u975b\u74d9\u95bf\u4f78\u7d11_electronic-locks-open.svg);")

        self.horizontalLayout_7.addWidget(self.widget_3)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	selection-color: rgb(34, 34, 34);\n"
"}")

        self.horizontalLayout_7.addWidget(self.lineEdit_2)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 9)

        self.verticalLayout_4.addWidget(self.frame_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox = QCheckBox(self.frame_9)
        self.checkBox.setObjectName(u"checkBox")
        font2 = QFont()
        font2.setPointSize(10)
        self.checkBox.setFont(font2)

        self.horizontalLayout_4.addWidget(self.checkBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.pushButton = QPushButton(self.frame_9)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"color: rgb(84, 42, 155);")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 48))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(11, 11, 11);\n"
"	border-radius:20px ;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"color: rgb(84, 42, 155);")

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 2)
        self.horizontalLayout_5.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(340, 20, 20, 20))
        self.pushButton_10.setMinimumSize(QSize(20, 20))
        self.pushButton_10.setMaximumSize(QSize(48, 48))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	border-radius:24px ;\n"
"	background-color: rgba(251, 252, 255, 51);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/img/buttom_white/\u934f\u62bd\u68f4_close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QSize(20, 20))
        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(320, 20, 20, 20))
        self.pushButton_11.setMinimumSize(QSize(20, 20))
        self.pushButton_11.setMaximumSize(QSize(48, 48))
        font4 = QFont()
        font4.setPointSize(5)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        self.pushButton_11.setFont(font4)
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	border-radius:24px ;\n"
"	background-color: rgba(251, 252, 255, 51);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_11.setText(u"\u2014\u2014")
        self.pushButton_11.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.horizontalSpacer_2 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(24)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(24)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(48, 48))
        self.pushButton_4.setMaximumSize(QSize(48, 48))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border-radius:24px ;\n"
"	background-color: rgba(251, 252, 255, 51);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/images/img/buttom_white/github _github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(48, 48))
        self.pushButton_6.setMaximumSize(QSize(48, 48))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	border-radius:24px ;\n"
"	background-color: rgba(251, 252, 255, 51);\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/img/buttom_white/\u9474\u9550\u529f_facebook.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(48, 48))
        self.pushButton_7.setMaximumSize(QSize(48, 48))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	border-radius:24px ;\n"
"	background-color: rgba(251, 252, 255, 51);\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/images/img/buttom_white/\u748b\u950b\u74d5_google.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(48, 48))
        self.pushButton_5.setMaximumSize(QSize(48, 48))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	border-radius:24px ;\n"
"	background-color: rgba(251, 252, 255, 51);\n"
"\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/img/buttom_white/\u947b\u89c4\u7049_apple.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(48, 48))
        self.pushButton_8.setMaximumSize(QSize(48, 48))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	border-radius:24px ;\n"
"	background-color: rgba(251, 252, 255, 51);\n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/images/img/buttom_white/\u5bf0\ue1bb\u4fca_wechat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.pushButton_8)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.frame_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.frame_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_9.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TechXpose", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u767b\u5f55\u8d26\u6237\u4ee5\u4f7f\u7528TechXpose", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1\uff1a", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5fd8\u8bb0\u5bc6\u7801", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"SIGN  IN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6ca1\u6709\u8d26\u6237\uff1f", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c\u8d26\u6237", None))
        self.pushButton_10.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5176\u5b83\u65b9\u5f0f\u767b\u5f55", None))
        self.pushButton_4.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_5.setText("")
        self.pushButton_8.setText("")
    # retranslateUi

