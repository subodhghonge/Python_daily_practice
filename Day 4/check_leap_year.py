a = int(input("Enter a year:"))

if (a % 4 ==0 or a % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")