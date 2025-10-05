#1. calculate length of a string without using len()
a = str(input("Enter a string"))
count = 0

for i in a:
    count += 1

print("Length of string is : ", count)

#2. reverse of a string without using slicing
a = input("Enter a String : ")
n = len(a)

for i in range(n-1, -1, -1):
    print(a[i], end=" ")

#3. to check string is palindrome or not
a = input("Enter a String : ")

if a == a[::-1]:
    print("Palindrom")
else:
    print("Not a Palindrom")        

#4. to check string is anagram or not
a = "listen"
b = "silent"

if sorted(a) == sorted(b):
    print("Strings are anagram")
else:
    print("Not Anagram")

#5. to convert string to upper case, lower case, title case, capitalize
a = input("Enter a String : ")

print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.swapcase())

#6. convert a string to list
a = input("Enter a String : ")

print(a.split())

