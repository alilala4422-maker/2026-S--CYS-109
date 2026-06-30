# Lambda function
upper = lambda s: s.upper()
def reverse_string(text):
    reversed_text = ""
    i = len(text) - 1
    while i >= 0:
        reversed_text = reversed_text + text[i]
        i = i - 1
    print("Reversed String:", reversed_text)
string = input("Enter a string: ")
uppercase = upper(string)
print("Uppercase String:", uppercase)
reverse_string(uppercase)