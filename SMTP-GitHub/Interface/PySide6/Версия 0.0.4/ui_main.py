# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(442, 412)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 200, 351, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.DB_button = QPushButton(self.horizontalLayoutWidget)
        self.DB_button.setObjectName(u"DB_button")
        self.DB_button.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.DB_button)

        self.File_button = QPushButton(self.horizontalLayoutWidget)
        self.File_button.setObjectName(u"File_button")
        self.File_button.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.File_button)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(70, 150, 321, 21))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSpacing(100)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.DB_file = QLabel(self.horizontalLayoutWidget_3)
        self.DB_file.setObjectName(u"DB_file")

        self.horizontalLayout_3.addWidget(self.DB_file)

        self.File_file = QLabel(self.horizontalLayoutWidget_3)
        self.File_file.setObjectName(u"File_file")

        self.horizontalLayout_3.addWidget(self.File_file)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(60, 170, 351, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.DB_name = QLabel(self.horizontalLayoutWidget_4)
        self.DB_name.setObjectName(u"DB_name")

        self.horizontalLayout_4.addWidget(self.DB_name)

        self.File_name = QLabel(self.horizontalLayoutWidget_4)
        self.File_name.setObjectName(u"File_name")

        self.horizontalLayout_4.addWidget(self.File_name)

        self.email_button = QPushButton(self.centralwidget)
        self.email_button.setObjectName(u"email_button")
        self.email_button.setGeometry(QRect(160, 310, 111, 24))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(160, 80, 118, 23))
        self.progressBar.setValue(24)
        self.DB_file_2 = QLabel(self.centralwidget)
        self.DB_file_2.setObjectName(u"DB_file_2")
        self.DB_file_2.setGeometry(QRect(150, 50, 110, 19))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 442, 22))
        self.menu_fds = QMenu(self.menubar)
        self.menu_fds.setObjectName(u"menu_fds")
        self.menuE_mail_nikolay_krutykh_yandex_ru = QMenu(self.menubar)
        self.menuE_mail_nikolay_krutykh_yandex_ru.setObjectName(u"menuE_mail_nikolay_krutykh_yandex_ru")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_fds.menuAction())
        self.menubar.addAction(self.menuE_mail_nikolay_krutykh_yandex_ru.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.DB_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u044c", None))
        self.File_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u044c", None))
        self.DB_file.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u0411\u0414", None))
        self.File_file.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b Attach", None))
        self.DB_name.setText("")
        self.File_name.setText("")
        self.email_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0443", None))
        self.DB_file_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438", None))
        self.menu_fds.setTitle(QCoreApplication.translate("MainWindow", u"TG: @Tachg", None))
        self.menuE_mail_nikolay_krutykh_yandex_ru.setTitle(QCoreApplication.translate("MainWindow", u"E-mail: nikolay.krutykh@yandex.ru", None))
    # retranslateUi

