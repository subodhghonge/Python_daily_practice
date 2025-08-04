#11 to display multiplication table of given number

n = int(input("Enter number to create a table: "))
mul = 1

for i in range(1, 11):
    mul = n * i
    print(n, '* ', i, '=', mul)