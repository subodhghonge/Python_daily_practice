# Write a program to find eligibilty of admission for a professional course based on the following criteria
# Maths >= 65
# Physics >= 55
# Chemistry >= 50
# Total Marks >= 180

Maths = int(input("Enter Maths Marks: "))
Phy = int(input("Enter Pyhsics Marks: "))
chem = int(input("Enter Chemistry Marks: "))

total = Maths + Phy + chem

if (Maths >= 65 and Phy >= 55 and chem >= 50) and total >= 180:
    print("Eligible for admission criteria")
else:
    print("Not Eligible for admission")