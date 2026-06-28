# data.py  Movie class and movie list
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
registered_users = []

ADMIN_USER = "admin"
ADMIN_PASS = "admin123"