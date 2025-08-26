#1. Write a program to check if a number is prime, Armstrong, or perfect.
def prime():
    n = int(input("Enter Number to check wether it is Prime Number: "))
    if n <= 1:
        print("Not a Prime Number")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not a prime number")
                break
        else:
            print("Prime Number")

def armstrong(n):
    temp = n
    power = len(str(n))
    sum = 0

    for i in range(n):
        r = n % 10
        sum = sum + (r**power)
        n = n // 10
    
    return sum == temp

while True:
    print("""
          1. Prime Number
          2. Armstrong Number
          3. Perfect Number""")
    
    ch = int(input("Enter your choice: "))

    if ch == 1:
        prime()
    if ch == 2:
        n = int(input("Enter Number to check wether it is Armstrong: "))
        a = armstrong(n)

        if armstrong(n):
            print(f'{a}, {n} is a armstrong number')
        else:
            print(f'{a}, {n} is not a armstrong number')

#2. Find the factorial of a number using for loop and functions.
def factorial(n):
    fact = 1

    for i in range(1, n+1):
        fact = fact * i
    return fact

n = int(input("Enter Number to get factorial: "))
a = factorial(n)
print(a)

#3. Create a function that takes a number n and returns the sum of its digits.
def sum_digits(n):
    s = 0

    while n > 0:
        s += n%10
        n = n//10
    
    return s

n = int(input("Enter a number to get sum : "))
print(f'Sum of digits you entered are : {sum_digits(n)}')
