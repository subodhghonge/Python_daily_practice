#1. Create a list and access elements using indexing & slicing.
list = [1, "John", 20, "Washington", +15555661234]

print(list[0])          #1
print(list[-1])         #15555661234
print(list[0:5])        #[1, 'John', 20, 'Washington', 15555661234]
print(list[-1:-5:-1])   #[15555661234, 'Washington', 20, 'John']
print(list[-5:-1:1])    #[1, 'John', 20, 'Washington']

#2. Find the length of a list without using len().
fruits = ['apple', 'banana', 'cherry', 'dragon fruit', 'mango', 'pamogrante']
length = 0

for i in fruits:
    length += 1
    print(f'{length}.{i}')
print(length)

#3. Find the sum of elements in a list.

marks = [50, 89, 45, 63, 60, 75]

sum_m = sum(marks)
print(sum_m)

#OR
sum = 0
for i in marks:
    sum += i
print(sum)

#4. Find maximum and minimum elements in a list.
score = [50, 89, 45, 63, 60, 75, 10, 100]

print(max(score))
print(min(score))

#OR

maximum = score[0]
minimum = score[0]

for i in score:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Maximum Value is : ", maximum)
print("Minimum Value is :",minimum)

#5. Count occurrences of a given element in a list.
list = [10, 30, 20, 50, 20, 90, 45, 50, 45, 100, 48, 26, 28, 26, 'apple', 'apple']
freq = {}

for i in list:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

#6. Reverse a list without using reverse() or slicing.
list1 = ['apple', 'banana', 'cherry', 'dragon fruit', 'mango', 'pamogrante']

list2 = []

for i in range(len(list1)-1, -1,-1):
    list2.append(list1[i])
print(list1)
print(list2)

#7. Copy one list into another list without using copy().
list1 = ['apple', 'banana', 'cherry', 'dragon fruit', 'mango', 'pamogrante']

list2 = []

for i in list1:
    list2.append(i)
print(list2)

#8. Remove all occurrences of an element from a list.
lst_d = [1, 2, 3, 2, 4, 5, 3, 6, 2, 7, 3, 8, 2, 9, 3]

lst = []

for i in lst_d:
    if i not in lst:
        lst.append(i)
print(lst)

#9. Find second largest element in a list.
numbers = [12, 45, 23, 67, 34, 89, 67, 89, 23, 45]

s = sorted(numbers)
print(s)

print(f"Second largest number {s[-2]}")
    

#10. Check if a list is palindrome.
palindrome_list = [1, 2, 3, 2, 1]

if palindrome_list == palindrome_list[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
