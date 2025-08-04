#1 to display 1 - 10 numbers
for i in range(1, 11, 1):
    print(i)

#2 to display even numbers between 1 to 20
for i in range(1, 21, 1):
    if i % 2 == 0:
        print("Even Numbers Are : ", i)

#3 to dislay odd numbers between 1 to 20
for i in range(1, 21, 1):
    if i % 2 != 0:
        print("Odd Numbers Are : ", i)  

#4 to display 10 to 1 numbers
for i in range(10, 0, -1):
    print(i)
