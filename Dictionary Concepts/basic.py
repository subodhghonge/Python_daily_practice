#1. Create a dictionary of student → marks.
student_marks = {'stud1' : 85, 'stud2' : 90, "stud3" : 70, 'stud4' : 50}

for i in student_marks.items():
    print(f"{i}")

#2. Access value by key.
print(student_marks['stud1'])
print(student_marks['stud2'])
print(student_marks['stud3'])
print(student_marks['stud4'])

#3. Add new key-value pair.
student_marks['stud5'] = 60
print(student_marks)

#4. Update value of an existing key.
student_marks['stud3'] = 75
print(student_marks)

#5. Delete a key-value pair.
student_marks.pop("stud5")
print(student_marks)

#6. Iterate through keys, values, and items.
for i in student_marks.keys():
    print(i)

for i in student_marks.values():
    print(i)

for key, value in student_marks.items():
    print(f"{key} : {value}")

#7. Check if a key exists in dict.
if 'stud1' in student_marks:
    print("Key exists")
else:
    print("Key does not exist")

#8. Create a dictionary using dict() constructor.
new_dict = dict(a=1, b=2, c=3)
print(new_dict)

#9. Create a dictionary using fromkeys().
keys = ['a', 'b', 'c']
values = 0
dict_from_keys = dict.fromkeys(keys, values)
print(dict_from_keys)

#10. Copy dictionary.
c_dict = student_marks.copy()
print(c_dict)