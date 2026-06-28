# user.py — Logic for user login and user menu dashboard
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QInputDialog
from ui_user_login import Ui_MainWindow as Ui_UserLogin
from ui_user_menu import Ui_MainWindow as Ui_UserMenu
import data


class UserLoginWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = Ui_UserLogin()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget

        # Connect buttons
        self.ui.btn_continue.clicked.connect(self.handle_login)
        self.ui.btn_back.clicked.connect(self.go_back)

    def handle_login(self):
        username = self.ui.input_username.text().strip()
        if not username:
            QMessageBox.warning(self, "Error", "Username cannot be empty!")
            return

        # Check if the user is already registered
        if username not in data.registered_users:
            # Explicitly ask the user if they want to register a new account
            reply = QMessageBox.question(
                self,
                "User Not Found",
                f"The username '{username}' does not exist.\nDo you want to register a new account?",
                QMessageBox.Yes | QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                data.registered_users.append(username)
                QMessageBox.information(self, "Welcome", f"New account successfully created for '{username}'!")
            else:
                # If they choose 'No', stop here and don't log them in
                return
        else:
            QMessageBox.information(self, "Welcome Back", f"Welcome back, {username}!")

        # Clear input field and proceed to the user dashboard panel
        self.ui.input_username.clear()
        user_menu_window = self.stacked_widget.widget(3)  # Index 3 is User Menu
        user_menu_window.set_user(username)
        self.stacked_widget.setCurrentIndex(3)

    def go_back(self):
        self.ui.input_username.clear()
        self.stacked_widget.setCurrentIndex(0)  # Back to welcome screen


class UserMenuWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = Ui_UserMenu()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.current_user = ""

        # Hide the table completely when the menu first loads
        self.ui.table_movies.setVisible(False)

        # Connect dashboard actions
        self.ui.btn_view.clicked.connect(self.show_only_movies)
        self.ui.btn_seats.clicked.connect(self.show_only_seats)
        self.ui.btn_book.clicked.connect(self.show_booking_flow)
        self.ui.btn_logout.clicked.connect(self.logout)

    def set_user(self, username):
        self.current_user = username
        self.ui.lbl_welcome.setText(f"Welcome, {username}")
        # Reset view state when a user logs in
        self.ui.table_movies.setVisible(False)
        self.ui.lbl_status.setText("Welcome! Please select an action from the menu above.")

    def show_only_movies(self):
        """Shows only the movie list columns, hiding seat numbers"""
        self.ui.table_movies.setVisible(True)
        self.ui.table_movies.setRowCount(0)
        self.ui.lbl_status.setText("Displaying active movie schedules.")

        for row_idx, movie in enumerate(data.movies):
            self.ui.table_movies.insertRow(row_idx)
            self.ui.table_movies.setItem(row_idx, 0, QTableWidgetItem(movie.name))
            self.ui.table_movies.setItem(row_idx, 1, QTableWidgetItem(movie.date))
            self.ui.table_movies.setItem(row_idx, 2, QTableWidgetItem(movie.time))
            self.ui.table_movies.setItem(row_idx, 3, QTableWidgetItem(str(movie.price)))
            self.ui.table_movies.setItem(row_idx, 4, QTableWidgetItem("Select 'Available Seats' to view"))

    def show_only_seats(self):
        """Shows only movie names and their respective remaining seating availability"""
        self.ui.table_movies.setVisible(True)
        self.ui.table_movies.setRowCount(0)
        self.ui.lbl_status.setText("Displaying seating availability details.")

        for row_idx, movie in enumerate(data.movies):
            self.ui.table_movies.insertRow(row_idx)
            self.ui.table_movies.setItem(row_idx, 0, QTableWidgetItem(movie.name))
            self.ui.table_movies.setItem(row_idx, 1, QTableWidgetItem("—"))
            self.ui.table_movies.setItem(row_idx, 2, QTableWidgetItem("—"))
            self.ui.table_movies.setItem(row_idx, 3, QTableWidgetItem("—"))
            self.ui.table_movies.setItem(row_idx, 4, QTableWidgetItem(f"{movie.seats} Seats Left"))

    def show_booking_flow(self):
        """Reveals full movie specs so the user can select rows to execute a booking"""
        self.ui.table_movies.setVisible(True)
        self.ui.table_movies.setRowCount(0)
        self.ui.lbl_status.setText(
            "Select a movie row from the table below, then click 'Book Ticket' again to confirm.")

        # Populate the complete dataset so they can make an informed choice
        for row_idx, movie in enumerate(data.movies):
            self.ui.table_movies.insertRow(row_idx)
            self.ui.table_movies.setItem(row_idx, 0, QTableWidgetItem(movie.name))
            self.ui.table_movies.setItem(row_idx, 1, QTableWidgetItem(movie.date))
            self.ui.table_movies.setItem(row_idx, 2, QTableWidgetItem(movie.time))
            self.ui.table_movies.setItem(row_idx, 3, QTableWidgetItem(str(movie.price)))
            self.ui.table_movies.setItem(row_idx, 4, QTableWidgetItem(str(movie.seats)))

        # Temporarily disconnect and redirect the button to trigger the ticket purchase prompt if a row is selected
        try:
            self.ui.btn_book.clicked.disconnect()
        except TypeError:
            pass
        self.ui.btn_book.clicked.connect(self.execute_ticket_purchase)

    def execute_ticket_purchase(self):
        selected_row = self.ui.table_movies.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a movie from the visible table below first.")
            return

        movie = data.movies[selected_row]
        if movie.seats <= 0:
            QMessageBox.critical(self, "Sold Out", "Sorry, this show is completely sold out!")
            return

        tickets, ok = QInputDialog.getInt(
            self, "Book Tickets",
            f"How many tickets for {movie.name}?",
            min=1, max=movie.seats
        )
        if not ok: return

        total_cost = tickets * movie.price

        while True:
            payment, ok = QInputDialog.getInt(
                self, "Payment Processing",
                f"Total Cost: Rs. {total_cost}\nEnter Amount Paid:"
            )
            if not ok: return

            if payment >= total_cost:
                change = payment - total_cost
                movie.seats -= tickets
                self.show_booking_flow()  # Refresh full view numbers
                QMessageBox.information(
                    self, "Success!",
                    f"Successfully booked {tickets} ticket(s)!\nChange: Rs. {change}"
                )
                break
            else:
                QMessageBox.warning(
                    self, "Payment Failed",
                    f"Insufficient amount! You still owe Rs. {total_cost - payment}"
                )

        # Reconnect the original state routing after checkout completes
        try:
            self.ui.btn_book.clicked.disconnect()
        except TypeError:
            pass
        self.ui.btn_book.clicked.connect(self.show_booking_flow)

    def logout(self):
        # Reset button connections if user logs out mid-booking flow
        try:
            self.ui.btn_book.clicked.disconnect()
        except TypeError:
            pass
        self.ui.btn_book.clicked.connect(self.show_booking_flow)
        self.current_user = ""
        self.stacked_widget.setCurrentIndex(0)