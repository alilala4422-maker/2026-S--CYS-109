# Program to calculate ECAT Aggregate
e_tot = float(input("Enter ECAT Total Marks: "))
e_obt = float(input("Enter ECAT Obtained Marks: "))
i_tot = float(input("Enter Intermediate Part-1 Total Marks: "))
i_obt = float(input("Enter Intermediate Part-1 Obtained Marks: "))
m_tot = float(input("Enter Matric Total Marks: "))
m_obt = float(input("Enter Matric Obtained Marks: "))

e_pct = (e_obt / e_tot) * 100
i_pct = (i_obt / i_tot) * 100
m_pct = (m_obt / m_tot) * 100
agg = (e_pct * 0.33) + (i_pct * 0.50) + (m_pct * 0.17)
print("ECAT % =", e_pct)
print("Inter % =", i_pct)
print("Matric % =", m_pct)
print("Aggregate =", round(agg, 2), "%")