#1. Write a program to remove duplicates from a tuple.
a = (1, 2, 3, 2, 4, 1, 5, 3)
b = tuple(set(a))

print(b)

#OR

c = ()
for i in a:
    if i not in c:
        c += (i,)
print(c)

#2. Write a program to convert a list of tuples into a dictionary.
# Example: [("a",1),("b",2)] → {"a":1,"b":2}
l_tuple = [('a', 1), ('b', 2), ('c', 3)]
d = dict(l_tuple)
print(d)

#3. Given a tuple (name, age, score), sort by age or score.
a = [
    ("Alice", 22, 85),
    ("Bob", 20, 90),
    ("Charlie", 23, 80),
    ("David", 21, 95)
]

age = sorted(a, lambda x : x[1])
print(age)

#4. Find element(s) with highest frequency in a tuple.
a = (1, 2, 3, 2, 4, 1, 5, 3, 2, 1, 1)
freq = {}

for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

#5. Find pairs in tuple whose sum = given number.
def find_pairs(tup, target):
    seen = set()
    pairs = []
    
    for i in tup:
        diff = target - i
        if diff in seen:
            pairs.append((diff, i))
        seen.add(i)
    return pairs  

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
n = int(input("enter a number : "))
print("Pairs :", find_pairs(a, n))

#6. Check if tuple is palindrome.
a = (1, 2, 3, 2, 1)

if a == a[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

#7. Write program to count vowels in a tuple of characters.
a = ('a', 'b', 'e', 'i', 'o', 'u', 'c', 'd', 'A', 'E')

vowels = 'aeiouAEIOU'

count = 0

for i in a:
    if i in vowels:
        count += 1

print("Number of Vowels :", count)

#8. Convert string → tuple of characters.
s = "hello"

t = tuple(s)
print(t)

#9 Write function that returns n-th largest element in a tuple.
def nth_largest(tup, n):
    sorted_lit = sorted(tup, reverse=True)

    if n < 0 or n > len(tup):
        return "Invalid n"
    
    return sorted_lit[n-1]

a = (5, 10, 3, 8, 20, 15)
n = int(input("Enter n: "))
print(f"{n}-th largest element is:", nth_largest(a, n))

#10. Write function that returns all possible pairs from a tuple..'
def pairs(tup):
    pairs = []

    for i in range(len(tup)):
        for j in range(i+1, len(tup)):
            pairs.append((tup[i], tup[j]))
    
    return pairs
a = (1, 2, 3, 4)
print(pairs(a))
