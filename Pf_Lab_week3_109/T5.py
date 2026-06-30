# Function to calculate GPA
def calc_gpa(tgp, tch):
    return tgp / tch
n = int(input("Enter number of subjects: "))
tgp = 0
tch = 0
for i in range(n):
    print("\nSubject", i + 1)
    gp = float(input("Enter Grade Point: "))
    ch = int(input("Enter Credit Hours: "))
    tgp += gp * ch
    tch += ch
gpa = calc_gpa(tgp, tch)
print("\nSemester GPA =", round(gpa, 2))