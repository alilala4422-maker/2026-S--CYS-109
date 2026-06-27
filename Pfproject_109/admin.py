# admin.py — Logic for admin menu operations
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QInputDialog, QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton
from ui_admin_menu import Ui_MainWindow as Ui_AdminMenu
import data

class MovieDialog(QDialog):
    def __init__(self, parent=None, movie=None):
        super().__init__(parent)
        self.setWindowTitle("Movie Details" if not movie else "Edit Movie Details")
        self.layout = QVBoxLayout(self)
        self.inputs = {}
        fields = [
            ("Name", movie.name if movie else ""),
            ("Date", movie.date if movie else ""),
            ("Time", movie.time if movie else ""),
            ("Price (Rs.)", str(movie.price) if movie else ""),
            ("Seats Available", str(movie.seats) if movie else "")
        ]
        for label_text, default_val in fields:
            self.layout.addWidget(QLabel(label_text))
            line_edit = QLineEdit(self)
            line_edit.setText(default_val)
            self.layout.addWidget(line_edit)
            self.inputs[label_text] = line_edit
        self.btn_save = QPushButton("Save", self)
        self.btn_save.clicked.connect(self.accept)
        self.layout.addWidget(self.btn_save)

    def get_data(self):
        return {label: widget.text().strip() for label, widget in self.inputs.items()}

class AdminMenuWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.ui = Ui_AdminMenu()
        self.ui.setupUi(self)
        self.stacked_widget = stacked_widget
        self.ui.btn_add.clicked.connect(self.add_movie)
        self.ui.btn_edit.clicked.connect(self.edit_movie)
        self.ui.btn_delete.clicked.connect(self.delete_movie)
        self.ui.btn_update_seats.clicked.connect(self.update_seats)
        self.ui.btn_logout.clicked.connect(self.logout)

    def load_movies(self):
        self.ui.table_movies.setRowCount(0)
        for row_idx, movie in enumerate(data.movies):
            self.ui.table_movies.insertRow(row_idx)
            self.ui.table_movies.setItem(row_idx, 0, QTableWidgetItem(movie.name))
            self.ui.table_movies.setItem(row_idx, 1, QTableWidgetItem(movie.date))
            self.ui.table_movies.setItem(row_idx, 2, QTableWidgetItem(movie.time))
            self.ui.table_movies.setItem(row_idx, 3, QTableWidgetItem(str(movie.price)))
            self.ui.table_movies.setItem(row_idx, 4, QTableWidgetItem(str(movie.seats)))

    def add_movie(self):
        dialog = MovieDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            res = dialog.get_data()
            try:
                if not res["Name"] or not res["Date"] or not res["Time"]:
                    raise ValueError("Fields cannot be empty.")
                new_movie = data.Movie(res["Name"], res["Date"], res["Time"], int(res["Price (Rs.)"]), int(res["Seats Available"]))
                data.movies.append(new_movie)
                self.load_movies()
                QMessageBox.information(self, "Success", f"'{new_movie.name}' added successfully!")
            except ValueError as e:
                QMessageBox.warning(self, "Input Error", f"Invalid data: {e}")

    def edit_movie(self):
        selected_row = self.ui.table_movies.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a movie to edit.")
            return
        movie = data.movies[selected_row]
        dialog = MovieDialog(self, movie)
        if dialog.exec_() == QDialog.Accepted:
            res = dialog.get_data()
            try:
                if not res["Name"] or not res["Date"] or not res["Time"]:
                    raise ValueError("Fields cannot be empty.")
                movie.name = res["Name"]
                movie.date = res["Date"]
                movie.time = res["Time"]
                movie.price = int(res["Price (Rs.)"])
                movie.seats = int(res["Seats Available"])
                self.load_movies()
                QMessageBox.information(self, "Success", "Movie updated successfully!")
            except ValueError as e:
                QMessageBox.warning(self, "Input Error", f"Invalid data: {e}")

    def delete_movie(self):
        selected_row = self.ui.table_movies.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a movie to delete.")
            return
        movie = data.movies[selected_row]
        confirm = QMessageBox.question(self, "Confirm Delete", f"Delete '{movie.name}'?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            data.movies.remove(movie)
            self.load_movies()

    def update_seats(self):
        selected_row = self.ui.table_movies.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a movie.")
            return
        movie = data.movies[selected_row]
        new_seats, ok = QInputDialog.getInt(self, "Update Seats", f"Seats for {movie.name}:", value=movie.seats, min=0)
        if ok:
            movie.seats = new_seats
            self.load_movies()

    def logout(self):
        self.stacked_widget.setCurrentIndex(0)