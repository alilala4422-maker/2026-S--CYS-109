n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
if r > n or n < 0 or r < 0:
    print("Invalid input.")
else:
    def factorial(num):
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        return fact
    n_fact = factorial(n)
    r_fact = factorial(r)
    nr_fact = factorial(n - r)
    permutation = n_fact // nr_fact
    combination = n_fact // (r_fact * nr_fact)
    print("Permutation (nPr) =", permutation)
    print("Combination (nCr) =", combination)