import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
D = b * b - 4 * a * c
print("Discriminant =", D)
if D > 0:
    print("Roots are Real, Distinct and Irrational")
    sqrt_D = math.sqrt(D)
    root1 = (-b + sqrt_D) / (2 * a)
    root2 = (-b - sqrt_D) / (2 * a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif D == 0:
    print("Roots are Real, Equal and Rational")
    root = -b / (2 * a)
    print("Root 1 =", root)
    print("Root 2 =", root)
else:
    print("Roots are Imaginary")
    real = -b / (2 * a)
    imaginary = math.sqrt(-D) / (2 * a)
    print("Root 1 =", real, "+", imaginary, "i")
    print("Root 2 =", real, "-", imaginary, "i")