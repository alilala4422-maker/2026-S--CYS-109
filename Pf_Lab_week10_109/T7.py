s = int(input("Enter no. of students: "))
i = 0
while (i < s):
    i = i+1
    sn = input("\nStudent name: ")
    reg = input("Reg. No: ")
    to = float(input("Total marks: "))
    ob = float(input("Obtained marks: "))
    print(f"\nStudent {i} name:", sn)
    print("Reg. No:", reg)
    per = (ob * 100) / to
    print(f"Percentage: {per}%")
    if (per >= 90):
        grade = "A"
    elif (per >= 85):
        grade = "A-"
    elif (per >= 80):
        grade = "B+"
    elif (per >= 75):
        grade = "B"
    elif (per >= 70):
        grade = "B-"
    elif (per >= 65):
        grade = "C+"
    elif (per >= 60):
        grade = "C"
    elif (per >= 55):
        grade = "C-"
    elif (per >= 50):
        grade = "D"
    else:
        grade = "F"
    print("Grade:", grade)