#1) to print the pattern using for loop
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print("*", end=' ')
    print()

#2) to print the pattern using for loop
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i, end=' ')
    print()

#3) to print the pattern using for loop
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()