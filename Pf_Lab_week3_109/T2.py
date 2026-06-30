# Lambda function to calculate product
multiply = lambda x, y: x * y
# User Defined Function
def table(func, number):
    print("Multiplication Table of", number)
    for i in range(1, 11):
        print(number, "x", i, "=", func(number, i))
num = int(input("Enter a number: "))
table(multiply, num)