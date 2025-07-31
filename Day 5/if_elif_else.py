#1. To find out greater number amoung 3 numbers
a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))
c = int(input("Enter a number 3: "))


if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
elif c > a and c > b:
    print("c is greater")
else:
    print("Enter a valid number")


#2. to enter 5 subjects marks from user and take sum and percent
sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 marks: "))
sub4 = int(input("Enter sub4 marks: "))
sub5 = int(input("Enter sub5 marks: "))

sum = sub1 + sub2 + sub3 + sub4 + sub5

per = (sum/500)*100

if per>=75:
    print("Distinction")
elif per>=65:
    print("First Class")
elif per>=55:
    print("Second Class")
else:
    print("Fail")