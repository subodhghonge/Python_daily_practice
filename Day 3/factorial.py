n = int(input("Enter a number to find its factorial: "))
fact = 1

for i in range(1, n+1):
    fact *= i 
print(f"The factorial of {n} is {fact}")