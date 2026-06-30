list = [1,2,3,4,5]
emptylist = []
for i in range(len(list)):
    emptylist.append(list[i]**2)
print(emptylist)
#lambda function
n = lambda x: x**2
for x in list:
    print(n(x))