#1. Create a set of numbers from user input.
a = input("Enter numbers separated by spaces: ")
s = set()

for i in a.split():
    s.add(int(i))
print('set of numbers:', s)

#2. Add elements into a set.
a = {1, 2, 3, 4, 5}
n = int(input("Enter a number to add to the set: "))

a.add(n)
print(a)

#3. Remove an element safely (without error).
a = {1, 2, 3, 4, 5}
a.discard(3)
print(a)
#4. Convert list → set (remove duplicates).
lst = [1, 2, 2, 3, 4, 4, 5]

b = set(lst)

print(b)

#5. Convert string → set of unique characters.
s = 'hello world'

u_c = set(s)
print(u_c)

#6. Find length of a set.
c = {'l', 'r', 'o', 'w', ' ', 'd', 'h', 'e'}

print(len(c))

#or

count = 0
for i in c:
    count += 1
print(count)

#7. Pop a random element.
c = {'l', 'r', 'o', 'w', ' ', 'd', 'h', 'e'}
print(c.pop())

#8. Clear all elements.
c = {'l', 'r', 'o', 'w', ' ', 'd', 'h', 'e'}
print(c.clear())

#9. Check membership (x in set).
c = {'l', 'r', 'o', 'w', ' ', 'd', 'h', 'e'}
print('h' in c)
print('a' in c)

#10. Create a frozen set.
a = frozenset([1, 2, 3, 4, 5])
print(a)