using System;
using System.IO;
using System.Windows.Forms;

namespace StudentProfileApp
{
    // Главное окно входа
    public partial class LoginWindow : Form
    {
        public LoginWindow()
        {
            InitializeComponent();
        }

        private void InitializeComponent()
        {
            this.Text = "Вход";
            this.ClientSize = new System.Drawing.Size(400, 400);
            this.StartPosition = FormStartPosition.CenterScreen;

            Label label = new Label() { Text = "Введите логин и пароль", AutoSize = true, TextAlign = System.Drawing.ContentAlignment.MiddleCenter, Dock = DockStyle.Top };
            TextBox loginEdit = new TextBox() { Size = new System.Drawing.Size(200, 30), Location = new System.Drawing.Point(100, 100) };
            TextBox passwordEdit = new TextBox() { Size = new System.Drawing.Size(200, 30), Location = new System.Drawing.Point(100, 150), UseSystemPasswordChar = true };
            Button loginButton = new Button() { Text = "Вход", Size = new System.Drawing.Size(140, 50), Location = new System.Drawing.Point(130, 230) };

            loginButton.Click += (s, e) => CheckLogin(loginEdit.Text, passwordEdit.Text);

            this.Controls.Add(label);
            this.Controls.Add(loginEdit);
            this.Controls.Add(passwordEdit);
            this.Controls.Add(loginButton);

            this.BackColor = System.Drawing.Color.FromArgb(255, 228, 215);
            this.Font = new System.Drawing.Font("Bryndan Write", 15);
        }

        private void CheckLogin(string login, string password)
        {
            if (login == "admin" && password == "1111")
            {
                MessageBox.Show("Вход выполнен!", "Успешно", MessageBoxButtons.OK, MessageBoxIcon.Information);
                StudentProfileWindow studentProfileWindow = new StudentProfileWindow();
                studentProfileWindow.Show();
                this.Hide();
            }
            else
            {
                MessageBox.Show("Неверный логин или пароль!", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
    }

    // Главное окно профиля студента
    public partial class StudentProfileWindow : Form
    {
        private int counter;
        private string imagePath;

        public StudentProfileWindow()
        {
            InitializeComponent();
            LoadCounter();
        }

        private void InitializeComponent()
        {
            this.Text = "Личное дело студента";
            this.ClientSize = new System.Drawing.Size(632, 518);
            this.StartPosition = FormStartPosition.CenterScreen;

            Label headerLabel = new Label() { Text = "Личное дело студента", AutoSize = true, Dock = DockStyle.Top, TextAlign = System.Drawing.ContentAlignment.MiddleCenter };
            this.Controls.Add(headerLabel);

            // Инициализация полей формы
            // Код для создания текстовых полей и кнопок и их расположения...
            // (ресурсы и расположение аналогичны предыдущему примеру на Python)

            Button saveButton = new Button() { Text = "Сохранить", Dock = DockStyle.Bottom };
            saveButton.Click += (s, e) => SaveProfile();
            this.Controls.Add(saveButton);

            Button backButton = new Button() { Text = "Выход", Dock = DockStyle.Bottom };
            backButton.Click += (s, e) => BackToLogin();
            this.Controls.Add(backButton);

            Button photoButton = new Button() { Text = "Выбрать изображение", Dock = DockStyle.Bottom };
            photoButton.Click += (s, e) => OpenImage();
            this.Controls.Add(photoButton);
        }

        private void LoadCounter()
        {
            try
            {
                if (File.Exists("counter.txt"))
                {
                    string content = File.ReadAllText("counter.txt");
                    counter = int.Parse(content.Trim());
                }
                else
                {
                    counter = 1;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка загрузки: {ex.Message}", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                counter = 1;
            }
        }

        private void OpenImage()
        {
            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                openFileDialog.Filter = "Image Files (*.png; *.jpg; *.jpeg; *.bmp; *.gif)|*.png;*.jpg;*.jpeg;*.bmp;*.gif";
                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    imagePath = openFileDialog.FileName;
                    // Код для отображения изображения
                }
            }
        }

        private void SaveProfile()
        {
            try
            {
                // Проверка на заполнение обязательных полей...

                string dataToSave = $"Номер дела: {counter}\n" +
                                    $"Фото: {imagePath}\n" +
                                    // добавьте остальную информацию о профиле...

                File.AppendAllText("student_profile_data.txt", dataToSave);
                
                MessageBox.Show("Данные сохранены.", "Успех", MessageBoxButtons.OK, MessageBoxIcon.Information);
                
                counter++;
                SaveCounter();
                // Очищение полей...
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка при сохранении данных: {ex.Message}", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void SaveCounter()
        {
            try
            {
                File.WriteAllText("counter.txt", counter.ToString());
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка при сохранении счётчика: {ex.Message}", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void BackToLogin()
        {
            LoginWindow loginWindow = new LoginWindow();
            loginWindow.Show();
            this.Close();
        }
    }

    // Основной класс программы
    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new LoginWindow());
        }
    }
}
