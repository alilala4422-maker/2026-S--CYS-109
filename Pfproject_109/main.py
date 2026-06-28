# main.py Main entry point to connecting all windows
import sys
import warnings
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from ui_main import Ui_MainWindow as Ui_Welcome
from user import UserLoginWindow, UserMenuWindow
from admin import AdminMenuWindow
import data

warnings.filterwarnings("ignore", category=DeprecationWarning)

class WelcomeWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = Ui_Welcome()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.btn_user.clicked.connect(self.go_to_user_login)
        self.ui.btn_admin.clicked.connect(self.go_to_admin_login)
        self.ui.btn_exit.clicked.connect(QApplication.quit)

    def go_to_user_login(self):
        self.stacked_widget.setCurrentIndex(1)

    def go_to_admin_login(self):
        self.stacked_widget.setCurrentIndex(2)

class AdminLoginWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        from ui_admin_login import Ui_MainWindow as Ui_AdminLogin
        self.ui = Ui_AdminLogin()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.attempts = 3
        self.ui.btn_login.clicked.connect(self.handle_login)
        self.ui.btn_back.clicked.connect(self.go_back)

    def handle_login(self):
        username = self.ui.input_username.text().strip()
        password = self.ui.input_password.text().strip()

        if username == data.ADMIN_USER and password == data.ADMIN_PASS:
            self.ui.lbl_error.setText("")
            self.ui.input_username.clear()
            self.ui.input_password.clear()
            self.attempts = 3
            admin_menu_window = self.stacked_widget.widget(4)
            admin_menu_window.load_movies()
            self.stacked_widget.setCurrentIndex(4)
        else:
            self.attempts -= 1
            if self.attempts <= 0:
                self.ui.lbl_error.setStyleSheet("color: red;")
                self.ui.lbl_error.setText("Too many failed attempts. Closing app.")
                self.ui.btn_login.setEnabled(False)
            else:
                self.ui.lbl_error.setStyleSheet("color: orange;")
                self.ui.lbl_error.setText(f"Invalid credentials! {self.attempts} left.")

    def go_back(self):
        self.ui.input_username.clear()
        self.ui.input_password.clear()
        self.ui.lbl_error.setText("")
        self.stacked_widget.setCurrentIndex(0)

def apply_theme(app):
    dark_stylesheet = """
        QMainWindow, QDialog { background-color: #1e1e24; color: #ffffff; }
        QLabel { color: #ffffff; }
        QPushButton { background-color: #e8c84a; color: #1e1e24; border-radius: 5px; font-weight: bold; border: none; }
        QPushButton:hover { background-color: #ffd954; }
        QLineEdit { background-color: #2b2b36; color: #ffffff; border: 1px solid #444454; border-radius: 4px; padding: 4px; }
        QTableWidget { background-color: #2b2b36; color: #ffffff; gridline-color: #444454; border: 1px solid #444454; }
        QHeaderView::section { background-color: #3e3e4f; color: #ffffff; padding: 4px; border: 1px solid #444454; }
    """
    app.setStyleSheet(dark_stylesheet)

def main():
    app = QApplication(sys.argv)
    apply_theme(app)
    stacked_widget = QStackedWidget()

    welcome = WelcomeWindow(stacked_widget)
    user_login = UserLoginWindow(stacked_widget)
    admin_login = AdminLoginWindow(stacked_widget)
    user_menu = UserMenuWindow(stacked_widget)
    admin_menu = AdminMenuWindow(stacked_widget)

    stacked_widget.addWidget(welcome)
    stacked_widget.addWidget(user_login)
    stacked_widget.addWidget(admin_login)
    stacked_widget.addWidget(user_menu)
    stacked_widget.addWidget(admin_menu)

    stacked_widget.setCurrentIndex(0)
    stacked_widget.resize(900, 650)
    stacked_widget.setWindowTitle("ECHOPLEX Cinema System")
    stacked_widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()