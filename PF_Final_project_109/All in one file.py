#  ECHOPLEX Cinema — PyQt5 GUI Application
#  2026_CYS_109  |  PF Lab Final Project
#  Run:  python echoplex_cinema.py

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QDialog, QFormLayout, QSpinBox, QHeaderView,
    QFrame, QSizePolicy
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QColor, QPalette

STYLESHEET = """
QWidget {
    background-color: #0A0A0A;
    color: #FFFFFF;
    font-family: Arial;
    font-size: 13px;
}

/* ── Main window title bar ── */
QMainWindow {
    background-color: #0A0A0A;
}

/* ── Generic labels ── */
QLabel {
    color: #FFFFFF;
    background-color: transparent;
}
QLabel#title_label {
    color: #FFD700;
    font-size: 32px;
    font-weight: bold;
    letter-spacing: 4px;
}
QLabel#subtitle_label {
    color: #FFFFFF;
    font-size: 16px;
    letter-spacing: 2px;
}
QLabel#section_label {
    color: #FFD700;
    font-size: 18px;
    font-weight: bold;
}
QLabel#info_label {
    color: #AAAAAA;
    font-size: 12px;
}
QLabel#welcome_label {
    color: #FFD700;
    font-size: 15px;
    font-weight: bold;
}

/* ── Line edits ── */
QLineEdit {
    background-color: #1A1A1A;
    color: #FFFFFF;
    border: 1px solid #444444;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 13px;
}
QLineEdit:focus {
    border: 1px solid #FFD700;
}
QLineEdit::placeholder {
    color: #666666;
}

/* ── Primary (Yellow) button ── */
QPushButton {
    background-color: #FFD700;
    color: #0A0A0A;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #FFC200;
}
QPushButton:pressed {
    background-color: #E6B000;
}

/* ── Secondary (dark) button ── */
QPushButton#secondary_btn {
    background-color: #2A2A2A;
    color: #FFD700;
    border: 1px solid #FFD700;
}
QPushButton#secondary_btn:hover {
    background-color: #333333;
}

/* ── Danger (red) button ── */
QPushButton#danger_btn {
    background-color: #8B0000;
    color: #FFFFFF;
    border: none;
}
QPushButton#danger_btn:hover {
    background-color: #A00000;
}

/* ── Table ── */
QTableWidget {
    background-color: #1A1A1A;
    color: #FFFFFF;
    gridline-color: #333333;
    border: 1px solid #333333;
    border-radius: 6px;
    selection-background-color: #FFD700;
    selection-color: #0A0A0A;
    font-size: 12px;
}
QTableWidget::item {
    padding: 6px 10px;
}
QHeaderView::section {
    background-color: #FFD700;
    color: #0A0A0A;
    font-weight: bold;
    font-size: 12px;
    padding: 8px;
    border: none;
}
QTableWidget::item:selected {
    background-color: #FFD700;
    color: #0A0A0A;
}

/* ── Spin box ── */
QSpinBox {
    background-color: #1A1A1A;
    color: #FFFFFF;
    border: 1px solid #444444;
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 13px;
}
QSpinBox:focus {
    border: 1px solid #FFD700;
}

/* ── Dialog ── */
QDialog {
    background-color: #0A0A0A;
}

/* ── Message box ── */
QMessageBox {
    background-color: #0A0A0A;
    color: #FFFFFF;
}
QMessageBox QPushButton {
    min-width: 80px;
    min-height: 30px;
}

/* ── Frame / cards ── */
QFrame#card_frame {
    background-color: #1A1A1A;
    border: 1px solid #333333;
    border-radius: 10px;
}
QFrame#yellow_line {
    background-color: #FFD700;
    max-height: 3px;
    min-height: 3px;
}
"""
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

class Movie:
    def __init__(self, name, date, time, price, seats):
        self.name  = name
        self.date  = date
        self.time  = time
        self.price = price
        self.seats = seats

movies = [
    Movie("Avengers",     "01-June", "3:00 PM", 500, 50),
    Movie("Frozen",       "02-June", "6:00 PM", 400, 40),
    Movie("Avatar",       "03-June", "9:00 PM", 600, 60),
    Movie("Batman",       "04-June", "5:00 PM", 450, 45),
    Movie("Spider Man",   "05-June", "8:00 PM", 550, 55),
    Movie("John Wick",    "08-June", "4:00 PM", 500, 50),
    Movie("Joker",        "09-June", "7:00 PM", 350, 35),
    Movie("Titanic",      "10-June", "2:00 PM", 700, 70),
    Movie("Iron Man",     "11-June", "6:00 PM", 450, 45),
    Movie("Interstellar", "12-June", "9:00 PM", 600, 60),
]

registered_users = []   # stored usernames
current_user     = None # logged-in username

# ─────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────
def make_label(text, obj_name=None, align=Qt.AlignLeft):
    lbl = QLabel(text)
    if obj_name:
        lbl.setObjectName(obj_name)
    lbl.setAlignment(align)
    return lbl

def make_button(text, obj_name=None, min_w=140, min_h=42):
    btn = QPushButton(text)
    if obj_name:
        btn.setObjectName(obj_name)
    btn.setMinimumSize(min_w, min_h)
    return btn

def make_separator():
    line = QFrame()
    line.setObjectName("yellow_line")
    line.setFrameShape(QFrame.HLine)
    return line

def movie_table(parent=None):
    tbl = QTableWidget(parent)
    tbl.setColumnCount(6)
    tbl.setHorizontalHeaderLabels(["#", "Movie", "Date", "Time", "Price (Rs.)", "Seats"])
    tbl.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
    tbl.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
    tbl.setEditTriggers(QTableWidget.NoEditTriggers)
    tbl.setSelectionBehavior(QTableWidget.SelectRows)
    tbl.setAlternatingRowColors(False)
    tbl.verticalHeader().setVisible(False)
    return tbl

def populate_table(tbl):
    tbl.setRowCount(len(movies))
    for i, m in enumerate(movies):
        tbl.setItem(i, 0, QTableWidgetItem(str(i + 1)))
        tbl.setItem(i, 1, QTableWidgetItem(m.name))
        tbl.setItem(i, 2, QTableWidgetItem(m.date))
        tbl.setItem(i, 3, QTableWidgetItem(m.time))
        tbl.setItem(i, 4, QTableWidgetItem(f"Rs. {m.price}"))
        tbl.setItem(i, 5, QTableWidgetItem(str(m.seats)))
        for col in range(6):
            item = tbl.item(i, col)
            item.setTextAlignment(Qt.AlignCenter)
            item.setForeground(QColor("#FFFFFF"))
            bg = QColor("#1A1A1A") if i % 2 == 0 else QColor("#222222")
            item.setBackground(bg)

def alert(title, msg, icon=QMessageBox.Information):
    box = QMessageBox()
    box.setWindowTitle(title)
    box.setText(msg)
    box.setIcon(icon)
    box.exec_()

class AddMovieDialog(QDialog):
    def __init__(self, parent=None, movie=None):
        super().__init__(parent)
        self.movie = movie
        self.setWindowTitle("Edit Movie" if movie else "Add Movie")
        self.setMinimumWidth(400)
        self.setModal(True)
        form = QFormLayout(self)
        form.setSpacing(14)
        form.setContentsMargins(24, 24, 24, 24)
        self.name_input  = QLineEdit(movie.name  if movie else "")
        self.date_input  = QLineEdit(movie.date  if movie else "")
        self.time_input  = QLineEdit(movie.time  if movie else "")
        self.price_input = QLineEdit(str(movie.price) if movie else "")
        self.seats_input = QLineEdit(str(movie.seats) if movie else "")
        self.date_input.setPlaceholderText("e.g. 15-June")
        self.time_input.setPlaceholderText("e.g. 5:00 PM")
        self.price_input.setPlaceholderText("e.g. 500")
        self.seats_input.setPlaceholderText("e.g. 50")
        form.addRow("Movie Name:", self.name_input)
        form.addRow("Date:",       self.date_input)
        form.addRow("Time:",       self.time_input)
        form.addRow("Price (Rs.):",self.price_input)
        form.addRow("Seats:",      self.seats_input)
        btn_row = QHBoxLayout()
        save_btn   = make_button("Save", min_w=110, min_h=38)
        cancel_btn = make_button("Cancel", obj_name="secondary_btn", min_w=110, min_h=38)
        btn_row.addStretch()
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(save_btn)
        save_btn.clicked.connect(self.save)
        cancel_btn.clicked.connect(self.reject)
        form.addRow(btn_row)
    def save(self):
        name  = self.name_input.text().strip()
        date  = self.date_input.text().strip()
        time  = self.time_input.text().strip()
        price = self.price_input.text().strip()
        seats = self.seats_input.text().strip()

        if not all([name, date, time, price, seats]):
            alert("Error", "All fields are required.", QMessageBox.Warning)
            return
        try:
            price = int(price)
            seats = int(seats)
        except ValueError:
            alert("Error", "Price and Seats must be numbers.", QMessageBox.Warning)
            return
        if self.movie:
            self.movie.name  = name
            self.movie.date  = date
            self.movie.time  = time
            self.movie.price = price
            self.movie.seats = seats
        else:
            movies.append(Movie(name, date, time, price, seats))

        self.accept()

class BookTicketDialog(QDialog):
    def __init__(self, movie_index, parent=None):
        super().__init__(parent)
        self.movie = movies[movie_index]
        self.setWindowTitle(f"Book Ticket — {self.movie.name}")
        self.setMinimumWidth(380)
        self.setModal(True)

        layout = QVBoxLayout(self)
        layout.setSpacing(14)
        layout.setContentsMargins(24, 24, 24, 24)

        # Movie info
        info = QFrame()
        info.setObjectName("card_frame")
        info_layout = QVBoxLayout(info)
        info_layout.setSpacing(4)
        info_layout.setContentsMargins(16, 12, 16, 12)

        info_layout.addWidget(make_label(self.movie.name, "section_label"))
        info_layout.addWidget(make_label(f"Date: {self.movie.date}  |  Time: {self.movie.time}", "info_label"))
        info_layout.addWidget(make_label(f"Price per ticket: Rs. {self.movie.price}", "info_label"))
        info_layout.addWidget(make_label(f"Available Seats: {self.movie.seats}", "info_label"))
        layout.addWidget(info)

        # Ticket count
        form = QFormLayout()
        form.setSpacing(10)
        self.tickets_input = QSpinBox()
        self.tickets_input.setMinimum(1)
        self.tickets_input.setMaximum(self.movie.seats if self.movie.seats > 0 else 1)
        self.tickets_input.setValue(1)
        self.tickets_input.valueChanged.connect(self.update_total)
        form.addRow("Number of Tickets:", self.tickets_input)

        self.total_label = make_label(f"Total: Rs. {self.movie.price}", "welcome_label")
        form.addRow("", self.total_label)
        layout.addLayout(form)

        layout.addWidget(make_separator())

        # Payment
        pay_form = QFormLayout()
        pay_form.setSpacing(10)
        self.payment_input = QLineEdit()
        self.payment_input.setPlaceholderText("Enter amount in Rs.")
        pay_form.addRow("Payment Amount:", self.payment_input)
        layout.addLayout(pay_form)

        btn_row = QHBoxLayout()
        cancel_btn = make_button("Cancel", "secondary_btn", min_w=110, min_h=38)
        confirm_btn = make_button("Confirm Booking", min_w=150, min_h=38)
        btn_row.addStretch()
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(confirm_btn)
        layout.addLayout(btn_row)

        cancel_btn.clicked.connect(self.reject)
        confirm_btn.clicked.connect(self.confirm)

    def update_total(self):
        total = self.tickets_input.value() * self.movie.price
        self.total_label.setText(f"Total: Rs. {total}")

    def confirm(self):
        tickets = self.tickets_input.value()
        total   = tickets * self.movie.price

        try:
            paid = int(self.payment_input.text().strip())
        except ValueError:
            alert("Error", "Please enter a valid payment amount.", QMessageBox.Warning)
            return

        if tickets > self.movie.seats:
            alert("Error", "Not enough seats available.", QMessageBox.Warning)
            return

        if paid < total:
            alert("Payment Failed",
                  f"Insufficient amount.\nRequired: Rs. {total}\nEntered: Rs. {paid}",
                  QMessageBox.Warning)
            return

        self.movie.seats -= tickets
        change = paid - total

        msg = (f"✅  Ticket Booked Successfully!\n\n"
               f"Movie:    {self.movie.name}\n"
               f"Tickets:  {tickets}\n"
               f"Total:    Rs. {total}\n"
               f"Paid:     Rs. {paid}\n")
        if change > 0:
            msg += f"Change:   Rs. {change}\n"
        msg += f"\nRemaining Seats: {self.movie.seats}"

        alert("Booking Confirmed", msg)
        self.accept()

class MainMenuPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(16)
        layout.setContentsMargins(60, 40, 60, 40)

        layout.addStretch()

        # Logo / title block
        title = make_label("ECHOPLEX", "title_label", Qt.AlignCenter)
        title.setFont(QFont("Arial", 48, QFont.Bold))
        layout.addWidget(title)

        sub = make_label("CINEMA", "subtitle_label", Qt.AlignCenter)
        sub.setFont(QFont("Arial", 22, QFont.Bold))
        layout.addWidget(sub)

        tagline = make_label("A Cinema Ticket Booking System", "info_label", Qt.AlignCenter)
        layout.addWidget(tagline)

        layout.addSpacing(10)
        layout.addWidget(make_separator())
        layout.addSpacing(10)

        # Buttons
        user_btn  = make_button("👤  User Login",  min_w=280, min_h=52)
        admin_btn = make_button("🔐  Admin Login", obj_name="secondary_btn", min_w=280, min_h=52)
        exit_btn  = make_button("Exit",            obj_name="danger_btn",    min_w=280, min_h=44)

        for btn in [user_btn, admin_btn, exit_btn]:
            btn.setFont(QFont("Arial", 13, QFont.Bold))
            layout.addWidget(btn, alignment=Qt.AlignCenter)

        layout.addSpacing(10)
        layout.addWidget(make_label("UET Lahore  ·  Programming Fundamentals Lab  ·  2026",
                                    "info_label", Qt.AlignCenter))
        layout.addStretch()

        user_btn.clicked.connect(lambda: stack.setCurrentIndex(1))
        admin_btn.clicked.connect(lambda: stack.setCurrentIndex(2))
        exit_btn.clicked.connect(QApplication.quit)


class UserLoginPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(14)
        layout.setContentsMargins(100, 40, 100, 40)

        layout.addStretch()
        layout.addWidget(make_label("USER LOGIN", "section_label", Qt.AlignCenter))
        layout.addWidget(make_separator())
        layout.addSpacing(10)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setMinimumHeight(42)
        self.username_input.returnPressed.connect(self.login)
        layout.addWidget(self.username_input)

        login_btn = make_button("Login / Register", min_w=260, min_h=46)
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn, alignment=Qt.AlignCenter)

        back_btn = make_button("← Back", "secondary_btn", min_w=120, min_h=38)
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn, alignment=Qt.AlignCenter)

        layout.addWidget(make_label("New users are automatically registered on first login.",
                                    "info_label", Qt.AlignCenter))
        layout.addStretch()

    def login(self):
        global current_user
        username = self.username_input.text().strip()
        if not username:
            alert("Error", "Please enter a username.", QMessageBox.Warning)
            return

        if username in registered_users:
            current_user = username
            alert("Welcome Back", f"Welcome back, {username}!")
        else:
            box = QMessageBox()
            box.setWindowTitle("New User")
            box.setText(f"Username '{username}' not found.\nDo you want to register?")
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            box.setDefaultButton(QMessageBox.Yes)
            if box.exec_() == QMessageBox.Yes:
                registered_users.append(username)
                current_user = username
                alert("Registered", f"Account created! Welcome, {username}!")
            else:
                return

        self.username_input.clear()
        self.stack.setCurrentIndex(3)   # → User Menu
        self.stack.widget(3).refresh()

    def go_back(self):
        self.username_input.clear()
        self.stack.setCurrentIndex(0)


class AdminLoginPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.attempts = 0
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(14)
        layout.setContentsMargins(100, 40, 100, 40)

        layout.addStretch()
        layout.addWidget(make_label("ADMIN LOGIN", "section_label", Qt.AlignCenter))
        layout.addWidget(make_separator())
        layout.addSpacing(10)

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Admin Username")
        self.user_input.setMinimumHeight(42)
        layout.addWidget(self.user_input)

        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Admin Password")
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.pass_input.setMinimumHeight(42)
        self.pass_input.returnPressed.connect(self.login)
        layout.addWidget(self.pass_input)

        self.attempts_label = make_label("3 attempts allowed", "info_label", Qt.AlignCenter)
        layout.addWidget(self.attempts_label)

        login_btn = make_button("Login", min_w=220, min_h=46)
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn, alignment=Qt.AlignCenter)

        back_btn = make_button("← Back", "secondary_btn", min_w=120, min_h=38)
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn, alignment=Qt.AlignCenter)

        layout.addStretch()

    def login(self):
        username = self.user_input.text().strip()
        password = self.pass_input.text().strip()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            self.attempts = 0
            self.attempts_label.setText("3 attempts allowed")
            self.user_input.clear()
            self.pass_input.clear()
            self.stack.setCurrentIndex(4)   # → Admin Menu
        else:
            self.attempts += 1
            remaining = 3 - self.attempts
            if remaining > 0:
                self.attempts_label.setText(f"Wrong credentials. {remaining} attempt(s) left.")
                alert("Failed", f"Wrong credentials. {remaining} attempt(s) left.", QMessageBox.Warning)
            else:
                alert("Locked Out",
                      "Too many failed attempts. The application will now close.",
                      QMessageBox.Critical)
                QApplication.quit()

    def go_back(self):
        self.attempts = 0
        self.attempts_label.setText("3 attempts allowed")
        self.user_input.clear()
        self.pass_input.clear()
        self.stack.setCurrentIndex(0)


class UserMenuPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(24, 20, 24, 20)

        # Header
        hdr = QHBoxLayout()
        self.welcome_lbl = make_label("Welcome!", "welcome_label")
        logout_btn = make_button("Logout", "secondary_btn", min_w=100, min_h=36)
        logout_btn.clicked.connect(self.logout)
        hdr.addWidget(self.welcome_lbl)
        hdr.addStretch()
        hdr.addWidget(logout_btn)
        layout.addLayout(hdr)
        layout.addWidget(make_separator())

        layout.addWidget(make_label("MOVIE SCHEDULE", "section_label"))

        self.table = movie_table(self)
        layout.addWidget(self.table)

        # Action buttons
        btn_row = QHBoxLayout()
        btn_row.setSpacing(12)

        book_btn  = make_button("🎟  Book Ticket", min_w=180, min_h=44)
        seats_btn = make_button("💺  View Seats",  obj_name="secondary_btn", min_w=160, min_h=44)
        refresh_btn = make_button("↻  Refresh",    obj_name="secondary_btn", min_w=110, min_h=44)

        book_btn.clicked.connect(self.book_ticket)
        seats_btn.clicked.connect(self.view_seats)
        refresh_btn.clicked.connect(self.refresh)

        btn_row.addWidget(book_btn)
        btn_row.addWidget(seats_btn)
        btn_row.addStretch()
        btn_row.addWidget(refresh_btn)
        layout.addLayout(btn_row)

    def refresh(self):
        self.welcome_lbl.setText(f"Welcome, {current_user}!" if current_user else "Welcome!")
        populate_table(self.table)

    def book_ticket(self):
        row = self.table.currentRow()
        if row < 0:
            alert("Select Movie", "Please select a movie from the table first.", QMessageBox.Warning)
            return
        if movies[row].seats <= 0:
            alert("No Seats", "Sorry, this movie is sold out.", QMessageBox.Warning)
            return
        dlg = BookTicketDialog(row, self)
        if dlg.exec_() == QDialog.Accepted:
            populate_table(self.table)

    def view_seats(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Available Seats")
        dlg.setMinimumWidth(420)
        layout = QVBoxLayout(dlg)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        layout.addWidget(make_label("AVAILABLE SEATS", "section_label"))
        layout.addWidget(make_separator())

        tbl = QTableWidget()
        tbl.setColumnCount(3)
        tbl.setHorizontalHeaderLabels(["#", "Movie", "Seats Available"])
        tbl.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        tbl.setEditTriggers(QTableWidget.NoEditTriggers)
        tbl.verticalHeader().setVisible(False)
        tbl.setRowCount(len(movies))
        for i, m in enumerate(movies):
            tbl.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            tbl.setItem(i, 1, QTableWidgetItem(m.name))
            seats_item = QTableWidgetItem(str(m.seats))
            seats_item.setForeground(QColor("#4CAF50") if m.seats > 0 else QColor("#F44336"))
            tbl.setItem(i, 2, seats_item)
            for col in range(3):
                if tbl.item(i, col):
                    tbl.item(i, col).setTextAlignment(Qt.AlignCenter)
                    tbl.item(i, col).setForeground(
                        tbl.item(i, col).foreground()
                        if col == 2 else QColor("#FFFFFF")
                    )
                    bg = QColor("#1A1A1A") if i % 2 == 0 else QColor("#222222")
                    tbl.item(i, col).setBackground(bg)
        layout.addWidget(tbl)
        close_btn = make_button("Close", min_w=100, min_h=38)
        close_btn.clicked.connect(dlg.accept)
        layout.addWidget(close_btn, alignment=Qt.AlignRight)
        dlg.exec_()

    def logout(self):
        global current_user
        current_user = None
        self.stack.setCurrentIndex(0)


class AdminMenuPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(24, 20, 24, 20)

        # Header
        hdr = QHBoxLayout()
        hdr.addWidget(make_label("ADMIN PANEL", "section_label"))
        hdr.addStretch()
        logout_btn = make_button("Logout", "secondary_btn", min_w=100, min_h=36)
        logout_btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        hdr.addWidget(logout_btn)
        layout.addLayout(hdr)
        layout.addWidget(make_separator())

        layout.addWidget(make_label("MOVIE SCHEDULE", "info_label"))

        self.table = movie_table(self)
        layout.addWidget(self.table)

        # Action buttons
        btn_row = QHBoxLayout()
        btn_row.setSpacing(10)

        add_btn    = make_button("➕  Add Movie",    min_w=150, min_h=44)
        edit_btn   = make_button("✏️  Edit Movie",   obj_name="secondary_btn", min_w=150, min_h=44)
        delete_btn = make_button("🗑  Delete Movie", obj_name="danger_btn",    min_w=150, min_h=44)
        seats_btn  = make_button("💺  Update Seats", obj_name="secondary_btn", min_w=150, min_h=44)

        add_btn.clicked.connect(self.add_movie)
        edit_btn.clicked.connect(self.edit_movie)
        delete_btn.clicked.connect(self.delete_movie)
        seats_btn.clicked.connect(self.update_seats)

        for btn in [add_btn, edit_btn, delete_btn, seats_btn]:
            btn_row.addWidget(btn)
        btn_row.addStretch()
        layout.addLayout(btn_row)

    def refresh(self):
        populate_table(self.table)

    def showEvent(self, event):
        populate_table(self.table)
        super().showEvent(event)

    def add_movie(self):
        dlg = AddMovieDialog(self)
        if dlg.exec_() == QDialog.Accepted:
            populate_table(self.table)
            alert("Success", "Movie added successfully!")

    def edit_movie(self):
        row = self.table.currentRow()
        if row < 0:
            alert("Select Movie", "Please select a movie to edit.", QMessageBox.Warning)
            return
        dlg = AddMovieDialog(self, movie=movies[row])
        if dlg.exec_() == QDialog.Accepted:
            populate_table(self.table)
            alert("Success", "Movie updated successfully!")

    def delete_movie(self):
        row = self.table.currentRow()
        if row < 0:
            alert("Select Movie", "Please select a movie to delete.", QMessageBox.Warning)
            return
        box = QMessageBox()
        box.setWindowTitle("Confirm Delete")
        box.setText(f"Delete '{movies[row].name}'?")
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if box.exec_() == QMessageBox.Yes:
            movies.pop(row)
            populate_table(self.table)
            alert("Deleted", "Movie deleted successfully.")

    def update_seats(self):
        row = self.table.currentRow()
        if row < 0:
            alert("Select Movie", "Please select a movie to update seats.", QMessageBox.Warning)
            return
        movie = movies[row]
        dlg = QDialog(self)
        dlg.setWindowTitle(f"Update Seats — {movie.name}")
        dlg.setMinimumWidth(320)
        dlg.setModal(True)
        layout = QVBoxLayout(dlg)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(14)
        layout.addWidget(make_label(f"Movie: {movie.name}", "welcome_label"))
        layout.addWidget(make_label(f"Current seats: {movie.seats}", "info_label"))
        form = QFormLayout()
        spin = QSpinBox()
        spin.setMinimum(0)
        spin.setMaximum(9999)
        spin.setValue(movie.seats)
        form.addRow("New Seat Count:", spin)
        layout.addLayout(form)
        btn_row = QHBoxLayout()
        cancel_btn = make_button("Cancel", "secondary_btn", min_w=100, min_h=38)
        save_btn   = make_button("Save",                    min_w=100, min_h=38)
        cancel_btn.clicked.connect(dlg.reject)
        save_btn.clicked.connect(dlg.accept)
        btn_row.addStretch()
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(save_btn)
        layout.addLayout(btn_row)
        if dlg.exec_() == QDialog.Accepted:
            movie.seats = spin.value()
            populate_table(self.table)
            alert("Updated", f"Seats updated to {movie.seats}.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ECHOPLEX Cinema")
        self.setMinimumSize(900, 620)
        self.resize(1050, 680)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Pages  (index must match setCurrentIndex calls above)
        self.main_page       = MainMenuPage(self.stack)     # 0
        self.user_login_page = UserLoginPage(self.stack)    # 1
        self.admin_login_page= AdminLoginPage(self.stack)   # 2
        self.user_menu_page  = UserMenuPage(self.stack)     # 3
        self.admin_menu_page = AdminMenuPage(self.stack)    # 4

        for page in [self.main_page, self.user_login_page, self.admin_login_page,
                     self.user_menu_page, self.admin_menu_page]:
            self.stack.addWidget(page)

        self.stack.setCurrentIndex(0)

#  ENTRY POINT
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLESHEET)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
