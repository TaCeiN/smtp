import sys
from PySide2.QtCore import QFileInfo
from PySide2 import QtWidgets,QtCore
from PySide2.QtWidgets import (
    QFileDialog
)
import rass
from ui_main import Ui_MainWindow

class Task(QtCore.QRunnable):
    def __init__(self, progressBar, filename_t):
        super().__init__()
        self.progressBar = progressBar
        self.filename_t = filename_t

    def run(self):
        self.progressBar.setValue(0)
        rass.sendd(self.update_progress,self.filename_t)

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

        except AttributeError as e:
            print(f"Ошибка: {e}")
            sys.exit(-1)

    def select_db_file(self):  # Получение названия файла и его вывод в label
        dialog = QFileDialog()
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Excel files (*.xls *.xlsx *.csv)")
        dialog.setViewMode(QFileDialog.ViewMode.List)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                db_file_names = [QFileInfo(filename).fileName() for filename in filenames]
                db_filenames = filenames[0]
                print(db_filenames)
                success = rass.excel_format(db_file_names, db_filenames)

                if success:
                    self.ui.DB_name.setText(f"Выбранный файл: {db_file_names[0]}")
                else:
                    self.ui.DB_name.setText("Выберите 1 файл")

    def select_attach_file(self):  # Получение названия файла и его вывод в label
        dialog = QFileDialog()
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("PDF (*.pdf )")
        dialog.setViewMode(QFileDialog.ViewMode.List)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                file_names = [QFileInfo(filename).fileName() for filename in filenames]
                attach_filenames = filenames[0]
                self.ui.File_name.setText(f"Выбранный файл: {file_names[0]}")
                self.filename_t = rass.attach_file_save(attach_filenames, filenames)

    def sending_email(self):
            task = Task(self.ui.progressBar, self.filename_t)  # Передаем ссылку на progressBar и filename_t
            QtCore.QThreadPool.globalInstance().start(task)
            self.ui.sending_confirm.setText("Отправка начата")

    def run(self):
        self.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.run()

