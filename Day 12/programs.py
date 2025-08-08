#1. calculate length of a string without using len()
a = str(input("Enter a string"))
count = 0

for i in a:
    count += 1

print("Length of string is : ", count)

#2. reverse of a string without using slicing
a = input("Enter a string: ")
n = len(a)

for i in range(n-1, -1, -1):
    print(a[i], end="")

#3) to check string is palindrome or not
n = input("Enter a string: ")

if n == n[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

#4)to check string is anagram or not
str1 = 'listen'
str2 = 'silent'

print(str1)
print(str2)

if sorted(str1) == sorted(str2):
    print("str is anagram")
else:
    print("str is not anagram")

#5)to convert string to upper case, lower case, title case, capitalize
a = "Kiran Academy"
b = "KIRAN ACADEMY"
c = "kIRAN academy"
print(a.upper())
print(b.lower())
print(b.title())
print(c.capitalize())

#6)convert a string to list
a = "apple mangoes banana cherry"
print(a.split())

b = "subodh@1123@ghonge"
print(b.split('@'))

#7)To count number of words in string
str ="python is a dynamic language"

count = len(str.split())

print("Number of words:",count)

#8)to display longest and smallest word
str ="python is a dynamic language"

words = str.split()

print("Largest word in string is: ", max(words, key=len))
print("Largest word in string is: ", min(words, key=len))

#9) to check is functions
a  = "Admin"
print(a.isalpha()) # True

b = "Admin123"
print(a.isalpha()) # True

c = "1234"
print(a.isdigit()) #False
print(a.isnumeric()) #False