# Program to convert Bytes into MB and GB
bytes_value = float(input("Enter Bytes: "))

kb = bytes_value / 1024
mb = kb / 1024
gb = mb / 1024

print("Kilo Bytes =", kb)
print("Mega Bytes =", mb)
print("Giga Bytes =", gb)