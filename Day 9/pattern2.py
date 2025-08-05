#1) to print the pattern using for loop
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

#5) to print the pattern using for loop
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=' ')
    print()

#6) to print the pattern using for loop
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()