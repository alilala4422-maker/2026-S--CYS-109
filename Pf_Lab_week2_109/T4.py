import random
import string
length = int(input("Enter password length: "))
uppercase = input("Include uppercase letters? (y/n): ")
lowercase = input("Include lowercase letters? (y/n): ")
digits = input("Include digits? (y/n): ")
special = input("Include special characters? (y/n): ")
characters = ""
if uppercase.lower() == "y":
    characters += string.ascii_uppercase
if lowercase.lower() == "y":
    characters += string.ascii_lowercase
if digits.lower() == "y":
    characters += string.digits
if special.lower() == "y":
    characters += string.punctuation
if characters == "":
    print("Please select at least one character type.")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Generated Password:", password)