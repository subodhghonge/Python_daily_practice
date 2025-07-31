# #3) to accept basic salary of employee
# if basic salary is greater than 10000 then
# hra - 10% of basic salary, ta = 5% of bs, bonus = 2400,
# otherwise 
# hra - 5% of basic salary, ta = 1200 of bs, bonus = 1000
# then calculate netsalary of employee

bs = int(input("Enter your salary: "))
if bs > 10000:
    hra = bs * (10/100)
    ta = bs *(5/100)
    bonus = 2400
else:
    hra = bs * (5/100)
    ta = (1200)
    bonus = 1000

netsal = bs + hra + ta + bonus
print("hra =", hra,"ta =", ta,"bonus =", bonus)
print(netsal)