import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QPushButton, QVBoxLayout


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.setGeometry(800, 250, 400, 400)

        # Устанавливаем иконку окна
        icon = QtGui.QIcon("logo1.png")  # Путь к вашей иконке
        self.setWindowIcon(icon)

        # Создание виджетов
        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # Лейбл "Введите логин и пароль"
        self.label = QtWidgets.QLabel("Введите логин и пароль", self.centralWidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 270, 140))
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # Поля ввода логина и пароля
        self.loginEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.loginEdit.setGeometry(QtCore.QRect(100, 150, 200, 30))

        self.passwordEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.passwordEdit.setGeometry(QtCore.QRect(100, 200, 200, 30))
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        # Кнопка входа
        self.loginButton = QtWidgets.QPushButton("Вход", self.centralWidget)
        self.loginButton.setGeometry(QtCore.QRect(130, 270, 140, 50))
        self.loginButton.clicked.connect(self.check_login)

        # Применение стилей к окну входа
        self.setStyleSheet("""
                    QMainWindow {
                        background-color: rgb(255, 228, 215);
                    }
                    QWidget {
                        font-family: Bryndan Write;
                        font-size: 15pt;
                    }
                """)

    def check_login(self):
        login = self.loginEdit.text()
        password = self.passwordEdit.text()

        # Пример проверки логина и пароля (должны быть заданы вручную)
        if login == "admin" and password == "1111":
            QtWidgets.QMessageBox.information(self, "Успешно", "Вход выполнен!")
            self.studentProfileWindow = StudentProfileWindow()
            self.studentProfileWindow.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль!")


class StudentProfileWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Личное дело студента")
        self.setGeometry(690, 250, 632, 518)

        # Устанавливаем иконку окна
        icon = QtGui.QIcon("logo1.png")  # Путь к вашей иконке
        self.setWindowIcon(icon)

        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # Шрифт для виджетов
        font = QtGui.QFont()
        font.setFamily("Bryndan Write")
        font.setPointSize(15)

        # Лейбл "Личное дело студента"
        self.label = QtWidgets.QLabel("Личное дело студента", self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 12, 335, 45))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(font)

        # Лейбл для отображения изображения
        self.imageLabel = QtWidgets.QLabel(self.centralWidget)
        self.imageLabel.setGeometry(QtCore.QRect(385, 50, 250, 200))
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Загрузка номера дела из файла
        self.counter = self.load_counter()

        self.counterLabel = QtWidgets.QLabel(f"Номер дела: {self.counter}", self.centralWidget)
        self.counterLabel.setGeometry(QtCore.QRect(300, 20, 200, 30))
        self.counterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.counterLabel.setFont(font)  # Устанавливаем шрифт для номера дела

        # Поля для заполнения
        self.fullnameLabel = QtWidgets.QLabel("ФИО:", self.centralWidget)
        self.fullnameLabel.setGeometry(QtCore.QRect(30, 70, 150, 30))
        self.fullnameLabel.setFont(font)

        self.fullnameEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.fullnameEdit.setGeometry(QtCore.QRect(100, 70, 300, 30))
        self.fullnameEdit.setFont(font)

        self.dateLabel = QtWidgets.QLabel("Дата рождения:", self.centralWidget)
        self.dateLabel.setGeometry(QtCore.QRect(30, 110, 180, 30))
        self.dateLabel.setFont(font)

        self.dateEdit = QtWidgets.QDateEdit(self.centralWidget)
        self.dateEdit.setGeometry(QtCore.QRect(220, 110, 180, 30))
        self.dateEdit.setFont(font)

        self.nationalityLabel = QtWidgets.QLabel("Гражданство:", self.centralWidget)
        self.nationalityLabel.setGeometry(QtCore.QRect(30, 150, 155, 30))
        self.nationalityLabel.setFont(font)

        self.nationalityEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.nationalityEdit.setGeometry(QtCore.QRect(220, 150, 180, 30))
        self.nationalityEdit.setFont(font)

        self.innLabel = QtWidgets.QLabel("ИНН:", self.centralWidget)
        self.innLabel.setGeometry(QtCore.QRect(30, 190, 150, 30))
        self.innLabel.setFont(font)

        self.innEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.innEdit.setGeometry(QtCore.QRect(90, 190, 150, 30))
        self.innEdit.setFont(font)

        self.snilsLabel = QtWidgets.QLabel("Снилс:", self.centralWidget)
        self.snilsLabel.setGeometry(QtCore.QRect(30, 230, 150, 30))
        self.snilsLabel.setFont(font)

        self.snilsEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.snilsEdit.setGeometry(QtCore.QRect(110, 230, 150, 30))
        self.snilsEdit.setFont(font)

        self.passportLabel = QtWidgets.QLabel("Данные паспорта:", self.centralWidget)
        self.passportLabel.setGeometry(QtCore.QRect(30, 270, 185, 30))
        self.passportLabel.setFont(font)

        self.passportSeriesLabel = QtWidgets.QLabel("Серия:", self.centralWidget)
        self.passportSeriesLabel.setGeometry(QtCore.QRect(230, 270, 150, 30))
        self.passportSeriesLabel.setFont(font)

        self.passportSeriesEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.passportSeriesEdit.setGeometry(QtCore.QRect(310, 270, 70, 30))
        self.passportSeriesEdit.setFont(font)

        self.passportNumberLabel = QtWidgets.QLabel("Номер:", self.centralWidget)
        self.passportNumberLabel.setGeometry(QtCore.QRect(390, 270, 150, 30))
        self.passportNumberLabel.setFont(font)

        self.passportNumberEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.passportNumberEdit.setGeometry(QtCore.QRect(470, 270, 100, 30))
        self.passportNumberEdit.setFont(font)

        self.genderLabel = QtWidgets.QLabel("Пол:", self.centralWidget)
        self.genderLabel.setGeometry(QtCore.QRect(30, 310, 150, 30))
        self.genderLabel.setFont(font)

        self.genderGroup = QtWidgets.QButtonGroup(self.centralWidget)

        self.maleRadioButton = QtWidgets.QRadioButton("Мужской", self.centralWidget)
        self.maleRadioButton.setGeometry(QtCore.QRect(120, 310, 130, 30))
        self.maleRadioButton.setFont(font)
        self.genderGroup.addButton(self.maleRadioButton)

        self.femaleRadioButton = QtWidgets.QRadioButton("Женский", self.centralWidget)
        self.femaleRadioButton.setGeometry(QtCore.QRect(300, 310, 130, 30))
        self.femaleRadioButton.setFont(font)
        self.genderGroup.addButton(self.femaleRadioButton)

        self.directionLabel = QtWidgets.QLabel("Направление:", self.centralWidget)
        self.directionLabel.setGeometry(QtCore.QRect(30, 350, 150, 30))
        self.directionLabel.setFont(font)

        self.directionEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.directionEdit.setGeometry(QtCore.QRect(180, 350, 300, 30))
        self.directionEdit.setFont(font)

        self.groupLabel = QtWidgets.QLabel("Группа:", self.centralWidget)
        self.groupLabel.setGeometry(QtCore.QRect(30, 390, 150, 30))
        self.groupLabel.setFont(font)

        self.groupEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.groupEdit.setGeometry(QtCore.QRect(130, 390, 300, 30))
        self.groupEdit.setFont(font)

        # Кнопка "Назад"
        self.backButton = QtWidgets.QPushButton("Выход", self.centralWidget)
        self.backButton.setGeometry(QtCore.QRect(30, 440, 150, 50))
        self.backButton.setFont(font)
        self.backButton.clicked.connect(self.check_back)

        # Кнопка "Сохранить"
        self.saveButton = QtWidgets.QPushButton("Сохранить", self.centralWidget)
        self.saveButton.setGeometry(QtCore.QRect(190, 440, 150, 50))
        self.saveButton.setFont(font)
        self.saveButton.clicked.connect(self.save_profile)

        # Кнопка "Выбрать изображение"
        self.photoButton = QPushButton("Выбрать изображение", self.centralWidget)
        self.photoButton.setGeometry(QtCore.QRect(350, 440, 260, 50))
        self.photoButton.setFont(font)
        self.photoButton.clicked.connect(self.open_image)

        # Применение стилей к окну профиля студента
        self.setStyleSheet("""
                    QMainWindow {
                        background-color: rgb(255, 228, 215);
                    }
                    QWidget {
                        font-family: Bryndan Write;
                        font-size: 15pt;
                    }
                """)

    def open_image(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Открыть изображение", "", "Изображения (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if filename:
            self.pixmap = QPixmap(filename)
            self.pixmap = self.pixmap.scaled(250, 200, Qt.KeepAspectRatio)  # Установка ширины 250 пикселей и высоты 200 пикселей
            self.imageLabel.setPixmap(self.pixmap)
            self.imagePath = filename  # Сохраняем путь к изображению

    def load_counter(self):
        try:
            with open("counter.txt", "r") as file:
                counter = int(file.read().strip())
        except FileNotFoundError:
            counter = 1  # Если файл не найден, начинаем с 1
        return counter

    def check_back(self):
        self.loginWindow = LoginWindow()
        self.loginWindow.show()
        self.close()

    def save_profile(self):
        try:
            # Проверяем, что все обязательные поля заполнены
            if not self.imagePath.strip():
                raise ValueError("Прикрепите фото!")
            if not self.fullnameEdit.text().strip():
                raise ValueError("Поле ФИО не заполнено")
            if not self.dateEdit.text().strip():
                raise ValueError("Поле Дата рождения не заполнено")
            if not self.nationalityEdit.text().strip():
                raise ValueError("Поле Гражданство не заполнено")
            if not self.passportSeriesEdit.text().strip() or not self.passportNumberEdit.text().strip():
                raise ValueError("Поля Серия или Номер паспорта не заполнены")
            if not self.innEdit.text().strip():
                raise ValueError("Поле ИНН не заполнено")
            if not self.snilsEdit.text().strip():
                raise ValueError("Поле СНИЛС не заполнено")
            if not self.directionEdit.text().strip():
                raise ValueError("Поле Направление не заполнено")
            if not self.groupEdit.text().strip():
                raise ValueError("Поле Группа не заполнено")

            # Сохраняем данные в TXT файл
            with open("student_profile_data.txt", "a", encoding="utf-8") as file:
                file.write(f"Номер дела: {self.counter}\n")
                file.write(f"Фото: {self.imagePath}\n")  # Сохраняем путь к изображению
                file.write(f"ФИО: {self.fullnameEdit.text()}\n")
                file.write(f"Дата рождения: {self.dateEdit.text()}\n")
                file.write(f"Гражданство: {self.nationalityEdit.text()}\n")
                file.write(
                    f"Данные паспорта: Серия - {self.passportSeriesEdit.text()}, Номер - {self.passportNumberEdit.text()}\n")
                file.write(f"ИНН: {self.innEdit.text()}\n")
                file.write(f"СНИЛС: {self.snilsEdit.text()}\n")
                file.write(f"Пол: {'Мужской' if self.maleRadioButton.isChecked() else 'Женский'}\n")
                file.write(f"Направление: {self.directionEdit.text()}\n")
                file.write(f"Группа: {self.groupEdit.text()}\n\n")

            QtWidgets.QMessageBox.information(self, "Успех", "Данные сохранены в файл student_profile_data.txt")

            # Увеличиваем номер дела на 1 для следующего профиля
            self.counter += 1
            self.counterLabel.setText(f"Номер дела: {self.counter}")

            # Сохраняем новый номер дела в файл
            self.save_counter()

            # Очищаем поля ввода для следующего профиля
            self.fullnameEdit.clear()
            self.dateEdit.clear()
            self.nationalityEdit.clear()
            self.passportSeriesEdit.clear()
            self.passportNumberEdit.clear()
            self.innEdit.clear()
            self.snilsEdit.clear()
            self.directionEdit.clear()
            self.groupEdit.clear()
            self.imageLabel.clear()  # Очищаем отображение QLabel (не изображение!)
            self.imageLabel.setPixmap(QtGui.QPixmap())  # Устанавливаем пустое изображение
            self.maleRadioButton.setChecked(True)  # По умолчанию выбран мужской пол

        except ValueError as ve:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка сохранения данных: {str(ve)}")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка сохранения данных: {str(e)}")

    def save_counter(self):
        try:
            with open("counter.txt", "w") as file:
                file.write(str(self.counter))
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка сохранения номера дела: {str(e)}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec_())
