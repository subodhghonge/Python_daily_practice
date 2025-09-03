#1. Reverse a string without slicing.

n = input("Enter a string to reverse : ")

for i in range(len(n)-1, -1, -1):
    print(n[i], end="")
print()

#2. Reverse a string with slicing method
n = input("Enter a string to reverse : ")

print(n[::-1])

