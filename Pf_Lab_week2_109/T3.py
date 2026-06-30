# Prime numbers in a range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
sum_prime = 0
print("Prime Numbers are:")
for num in range(start, end + 1):
    if num > 1:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num, end=" ")
            sum_prime += num
print("\nSum of Prime Numbers =", sum_prime)