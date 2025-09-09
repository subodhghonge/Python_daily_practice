# #Compress a string (aaabbc → a3b2c1).
# def compress(s):
#     compressed = ""
#     count = 1

#     for i in range(len(s)):
#         if i+1 < len(s) and s[i] == s[i+1]:
#             count += 1
#         else:
#             compressed += s[i] + str(count)
#             count = 1

#     return compressed

# i = input("Enter a string : ") 

# print("Compressed string : ", compress(i))


# #2. Expand a compressed string (a3b2c1 → aaabbc).
# def expand_string(s):
#     expand = ""
#     i = 0

#     while i < len(s):
#         char = s[i]
#         i += 1
#         num = ""

#         while i < len(s) and s[i].isdigit():
#             num += s[i]
#             i += 1
        
#         expand += char * int(num)

#     return expand 

# i = input("Enter a compressed string: ")

# print("Expanded string:", expand_string(i))

#3.

