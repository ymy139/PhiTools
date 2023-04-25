# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(620, 320)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 350, 60))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 320, 30))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QRect(0, 305, 200, 15))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(8)
        self.label_3.setFont(font2)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(464, 244, 131, 51))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei';\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 270, 100, 20))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI Light"])
        font3.setPointSize(11)
        self.label_4.setFont(font3)
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 271, 127, 22))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid rgb(238, 239, 238);\n"
"    border-radius: 5px;\n"
"    border-bottom: 1px solid rgb(212, 213, 212);\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei';\n"
"	padding: 0px 0px 1px 0px;\n"
"    color: black;\n"
"    background-color: rgb(254, 254, 254);\n"
"    text-align: left;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: green;\n"
"}\n"
"\n"
"QComboBox:!editable,QComboBox::drop-down:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"/* \u5f53\u4e0b\u62c9\u6846\u6253\u5f00\u65f6,\u80cc\u666f\u989c\u8272\u6e10\u53d8 */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: white;\n"
"}\n"
"\n"
"/* \u5f53\u4e0b\u62c9\u6846\u6253\u5f00\u65f6, \u79fb\u52a8\u663e\u793a\u6846\u6587\u672c\u4f4d\u7f6e*/\n"
"QComboBox:on {\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u6309\u94ae\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"\n"
"    subcontrol-position: top right;\n"
"\n"
"    width: 2"
                        "5px;\n"
"\n"
"    border-left-width: 3px;\n"
"    border-left-color: red;\n"
"    border-left-style: solid;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"} */\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid rgb(238, 239, 238);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(254, 254, 254);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border-image-source: url(kMoT0EcmVt.jpg);\n"
"    border-image-repeat: rounded;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u6309\u94ae\u4f4d\u79fb */\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u5217\u8868\u91cc\u7684\u989c\u8272 */\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: green;\n"
"}")
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(120, 160, 69, 22))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6b22\u8fce\u4f7f\u7528REPGTools\uff01", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u60a8\u8981\u4f7f\u7528\u7684\u529f\u80fd\uff0c\u7136\u540e\u70b9\u51fb\u4e0b\u4e00\u6b65", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"REPGTools v0.1.0  Code by\uff1aymy139", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u6b65", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8981\u4f7f\u7528\u7684\u529f\u80fd\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u65b0\u5efa\u9879\u76ee", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u65b0\u5efa\u9879\u76ee", None))

    # retranslateUi

