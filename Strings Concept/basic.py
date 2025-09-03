# #1. Reverse a string without slicing.

# n = input("Enter a string to reverse : ")

# for i in range(len(n)-1, -1, -1):
#     print(n[i], end="")
# print()

# #2. Reverse a string with slicing method
# n = input("Enter a string to reverse : ")

# print(n[::-1])

# #3. Check if string is palindrome.
# def palindrome(n):
#     reverse = ""
#     for i in range(len(n)-1, -1, -1):
#         reverse = reverse + n[i]
#     return reverse

# n = input("Enter a string to reverse : ")

# if n == palindrome(n):
#     print("String is palindrome")
# else:
#     print("string is not palindrome")

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