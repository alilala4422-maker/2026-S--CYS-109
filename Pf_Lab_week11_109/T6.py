for i in range(1,9):
    for j in range(9-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    for l in range(i-1):
        print("*",end=" ")
    print()