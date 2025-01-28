import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

class SecondWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.loader = QUiLoader()
        self.window = self.loader.load("main_1.ui", None)

        # Установка layout для второго окна
        layout = QtWidgets.QVBoxLayout(self)  # Устанавливаем layout для текущего виджета
        layout.addWidget(self.window)

        self.resize(400, 300)

class MyApp:
    def __init__(self):
        # Инициализация загрузчика и приложения
        self.loader = QUiLoader()
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = self.loader.load("main.ui", None)

        # Проверка на успешную загрузку основного окна
        if not self.window:
            print("Не удалось загрузить интерфейс основного окна.")
            sys.exit(-1)

        # Подключение сигнала кнопки к методу
        try:
            self.window.pushButton.clicked.connect(self.open_second_window)
        except AttributeError:
            print("Ошибка: элемент 'pushButton' не найден в загруженном интерфейсе.")
            sys.exit(-1)

    def open_second_window(self):
        # Создаем и показываем второе окно
        self.second_window = SecondWindow()
        self.second_window.show()  # Показываем второе окно

    def run(self):
        # Показываем основное окно и запускаем приложение
        self.window.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    app = MyApp()  # Создаем экземпляр приложения
    app.run()      # Запускаем приложение
