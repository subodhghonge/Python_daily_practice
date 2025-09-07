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