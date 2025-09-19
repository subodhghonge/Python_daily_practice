#1. Find union, intersection, difference, symmetric difference of two sets.
a = (1, 2, 3, 4, 5)
b = (4, 5, 6, 7, 8)

set_a = set(a)
set_b = set(b)

print(f"Union: {set_a.union(set_b)}") #1,2,3,4,5,6,7,8
print(f"Intersection: {set_a.intersection(set_b)}") # 4,5
print(f"Difference: {set_a.difference(set_b)}") #1,2,3
print(f"Difference: {set_b.difference(set_a)}") #6,7,8
print(f"Symmetric Difference: {set_a.symmetric_difference(set_b)}") #1,2,3,6,7,8

#2. Check if one set is subset/superset of another.
a = {4, 5}
b = {4, 5, 6, 7, 8}

print(f"subset: {a.issubset(b)}")
print(f"subset: {b.issuperset(a)}")

#3. Find common elements in three sets.
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"Common Elements : {a.intersection(b)}")

#4. Remove duplicates from a list using set.
lst = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8]

set_a = set(lst)

print(set_a)

#5. Write program to find unique vowels in a string.
s = "Hello, welcome to the world of Python programming"
vowels = 'aeiouAEIOU'
u_vowels = set()
for i in s:
    if i in vowels:
        u_vowels.add(i)
print(u_vowels)

#6. Write program to find elements present in set A but not in set B.
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.difference(b))

#7. Check if two sets are disjoint.
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))

#8. Find max & min in a numeric set.
a = {10, 5, 25, 15, 40, 35, 80, 45, 90}
print(max(a))
print(min(a))

#OR

def min_max(s):
    it = iter(s)

    first = next(it)

    minimum = maximum = first

    for i in s:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    
    return minimum, maximum

nums = {10, 25, 5, 40, 7, 90, 3}
mx, mn = min_max(nums)
print("Maximum:", mx)
print("Minimum:", mn)


#9. Find all prime numbers in a set.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n*0.5)+1):
        if n % 2 == 0:
            return False
    return True

def prime_in_set(s):
    prime = set()

    for i in s:
        if is_prime(i):
            prime.add(i)
    return prime

nums = {10, 3, 5, 8, 11, 15, 2, 19, 20}
print("Prime numbers in set:", prime_in_set(nums))

#10. Find duplicate elements in a list using set.
def duplicate(lst):
    seen = set()
    duplicate = set()

    for i in lst:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)
    return duplicate

numbers = [1, 2, 3, 4, 2, 5, 6, 1, 7, 3, 8, 9, 1]
print("Duplicate elements:", duplicate(numbers))
