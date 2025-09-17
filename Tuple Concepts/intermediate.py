#1. Create nested tuple and access inner elements.
a = ((1, 2, 3), ('a', 'b'), (True, False, None))
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])
print(a[2][2])

#2. Find max & min in a tuple of numbers.
a = (10, 20, 5, 30, 15)

maximum = a[0]
minimum = a[0]

for i in a:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print(f"maximum{maximum}")
print(f"minimum{minimum}")

#3. Sort tuple elements (ascending/descending).
a = (10, 2, 30, 5, 15)
sort = sorted(a)
d_sort = sorted(a, reverse=True)
print(sort)
print(d_sort)

#4. Merge two sorted tuples into one sorted tuple.
a = (10, 2, 30, 5, 15)
b = (25, 12, 7, 18, 3)

merged = a + b
sort_m = sorted(merged)
print(sort_m)

#5. Convert tuple of tuples → single flat tuple.
a = ((1, 2, 3), ('a', 'b'), (True, False, None))

b = ()

for i in a:
    for j in i:
        b += (j,)

print(b)

#6. Swap two tuples without using temp variable.
a = (1, 2, 3)
b = ('a', 'b', 'c')

a, b= b, a
print(f"a : {a}")
print(f"b : {b}")

#7. Find common elements between two tuples.
a = (1, 2, 3, 4, 5)
b = (4, 5, 6, 7, 8)

l = []
for i in a:
    if i in b:
        l.append(i)
print(l)

#8. Create a tuple from user input (split by space).

n = input("Enter elemenets separated by space: ")

t = tuple(n.split())
print(t)
#9. Write program to check if two tuples are identical.

a = (1, 2, 3)
b = (1, 2, 3)

for i in a:
    if i in b:
        print("Identical")
    else:
        print("Not Identical")

#10. Write program to delete a tuple (using del).
a = (1, 2, 3)
del a
print(a)