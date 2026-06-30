x = input("Enter data: ")
def num(x):
    if x.isdigit():
        print("Integer")
    elif "." in x:
        print("Float")
    elif x.isalpha():
        print("String")
    else:
        print("Invalid")
num(x)