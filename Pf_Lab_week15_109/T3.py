
#Factorial
def X(n):
    if n==0 or n == 1:
        return 1
    else:
        return n*X(n-1)
print(X(5))