def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter your choice: "))
if choice == 1:
    f = float(input("Enter Temperature in Fahrenheit: "))
    print("Temperature in Celsius =", fahrenheit_to_celsius(f))
elif choice == 2:
    c = float(input("Enter Temperature in Celsius: "))
    print("Temperature in Fahrenheit =", celsius_to_fahrenheit(c))
else:
    print("Invalid Choice")