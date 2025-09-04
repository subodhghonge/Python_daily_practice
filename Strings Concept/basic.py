#1. Reverse a string without slicing.

n = input("Enter a string to reverse : ")

for i in range(len(n)-1, -1, -1):
    print(n[i], end="")
print()

#2. Reverse a string with slicing method
n = input("Enter a string to reverse : ")

print(n[::-1])

#3. Check if string is palindrome.
def palindrome(n):
    reverse = ""
    for i in range(len(n)-1, -1, -1):
        reverse = reverse + n[i]
    return reverse

n = input("Enter a string to reverse : ")

if n == palindrome(n):
    print("String is palindrome")
else:
    print("string is not palindrome")

#4. Count vowels, consonants, digits, special chars.
def count_char(s):
    vowels = 'aeiou'

    v_c = c_c = d_c = s_c = 0

    for i in n:
        if i.isalpha():
            if i in vowels:
                v_c += 1
            else:
                c_c += 1
        elif i.isdigit():
            d_c += 1
        else:
            s_c += 1
    
    return v_c, c_c, d_c, s_c

n = input("Enter your email Id :- ")

v, c, d, s = count_char(n)

print("vowels count is : ", v)
print("vowels count is : ", c)
print("vowels count is : ", d)
print("vowels count is : ", s)

#5.Convert string to uppercase/lowercase without using built-in.
def to_uppercase(s):
    result = ""
    for ch in s:
        if 'a' <= ch <='z':
            result = result + chr(ord(ch)-32)
        else:
            result += ch
    return result

def to_lowercase(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            result = result + chr(ord(ch)+32)
        else:
            result += ch
    return result

n = input("Enter a string : ")

print("Uppercase : ", to_uppercase(n))
print("Lowercase : ", to_lowercase(n))

#6. Remove whitespaces from a string.
def whitespace(s):
    result = ""

    for i in s:
        if i != " ":
            result += i
    return result

n = input("Enter a string : ")
print(whitespace(n))
        #OR
n = input("Enter a string : ")
print('Whitespace removed string : ', "".join(n.split()))

#7. Find length of a string without using len().
i = input('Enter a string: ')
count = 0
for ch in i:
    count += 1

print("length of a string is : ", count)

#8. Count occurrences of each character (frequency count).
n = input('Enter a string: ')
freq = {}

for i in n:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

#9.Find ASCII value of each character.
n = input('Enter a string: ')

print(f'The ASCII value of {n} is {ord(n)}')

#10. Find number of words in a string.
n = input('Enter a string: ')
count = 0

a = n.split()

print(len(a))

#11. Swap case of a string (PyThOn → pYtHoN).
n = input('Enter a string: ')

print("Swapcase of a string is ", n.swapcase())