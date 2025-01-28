import sys
from symbol import import_from

from PySide6.QtCore import QFileInfo
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QListWidget
)

from rass import *

class MainWindow:

    def __init__(self):
        self.loader = QUiLoader()
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = self.loader.load("main.ui", None)

        try:
            self.window.DB_button.clicked.connect(self.select_db_file)
            self.window.File_button.clicked.connect(self.select_attach_file)

        except AttributeError as e:
            print(f"Ошибка: {e}")
            sys.exit(-1)

    def select_db_file(self):   #Получение названия файла и его вывод в label
        dialog = QFileDialog()
        dialog.setDirectory(r'C:\images')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Images (*.xls *.xlsx )")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                db_file_names = [QFileInfo(filename).fileName() for filename in filenames]
                success = excel_format(db_file_names)
                if success:
                    self.window.DB_name.setText("\n".join(db_file_names)) #     file_names выходит списком с названием файла и его расширением
                else:
                    self.window.DB_name.setText("Выберите 1 файл")




    def select_attach_file(self):   #Получение названия файла и его вывод в label
        dialog = QFileDialog()
        dialog.setDirectory(r'C:\images')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Images (*.pdf )")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                file_names = [QFileInfo(filename).fileName() for filename in filenames]
                self.window.File_name.setText("\n".join(file_names)) #  file_names выходит списком с названием файла и его расширением


    def run(self):
        self.window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = MainWindow()
    app.run()
