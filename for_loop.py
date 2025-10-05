# #1. Print Numbers from 1 - 10
# for i in range(1, 11):
#     print(i, end=" ")

# #2. Print Even numbers till 20
# for i in range(0, 21, 2):
#     print(i, end=" ")

# #OR
# for i in range(0, 21):
#     if i%2==0:
#         print(i)

# #3. Print Odd number till 20
# print("Odd Numbers are :")
# for i in range(1, 21, 2):
#     print(i, end=" ")

# #OR
# for i in range(0, 21):
#     if i%2!=0:
#         print(i, end=" ")

# #4. print sqaure of numbers till 20
# for i in range(1, 21):
#     print(f"Square of {i} is : {i**2}")

# #5. Cube of numbers till 20
# for i in range(0, 21):
#     print(f"Cube of number {i} is : {i**3}")

# #6. display the factorial of given number
# n = int(input("Enter number : "))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(f"factorial of {n} is {fact}")

# ##Patterns
# #1) to print the pattern using for loop
# # * * * * *
# # * * * * *
# # * * * * *
# # * * * * *
# # * * * * *

# for i in range(1,6):
#     for j in range(1,6):
#         print("*", end=" ")
#     print()

# #2) to print the pattern using for loop
# # 1 1 1 1 1
# # 2 2 2 2 2
# # 3 3 3 3 3
# # 4 4 4 4 4
# # 5 5 5 5 5

# for i in range(1, 6):
#     for j in range(1,6):
#         print(i, end=" ")
#     print()

# #3) to print the pattern using for loop
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()

# #4) to print the pattern using for loop
# # *
# # * *
# # * * *
# # * * * *
# # * * * * *

# for i in range(1, 6,):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# #5) to print the pattern using for loop
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5

# for i in range(1, 6):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# #6) to print the pattern using for loop
# # 1 
# # 1 2 
# # 1 2 3 
# # 1 2 3 4
# # 1 2 3 4 5
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# #7) to print the pattern using for loop
# # * * * * *
# # * * * *
# # * * *
# # * *
# # *

# for i in range(5, 0, -1):
#     for i in range(i):
#         print("*", end=" ")
#     print()

# ## Problems
# #1) fibonacci series

# fs = 7
# a = 0
# b = 1

# for i in range(fs):
#     print(a, end=" ")
#     a, b = b, a+b

# #2) Reverse a Number
# n = 12345
# reverse = 0

# length = len(str(n))

# for i in range(length):
#     length = n % 10
#     reverse = reverse * 10 + length
#     n = n // 10

# print(reverse)

# #3)Sum of digits
# n = 12546
# sum = 0

# for i in range(n):
#     r = n % 10
#     sum += r
#     n = n // 10

# print(sum)

# #4) Armstrong Number
# n = 153
# temp = n
# power = len(str(n))
# sum = 0

# for i in range(n):
#     r = n % 10
#     sum = sum + (r**power)
#     n = n // 10

# print(sum)

# #5) Chech number is palindrom or not
# n = 12321
# temp = n
# reverse = 0

# while n>0:
#     r = n % 10
#     reverse = reverse * 10 + r
#     n = n // 10

# print(reverse)
# if temp == reverse:
#     print("Palindrom")
# else:
#     print("Not a Palindrom")

# #6) Prime Number

# n = int(input("Enter a Number : "))

# if n <= 1:
#     print(f"{n} is not a prime number")
# else:
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             print("Not a prime number")
#         else:
#             print("Prime Number")

# #7) Perfect Number

# n = int(input("Enter Number : "))
# sum = 0
# for i in range(1, n):
#     if n%i==0:
#         sum = sum + i

# if sum == n:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")