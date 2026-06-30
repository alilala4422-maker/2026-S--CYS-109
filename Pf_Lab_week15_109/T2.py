def random(n):
    if n==0:
        return n
    print(n)
    random(n-1)
random(6)