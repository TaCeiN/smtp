# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(489, 413)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 10, 412, 352))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(25)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.mail_password = QLabel(self.gridLayoutWidget)
        self.mail_password.setObjectName(u"mail_password")

        self.gridLayout.addWidget(self.mail_password, 1, 0, 1, 1)

        self.mail_adress_edit = QLineEdit(self.gridLayoutWidget)
        self.mail_adress_edit.setObjectName(u"mail_adress_edit")

        self.gridLayout.addWidget(self.mail_adress_edit, 0, 1, 1, 1)

        self.mail_topic = QLabel(self.gridLayoutWidget)
        self.mail_topic.setObjectName(u"mail_topic")

        self.gridLayout.addWidget(self.mail_topic, 2, 0, 1, 1)

        self.add_name_button = QPushButton(self.gridLayoutWidget)
        self.add_name_button.setObjectName(u"add_name_button")

        self.gridLayout.addWidget(self.add_name_button, 3, 2, 1, 1)

        self.mail_adress = QLabel(self.gridLayoutWidget)
        self.mail_adress.setObjectName(u"mail_adress")

        self.gridLayout.addWidget(self.mail_adress, 0, 0, 1, 1)

        self.mail_body = QLabel(self.gridLayoutWidget)
        self.mail_body.setObjectName(u"mail_body")

        self.gridLayout.addWidget(self.mail_body, 3, 0, 1, 1)

        self.mail_body_edit = QTextEdit(self.gridLayoutWidget)
        self.mail_body_edit.setObjectName(u"mail_body_edit")

        self.gridLayout.addWidget(self.mail_body_edit, 3, 1, 1, 1)

        self.mail_signature = QLabel(self.gridLayoutWidget)
        self.mail_signature.setObjectName(u"mail_signature")

        self.gridLayout.addWidget(self.mail_signature, 5, 0, 1, 1)

        self.mail_password_edit = QLineEdit(self.gridLayoutWidget)
        self.mail_password_edit.setObjectName(u"mail_password_edit")

        self.gridLayout.addWidget(self.mail_password_edit, 1, 1, 1, 1)

        self.mail_topic_edit = QLineEdit(self.gridLayoutWidget)
        self.mail_topic_edit.setObjectName(u"mail_topic_edit")

        self.gridLayout.addWidget(self.mail_topic_edit, 2, 1, 1, 1)

        self.mail_signature_edit = QTextEdit(self.gridLayoutWidget)
        self.mail_signature_edit.setObjectName(u"mail_signature_edit")

        self.gridLayout.addWidget(self.mail_signature_edit, 5, 1, 1, 2)

        self.open_config_button = QPushButton(Form)
        self.open_config_button.setObjectName(u"open_config_button")
        self.open_config_button.setGeometry(QRect(30, 370, 191, 23))
        self.save_config_button = QPushButton(Form)
        self.save_config_button.setObjectName(u"save_config_button")
        self.save_config_button.setGeometry(QRect(230, 370, 191, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mail_password.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c \u043f\u043e\u0447\u0442\u044b", None))
        self.mail_topic.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043c\u0430 \u043f\u0438\u0441\u044c\u043c\u0430:", None))
        self.add_name_button.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0435", None))
        self.mail_adress.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u043e\u0447\u0442\u044b", None))
        self.mail_body.setText(QCoreApplication.translate("Form", u"\u041f\u0438\u0441\u044c\u043c\u043e", None))
        self.mail_signature.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0434\u043f\u0438\u0441\u044c", None))
        self.open_config_button.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u0438", None))
        self.save_config_button.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u0438", None))
    # retranslateUi

