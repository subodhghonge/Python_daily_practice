#1. Remove duplicates from a string (programming → progamin).
n = input("Enter a String: ")
result = ""
for i in n:
    if i not in result:
        result = result + i
print(result)