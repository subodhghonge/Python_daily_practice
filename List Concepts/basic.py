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

#5. Count occurrences of a given element in a list.

#6. Reverse a list without using reverse() or slicing.

#7. Copy one list into another list without using copy().

#8. Remove all occurrences of an element from a list.

#9. Find second largest element in a list.

#10. Check if a list is palindrome.