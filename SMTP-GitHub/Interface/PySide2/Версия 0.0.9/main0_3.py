import sys,os,requests
from PySide2.QtCore import QFileInfo
from PySide2 import QtWidgets,QtCore
from PySide2.QtLocation import QPlaceIcon
from PySide2.QtWidgets import (
    QFileDialog
)
from PySide2.QtGui import QIcon, QPixmap

import rass
from ui_main import Ui_MainWindow
from ui_second_main import Ui_Form




class SendingThread(QtCore.QThread):
    sending_progressBar_update_signal = QtCore.Signal(int)
    update_label_signal = QtCore.Signal(str)
    reset_progressBar_signal = QtCore.Signal(int)
    def __init__(self, progressBar, filename_t,sending_confirm, parent = None):
        super(SendingThread,self).__init__(parent)
        self.progressBar = progressBar
        self.sending_confirm = sending_confirm
        self.filename_t = filename_t
        self.is_running = True
    def run(self):
        self.reset_progressBar_signal.emit(0)
        rass.read_value_from_txt("config.txt")
        self.update_label_signal.emit("Отправка начата")
        rass.sendd(self.update_progress, self.filename_t, self)
        if not self.is_running:
            self.update_label_signal.emit("Отправка прервана")
        else:
            self.update_label_signal.emit("Отправка завершена")


    def update_progress(self, value, maximum):
        self.progressBar.setMaximum(maximum)
        self.sending_progressBar_update_signal.emit(value)

    def stop(self):
        self.is_running = False

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)
        self.thread = None

        try:
            self.ui.DB_button.clicked.connect(self.select_db_file)
            self.ui.File_button.clicked.connect(self.select_attach_file)
            self.ui.email_button.clicked.connect(self.sending_email)
            self.ui.email_button_stop.clicked.connect(self.stop_sending)
            self.ui.settings_button.clicked.connect(self.open_settings_window)


        except AttributeError as e:
            print(f"Ошибка: {e}")
            sys.exit(-1)
        ##################### Иконки

        password_show = 'https://s.iimg.su/s/27/1n8duDoa9g59i49N0Xi1fCnSbFzeNodD8G80jQS3.png'
        self.show_icon = QPixmap()
        self.show_icon.loadFromData(requests.get(password_show).content)

        password_hide = 'https://s.iimg.su/s/27/UZLB1pKbwdWf4PYgBNUJSGVaQy5gJzZ7ePEJu2ts.png'
        self.hide_icon = QPixmap()
        self.hide_icon.loadFromData(requests.get(password_hide).content)

        ##################### Иконки

    def select_db_file(self):  # Получение названия файла и его вывод в label
        dialog = QFileDialog()
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Файлы таблиц (*.xls *.xlsx)")
        dialog.setViewMode(QFileDialog.ViewMode.List)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                rass.read_value_from_txt("config.txt")
                db_file_names = [QFileInfo(filename).fileName() for filename in filenames]
                db_filenames = filenames[0]
                print(db_filenames)
                success = rass.excel_format(db_file_names, db_filenames)

                if success:
                    self.ui.DB_name.setText("Выбранный файл:\n" + "\n".join(db_file_names))
                else:
                    self.ui.DB_name.setText("Выберите 1 файл")

    def select_attach_file(self):  # Получение названия файла и его вывод в label
        dialog = QFileDialog()
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Все файлы (*)")
        dialog.setViewMode(QFileDialog.ViewMode.List)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                rass.read_value_from_txt("config.txt")
                file_names = [QFileInfo(filename).fileName() for filename in filenames]
                self.ui.File_name.setText("Выбранные файлы:\n" + "\n".join(file_names))
                self.filename_t = rass.attach_file_save(filenames)

    def sending_email(self):
        if self.thread is None or not self.thread.isRunning():
            self.thread = SendingThread(self.ui.progressBar, self.filename_t, self.ui.sending_confirm)
            self.thread.reset_progressBar_signal.connect(self.reset_progressBar)
            self.thread.update_label_signal.connect(self.update_label_text)
            self.thread.sending_progressBar_update_signal.connect(self.update_progress_bar)
            self.thread.start()
        else:
            self.ui.sending_confirm.setText("Отправка уже идет")

    def stop_sending(self):
        if self.thread is not None:
            self.thread.stop()

    def reset_progressBar(self,value):
        self.ui.progressBar.setValue(value)

    def update_label_text(self, text):
        self.ui.sending_confirm.setText(text)

    def update_progress_bar(self, value):
        self.ui.progressBar.setValue(value)

    def open_settings_window(self):
        self.second_window = SettingsWidget()
        self.second_window.show()

    def run(self):
        self.show()
        sys.exit(app.exec_())


class SettingsWidget(QtWidgets.QWidget):

    def __init__(self):
        super(SettingsWidget, self).__init__()
        self.main_window = MainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.ui.mail_body_edit.textChanged.connect(self.body_text_changed)
        # self.ui.mail_signature_edit.textChanged.connect(self.signature_text_changed)
        self.ui.mail_password_visible.setIcon(QIcon(self.main_window.show_icon))
        self.ui.mail_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        try:
            self.ui.open_config_button.clicked.connect(self.open_config_file)
            self.ui.save_config_button.clicked.connect(self.save_config_file)
            self.ui.add_name_button.clicked.connect(self.add_name_func)
            self.ui.mail_password_visible.clicked.connect(self.password_visible)
        except AttributeError as e:
            print(f"Ошибка: {e}")
            sys.exit(-1)

    # def body_text_changed(self):
    #     text_input = self.ui.mail_body_edit.toPlainText()
    #     html_text = "<p>" + "<br>\n".join(line.strip() for line in text_input.splitlines() if line.strip()) + "</p>"
    #     print(html_text)
    #
    # def signature_text_changed(self):
    #     text_input = self.ui.mail_signature_edit.toPlainText()
    #     html_text = "<p>" + "<br>\n".join(line.strip() for line in text_input.splitlines() if line.strip()) + "</p>"
    #     print(html_text)


    def open_config_file(self):
        dialog = QFileDialog()
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("TXT (*.txt)")
        dialog.setViewMode(QFileDialog.ViewMode.List)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                config_filename = filenames[0]
                config = rass.read_value_from_txt(config_filename)
                print(config)
                self.ui.mail_adress_edit.setText(config['user'])
                self.ui.mail_password_edit.setText(config['app_password'])
                self.ui.mail_topic_edit.setText(config['topic'])
                self.ui.mail_body_edit.setText(config['body'])
                self.ui.mail_signature_edit.setText(config['signature'])

    def save_config_file(self):
        body_text = self.ui.mail_body_edit.toPlainText()
        signature_text = self.ui.mail_signature_edit.toPlainText()
        html_body = "<p>" + "<br>\n".join(line.strip() for line in body_text.splitlines() if line.strip()) + "</p>"
        html_signature = "<p>" + "<br>\n".join(line.strip() for line in signature_text.splitlines() if line.strip()) + "</p>"
        output = f"""
        user:'{self.ui.mail_adress_edit.text()}'
        app_password:'{self.ui.mail_password_edit.text()}'
        topic:'{self.ui.mail_topic_edit.text()}'
        body:'{html_body}'
        signature:'{html_signature}' 
        pixel:'https://mc.yandex.ru/pixel/6987978285606056592?rnd=%aw_random%'
        """
        with open('config.txt', 'w', encoding='utf-8') as file:
            file.write(output)

    def add_name_func(self):
        self.ui.mail_body_edit.insertPlainText('{name_list}')

    def password_visible(self):
        mode = self.ui.mail_password_edit.echoMode()
        if mode == QtWidgets.QLineEdit.Normal:
            self.ui.mail_password_visible.setIcon(QIcon(self.main_window.show_icon))
            self.ui.mail_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        if mode == QtWidgets.QLineEdit.Password:
            self.ui.mail_password_visible.setIcon(QIcon(self.main_window.hide_icon))
            self.ui.mail_password_edit.setEchoMode(QtWidgets.QLineEdit.Normal)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.run()

