import sys
from PySide2.QtCore import QFileInfo
from PySide2 import QtWidgets,QtCore
from PySide2.QtWidgets import (
    QFileDialog
)

import rass
from ui_main import Ui_MainWindow
from ui_second_main import Ui_Form
from multiprocessing import freeze_support




class Task(QtCore.QRunnable):
    def __init__(self, progressBar, filename_t, sending_confirm):
        super().__init__()
        self.progressBar = progressBar
        self.sending_confirm = sending_confirm
        self.filename_t = filename_t

    def run(self):
        self.progressBar.setValue(0)
        rass.sendd(self.update_progress, self.filename_t)
        self.sending_confirm.setText("")

    def update_progress(self, value, maximum):
        self.progressBar.setMaximum(maximum)
        self.progressBar.setValue(value)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)

        try:
            self.ui.DB_button.clicked.connect(self.select_db_file)
            self.ui.File_button.clicked.connect(self.select_attach_file)
            self.ui.email_button.clicked.connect(self.sending_email)
            self.ui.settings_button.clicked.connect(self.open_settings_window)

        except AttributeError as e:
            print(f"Ошибка: {e}")
            sys.exit(-1)

    def select_db_file(self):  # Получение названия файла и его вывод в label
        dialog = QFileDialog()
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Файлы таблиц (*.xls *.xlsx)")
        dialog.setViewMode(QFileDialog.ViewMode.List)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
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
                file_names = [QFileInfo(filename).fileName() for filename in filenames]
                self.ui.File_name.setText("Выбранные файлы:\n" + "\n".join(file_names))
                self.filename_t = rass.attach_file_save(filenames)

    def sending_email(self):
            task = Task(self.ui.progressBar, self.filename_t, self.ui.sending_confirm)  # Передаем ссылку на progressBar и filename_t
            QtCore.QThreadPool.globalInstance().start(task)
            self.ui.sending_confirm.setText("Отправка в процессе")

    def open_settings_window(self):
        self.second_window = SettingsWidget()
        self.second_window.show()

    def run(self):
        self.show()
        sys.exit(app.exec_())

class SettingsWidget(QtWidgets.QWidget):
    def __init__(self):
        super(SettingsWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.textEdit.textChanged.connect(self.text_changed)

        try:
            self.ui.pushButton.clicked.connect(self.text_changed)

        except AttributeError as e:
            print(f"Ошибка: {e}")
            sys.exit(-1)

    def text_changed(self):
        text_input = self.ui.textEdit.toPlainText()
        print(text_input)


if __name__ == "__main__":
    freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.run()

