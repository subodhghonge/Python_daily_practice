# #1. Remove duplicates from a string (programming → progamin).
# n = input("Enter a String: ")
# result = ""
# for i in n:
#     if i not in result:
#         result = result + i
# print(result)

# #2. First non-repeating character in a string
# n = input("Enter a String: ")
# freq = {}

# for ch in n:
#     freq[ch] = freq.get(ch, 0) + 1

# for ch in n:
#     if freq[ch] == 1:
#         print(ch)

# #3.Check if two strings are anagrams (listen, silent).
# a = input("Enter string1 : ")
# b = input("Enter string2 : ")

# if sorted(a.lower()) == sorted(b.lower()):
#     print("Anagram")
# else:
#     print("Not Anagram")

# #4. Find all substrings of a string.
# def sub_str(s):
#     substr = []
#     n = len(s)

#     for i in range(n):
#         for j in range(i+1, n+1):
#             substr.append(s[i:j])
    
#     return substr

# i = input("Enter a string: ")

# result = sub_str(i)

# print(result)

# #5. Find longest word in a sentence.
# def long_word(str):
#     word = str.split()
#     longest = ""

#     for i in word:
#         if len(i) > len(longest):
#             longest = i
    
#     return longest

# i = input("Enter a sentence: ")

# result = long_word(i)
# print(result)

# #6. Replace spaces with - (URL formatting).
# def spaces(s):
#     result = ""

#     for i in s:
#         if i == " ":
#             result += '-'
#         else:
#             result += i
    
#     return result

# i = input("Enter a string: ")

# r = spaces(i)

# print("String : ", r)

# #7. Check if a string has all unique characters
# # using set function
# def unqiue(s):
#     return len(s) == len(set(s))

# i = input("Enter a string : ")

# if unqiue(i):
#     print("All Character are unique")
# else:
#     print("All Characters are not unqiue")

# #8. Count frequency of each word in a sentence.
# def freq(s):
#     word = s.split()
#     freq = {}

#     for i in word:
#         i = i.lower()
#         freq[i] = freq.get(i, 0)+1
    
#     return freq

# i = input("Enter a string : ")
# d = {}
# result = freq(i)
# for word, count in result.items():
#     l = {word:count}
#     d.update(l)

# print(d)

# #9. Check if string is rotation of another (abcd, cdab).
# def is_rotation(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     return s2 in (s1+s1)  #Check the second string in first string 

# i = input("Enter first string : ")
# j = input("Enter second string : ")

# if is_rotation(i, j):
#     print("string 1 and string 2 are rotation of each other")
# else:
#     print("Strings are not rotation of each other")

#10. Check if two strings are equal without using ==.
def is_equal(s1, s2):
    if len(s1)!=len(s2):
        return False
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

i = input("Enter first string : ")
j = input("Enter second string : ")

if is_equal(i, j):
    print("Is equal")
else:
    print("Is not equal")