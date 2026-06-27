# Cinema Ticket Booking System
# 2026_CYS_109           PF_Lab_Final project

# Single admin with password
admin_username = "admin"
admin_password = "admin123"
users = []

# LOGIN FUNCTIONS

def user_login():
    username = input("Enter Username: ")
    if username in users:
        print(f"Welcome back, {username}!\n")
        user_menu()
    else:
        print(f"Username '{username}' not found.")
        choice = input("You have not registered yet. Do you want to register? (yes/no): ")
        if choice.lower() == "yes":
            users.append(username)
            print(f"Account created! Welcome, {username}!\n")
            user_menu()
        else:
            print("Returning to main menu.\n")

def admin_login():
    attempts = 0
    while attempts < 3:
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")
        if username == admin_username and password == admin_password:
            print("Admin Login Successful\n")
            admin_menu()
            return
        else:
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"Wrong credentials. {remaining} attempt(s) left\n")
            else:
                print("Too many failed attempts. Exiting program.\n")
                exit()

class Movie:
    def __init__(self, name, date, time, price, seats):
        self.name = name
        self.date = date
        self.time = time
        self.price = price
        self.seats = seats

# Sample schedule

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

# USER FUNCTIONS

def view_movies():
    print("\nMOVIE SCHEDULE")
    for i in range(len(movies)):
        print(
            f"{i+1}. {movies[i].name} | Date: {movies[i].date} | Time: {movies[i].time} | Price: Rs.{movies[i].price} | Seats: {movies[i].seats}"
        )

def view_seats():
    print("\nAVAILABLE SEATS")
    for i in range(len(movies)):
        print(f"{i+1}. {movies[i].name} | Seats Available: {movies[i].seats}")

def book_ticket():
    while True:
        view_movies()
        choice = int(input("Select Movie Number: "))
        if choice >= 1 and choice <= len(movies):
            seats = int(input("Enter number of tickets: "))
            movie = movies[choice - 1]
            if seats <= movie.seats:
                total = seats * movie.price
                print("Tickets:", seats)
                print("Price per ticket: Rs.", movie.price)
                print("Total Amount to Pay: Rs.", total)
                amount = int(input("Enter Payment Amount: Rs. "))
                if amount == total:
                    movie.seats -= seats
                    print("Payment Successful!")
                    print("Ticket Booked Successfully")
                    print("Remaining Seats:", movie.seats)
                elif amount > total:
                    change = amount - total
                    movie.seats -= seats
                    print("Payment Successful!")
                    print("Your Change: Rs.", change)
                    print("Ticket Booked Successfully")
                    print("Remaining Seats:", movie.seats)
                else:
                    print("Insufficient Amount. Ticket Not Booked.")
            else:
                print("Not Enough Seats")
        else:
            print("Invalid Choice")
        again = input("\nDo you want to book another ticket? (yes/no): ")
        if again.lower() != "yes":
            print("Returning to menu.")
            break

def user_menu():
    while True:
        print("\nUSER MENU")
        print("1. View Movies")
        print("2. Book Ticket")
        print("3. View Available Seats")
        print("4. Logout")
        option = input("Choose Option: ")
        if option == "1":
            view_movies()
        elif option == "2":
            book_ticket()
        elif option == "3":
            view_seats()
        elif option == "4":
            print("Logged Out")
            break
        else:
            print("Invalid Option")

# ADMIN FUNCTIONS

def add_movie():
    while True:
        name  = input("Movie Name: ")
        date  = input("Date (e.g. 15-June): ")
        time  = input("Time (e.g. 5:00 PM): ")
        price = int(input("Ticket Price (Rs.): "))
        seats = int(input("Total Seats: "))
        new_movie = Movie(name, date, time, price, seats)
        movies.append(new_movie)
        print("Movie Added Successfully")
        print("Name:", new_movie.name)
        print("Date:", new_movie.date)
        print("Time:", new_movie.time)
        print("Price: Rs.", new_movie.price)
        print("Seats:", new_movie.seats)
        again = input("\nDo you want to add another movie? (yes/no): ")
        if again.lower() != "yes":
            break

def edit_movie():
    view_movies()
    i= int(input("Movie Number: "))
    index= i-1
    if index >= 0 and index < len(movies):
        movies[index].name  = input("New Name: ")
        movies[index].date  = input("New Date: ")
        movies[index].time  = input("New Time: ")
        movies[index].price = int(input("New Price (Rs.): "))
        print("Movie Updated")
    else:
        print("Invalid Movie")

def delete_movie():
    view_movies()
    i = int(input("Movie Number: "))
    index = i - 1
    if index >= 0 and index < len(movies):
        movies.pop(index)
        print("Movie Deleted")
    else:
        print("Invalid Movie")

def update_seats():
    view_movies()
    i = int(input("Movie Number: "))
    index = i - 1
    if index >= 0 and index < len(movies):
        seats = int(input("New Seat Count: "))
        movies[index].seats = seats
        print("Seats Updated")
    else:
        print("Invalid Movie")

def admin_menu():
    while True:
        print("\nADMIN MENU")
        print("1. Add Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. Update Seats")
        print("5. View Schedule")
        print("6. Logout")
        option = input("Choose Option: ")
        if option == "1":
            add_movie()
        elif option == "2":
            edit_movie()
        elif option == "3":
            delete_movie()
        elif option == "4":
            update_seats()
        elif option == "5":
            view_movies()
        elif option == "6":
            print("Logged Out")
            break
        else:
            print("Invalid Option")

# MAIN PROGRAM

while True:
    print("\nCINEMA TICKET BOOKING ")
    print("\nWelcome to ECHOPLEX\n")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Exit")
    choice = input("Select Option: ")
    if choice == "1":
        user_login()
    elif choice == "2":
        admin_login()
    elif choice == "3":
        print("Thank You")
        break
    else:
        print("Invalid Input")