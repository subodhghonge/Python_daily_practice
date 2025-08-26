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
