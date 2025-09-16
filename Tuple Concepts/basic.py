#1. Create a tuple with integers, strings, and mixed types.
a = (1, "John", "Washington", 65.40)

#2. Find length of tuple without using len().
b = ('apple', 'banana','cherry','dragonfruit','banana', 'mango','watermelon')

print(len(a))

#3. Check if an element exists in tuple.

tuplee = (1, "John", "Washington", 65.40)

element = input("Enter the element to search:")

if element in tuplee:
    print("Element present")
else:
    print("Not present")

#4. Convert tuple → list and list → tuple.
x = ('apple', 'banana','cherry','dragonfruit','banana', 'mango','watermelon')
y = list(x)

print(f"List {y}")

x = tuple(y)
print(f"Tuple{x}")

#5. Slice a tuple (first 3, last 3, alternate elements).
t = ('apple', 'banana','cherry','dragonfruit','banana', 'mango','watermelon')

print(t[0:3])
print(t[5:])
print(t[0: :2])
print(t[1: :2])

#6. Reverse a tuple.
t = ('apple', 'banana','cherry','dragonfruit','banana', 'mango','watermelon')

print("Reverse :", t[::-1])

#7. Count frequency of an element in tuple.
t = ('apple', 'banana','cherry','dragonfruit','banana', 'mango','watermelon')
freq = {}

for i in t:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    
print(freq)

#8. Find index of an element in tuple.
t = ('apple', 'banana','cherry','dragonfruit','banana', 'mango','watermelon')

element = input("Enter the element to get index: ")

print(f"Index of {element} is {t.index(element)}")

#9. Concatenate two tuples.
t1 = "apple", "banana", "cherry"
t2 = "mmango", "watermelon", "orange"

t_tuple = t1 + t2
print(t_tuple)

#10. Repeat a tuple 5 times.
t1 = "apple", "banana", "cherry"

print(t1*5)