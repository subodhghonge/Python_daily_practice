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

#7) to print the pattern using for loop
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    for i in range(i):
        print("*", end=" ")
    print()