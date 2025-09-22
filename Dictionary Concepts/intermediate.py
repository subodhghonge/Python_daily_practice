#1. Count frequency of each character in a string.
str = "hello world!. welcome to python programming"
freq = {}

for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

#2. Count frequency of each word in a sentence.
str = "hello world!. welcome to python programming"

words = str.split()

freq = {}

for i in words:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

#3. Find key with maximum value.
dict = {'a':10, 'b':20, 'c':30, 'd':40}

for key in dict:
    if dict[key] == max(dict.values()):
        print('max value key: ', key)

#4. Sort dictionary by keys.
dic = {'a':10, 'd':40, 'c':30, 'b':20}

d_sorted = dict(sorted(dic.items()))
print(d_sorted)

#5. Sort dictionary by values.
dic = {'a':40, 'd':10, 'c':20, 'b':30}

d_sorted = dict(sorted(dic.items()), key = lambda item: item[1])
print(d_sorted)

#6. Merge two dictionaries.
a = {'a':10, 'b':20}
b = {'c':30, 'd':40}

a.update(b)
print(a)

#7. Convert 2 lists → dictionary (zip).
key = ['a', 'b', 'c', 'd']
value = [10, 20, 30, 40]

res = dict(zip(key, value))
print(res)

#8. Invert dictionary (swap keys and values).
dic = {'a':40, 'd':10, 'c':20, 'b':30}
inv_dic = {}

for key, value in dic.items():
    inv_dic[value] = key

print(inv_dic)

#9. Nested dictionary access (student records).
students = {
    'student1': {
        'name': 'Alice', 'age': 18, 'grades': {'math': 95, 'science': 90, 'english': 88}
        },
    'student2': {
        'name': 'Bob','age': 19,'grades': {'math': 80,'science': 85,'english': 92}
        }
}

print(students['student1']['grades']['math'])
print(students['student2']['name'])

#10. Check if two dictionaries are equal.
a = {'a':10, 'b':20}
b = {'c':30, 'd':40}

if a == b:
    print("equal")
else:
    print("not equal")