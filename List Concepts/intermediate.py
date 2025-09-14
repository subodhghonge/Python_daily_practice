#1. Remove duplicates from a list (preserve order).
def remove_dup(lst):
    l = []

    for i in lst:
        if i not in l:
            l.append(i)
    return l

my_list = [1, 2, 2, 3, 4, 3, 5]
print(remove_dup(my_list))

#2. Merge two sorted lists into one sorted list.
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

s_list = sorted(list1 + list2)
print(s_list)

#3. Rotate a list by n positions (left & right).
def left_shift(lst, n):
    n = n % len(lst)

    return lst[n:] + lst[:n]

def right_shift(lst, n):
    n = n % len(lst)

    return lst[-n:] + lst[:-n]

l = list(map(int, input('Enter number separated by comma : ').split(',')))
shifts = int(input("How many shift you want to perform : "))

while True:
    print("""
    1. shift Left Side
    2. Shift Right Side
    3. Exit""")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        print(left_shift(l, shifts))
    elif ch == 2:
        print(right_shift(l, shifts))
    elif ch == 3:
        print("Exiting program...")
        break
    else:
        print("Enter a valid choice")

#4 Find intersection of two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = []

for i in list1:
    if i in list2:
        intersection.append(i)

print(intersection)

#50 Find union of two lists (without using set).
def union(lst1, lst2):
    result = []

    for i in lst1 + lst2:
        if i not in result:
            result.append(i)
    return result

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print()

# 6. Flatten a nested list ([[1,2],[3,4]] → [1,2,3,4]).
lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]

r = []

for i in lis:
    r.extend(i)

print(r)

#7. Split a list into even and odd numbers.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []

for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even Numbers list : ",even)
print("Odd Numbers list : ",odd)

#8. Find common elements in three lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [0, 2, 3, 4, 5, 8]

common = []
for i in list1:
    if i in list2 and i in list3:
        common.append(i)

print("Common elements in all three lists:", common)

#9. Print all pairs in a list whose sum = given number.
def find_pairs(lst, target):
        seen = set()
        pairs = []

        for i in lst:
                diff = target - i
                if diff in seen:
                        pairs.append((diff, i))
                seen.add(i)
        return pairs

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("enter a number : "))

print("Pairs :", find_pairs(lst, n))

#10. Separate positive and negative numbers from a list.
numbers = [12, -7, 5, -3, 9, -2, 0, 8, -1]
p = []
n = []

for i in numbers:
        if i >= 0:
                p.append(i)
        else:
                n.append(i)
print(f"Positive numbers : {sorted(p)}")
print(f"Negative numbers : {sorted(n)}")