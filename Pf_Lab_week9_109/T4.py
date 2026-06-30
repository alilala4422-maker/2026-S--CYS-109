m = int(input("Total marks: "))
ob = int(input("Obtained Marks: "))
per = ((ob * 100) / m)
print("Percentage:", per)
if (per>=90):
  grade = 'A'
elif (per>=85):
  grade = 'A-'
elif (per>=80):
  grade = 'B+'
elif (per>=75):
  grade = 'B'
elif (per>=70):
  grade = 'B-'
elif (per>=65):
  grade = 'C+'
elif (per>=60):
  grade = 'C'
elif (per>=55):
  grade = 'C-'
elif (per>=50):
  grade = 'D'
else:
   grade = 'F'
print("Grade:", grade)