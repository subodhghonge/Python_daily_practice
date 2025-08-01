#1)Display Monument Based on City Name
city = input("Enter city name: ")

if city == "delhi":
    print("Monument: Red Fort")
elif city == "agra":
    print("Monument: Taj Mahal")
elif city == "jaipur":
    print("Monument: Jai Mahal")
else:
    print("City not in list")

#2) Road Tax Based on Bike Cost Price
cost_price = float(input("Enter the cost price of the bike: "))

if cost_price > 100000:
    tax = (15/100) * cost_price
elif cost_price > 50000:
    tax = (10/100) * cost_price
else:
    tax = (5/100) * cost_price

print("Road tax to be paid: Rs.", tax)

#3 Electricity Bill Calculator
units = int(input("Enter number of units consumed: "))

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + (units - 200) * 10

print("Total electricity bill: Rs.", bill)

#4 Enter Date is valid or not 


#5 Enter Character and display its ascii code
char = input("Enter a character: ")

if char == 'A':
    print("ASCII: 65")
elif char == 'B':
    print("ASCII: 66")
elif char == 'a':
    print("ASCII: 97")
else:
    print("Unknown character")

#6 Enter Character and print whether it is alphabets, digit, or special symbols
ch = input("Enter a character: ")

if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
    print("Alphabet")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special Symbol")
