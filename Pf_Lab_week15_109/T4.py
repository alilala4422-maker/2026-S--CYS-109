#Fibonacci series
num = int(input("Series length: "))
def fib(n):
    num1 = 0
    num2 = 1
    for i in range(num):
        print(num1, end=" ")
        temp = num1
        num1 = num2
        num2 = temp + num2
fib(num)