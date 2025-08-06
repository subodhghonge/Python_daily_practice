import math

n = int(input("Enter numbers: "))

if n<=1:
    print("Not a Prime number")
else:
    for i in range(2, int(math.sqrt(n))+1):
        if n % 2 == 0:
            print("Not a prime number")
        else:
            print("Prime Number")