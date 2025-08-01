day = int(input('Enter a valid date : '))
month = int(input('Enter a valid month : '))
year = int(input('Enter a valid year :'))

while True:
    if (day >= 1 and day <= 31) and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and year >=1000:
        print(day,"-",month,"-",year," Date is valid")
    elif(day >= 1 and day <=30) and (month == 4 or month == 6 or month == 9 or month == 11) and year >=1000:
        print(day,"-",month,"-",year," Date is valid")
    elif(month == 2):
        if(day>=1 and day<=29) and (year % 4 == 0) and (year % 400 == 0 or year >=1000):
            print(day,"-",month,"-",year," Date is valid")
        elif(day>=1 and day<=28) and (year>1000):
            print(day,"-",month,"-",year," Date is valid")
        else:
            print(day,"-",month,"-",year," Date is Invalid")
    else:
        print(day,"-",month,"-",year," Date is Invalid")
        break