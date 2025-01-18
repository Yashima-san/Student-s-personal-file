import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import json


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.setGeometry(800, 250, 400, 400)

        # Устанавливаем иконку окна
        icon = QtGui.QIcon("logo.png")
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

    def check_login(self):
        login = self.loginEdit.text()
        password = self.passwordEdit.text()

        # Пример проверки логина и пароля (должны быть заданы вручную)
        if login == "admin" and password == "000":
            QtWidgets.QMessageBox.information(self, "Успешно", "Вход выполнен!")
            self.studentProfileWindow = StudentProfileWindow()
            self.studentProfileWindow.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль!")

    # def check_login(self):
    #     login = self.loginEdit.text()
    #     password = self.passwordEdit.text()
    #
    #     with open("student_profile_data.json", "r", encoding="utf-8") as file:
    #         credentials = json.load(file)
    #         correct_login = credentials.get("login")
    #         correct_password = credentials.get("password")
    #
    #     if login == correct_login and password == correct_password:
    #         QtWidgets.QMessageBox.information(self, "Успешно", "Вход выполнен!")
    #         self.studentProfileWindow = StudentProfileWindow()
    #         self.studentProfileWindow.show()
    #         self.close()
    #     else:
    #         QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль!")


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
        font.setFamily("Arial")
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
        self.passportLabel.setGeometry(QtCore.QRect(30, 270, 220, 30))
        self.passportLabel.setFont(font)

        self.passportSeriesLabel = QtWidgets.QLabel("Серия:", self.centralWidget)
        self.passportSeriesLabel.setGeometry(QtCore.QRect(250, 270, 150, 30))
        self.passportSeriesLabel.setFont(font)

        self.passportSeriesEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.passportSeriesEdit.setGeometry(QtCore.QRect(330, 270, 70, 30))
        self.passportSeriesEdit.setFont(font)

        self.passportNumberLabel = QtWidgets.QLabel("Номер:", self.centralWidget)
        self.passportNumberLabel.setGeometry(QtCore.QRect(410, 270, 150, 30))
        self.passportNumberLabel.setFont(font)

        self.passportNumberEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.passportNumberEdit.setGeometry(QtCore.QRect(500, 270, 100, 30))
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
        self.directionLabel.setGeometry(QtCore.QRect(30, 350, 180, 30))
        self.directionLabel.setFont(font)

        self.directionEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.directionEdit.setGeometry(QtCore.QRect(200, 350, 300, 30))
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

    def load_counter(self):
        try:
            with open("student_profile_data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = data.get("Номер дела", 1)  # Получаем значение ключа "Номер дела", если его нет, возвращаем 1
        except FileNotFoundError:
            counter = 1  # Если файл не найден, начинаем с 1
        except json.JSONDecodeError:
            counter = 1  # Если файл не удалось декодировать как JSON, начинаем с 1
        return counter

    def check_back(self):
        self.loginWindow = LoginWindow()
        self.loginWindow.show()
        self.close()

    def save_profile(self):
        try:
            # Проверяем, что все обязательные поля заполнены
            if not self.fullnameEdit.text().strip():
                raise ValueError("Поле ФИО не заполнено")
            elif not self.dateEdit.text().strip():
                raise ValueError("Поле Дата рождения не заполнено")
            elif not self.nationalityEdit.text().strip():
                raise ValueError("Поле Гражданство не заполнено")
            elif not self.passportSeriesEdit.text().strip() or not self.passportNumberEdit.text().strip():
                raise ValueError("Поля Серия или Номер паспорта не заполнены")
            elif not self.innEdit.text().strip():
                raise ValueError("Поле ИНН не заполнено")
            elif not self.snilsEdit.text().strip():
                raise ValueError("Поле СНИЛС не заполнено")
            elif not self.directionEdit.text().strip():
                raise ValueError("Поле Направление не заполнено")
            elif not self.groupEdit.text().strip():
                raise ValueError("Поле Группа не заполнено")

            # Сохраняем данные в json файл
            data = {
                "Номер дела": self.counter,
                "Фото": self.imagePath,
                "ФИО": self.fullnameEdit.text(),
                "Дата рождения": self.dateEdit.text(),
                "Гражданство": self.nationalityEdit.text(),
                "Данные паспорта": {
                    "Серия": self.passportSeriesEdit.text(),
                    "Номер": self.passportNumberEdit.text()
                },
                "ИНН": self.innEdit.text(),
                "СНИЛС": self.snilsEdit.text(),
                "Пол": "Мужской" if self.maleRadioButton.isChecked() else "Женский",
                "Направление": self.directionEdit.text(),
                "Группа": self.groupEdit.text()
            }

            # Открываем файл на запись в формате JSON
            with open("student_profile_data.json", "a", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False)
                file.write("\n")

            QtWidgets.QMessageBox.information(self, "Успех", "Данные сохранены в файл student_profile_data.json")

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
            self.maleRadioButton.setChecked(True)  # По умолчанию выбран мужской пол

        except ValueError as ve:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка сохранения данных: {str(ve)}")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка сохранения данных: {str(e)}")

    def save_counter(self):
        try:
            data = {"counter": self.counter}

            with open("student_profile_data.json", "w") as file:
                json.dump(data, file)

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка сохранения номера дела: {str(e)}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec_())
