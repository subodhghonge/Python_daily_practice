#1 To display square of 1 to 10 numbers

for i in range(1,11):
    print(f"Square of {i} is: ", i**2)

#2 To display cube of 1 to 10 numbers
for i in range(1, 11):
    print(f"Cube of {i} is: ", i**3)

#3 to display square of even no and cube of odd numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(f"Square of {i} : ", i**2)
    else:
        print(f"Square of {i} : ", i**3)