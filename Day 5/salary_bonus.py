#A company decided to give bonus of 5% to the employee. if his/her year of service is more than 5 years. as user for their salary and year experience of service

salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = 0.05 * salary
    print("Bonus :", bonus)
else:
    print("No Bonus")