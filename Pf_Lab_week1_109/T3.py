# Program to check Palindrome Number
num = input("Enter a Number: ")
reverse = ""
i = len(num) - 1
while i >= 0:
    reverse = reverse + num[i]
    i = i - 1
if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")