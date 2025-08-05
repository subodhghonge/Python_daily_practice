#1) to print the pattern using for loop
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

for i in range(1,6):
    for j in range(1,6):
        if i==1 or i == 5 or j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# #2) to print the pattern using for loop
# #1
# #23
# #456
# #78910

num = 1
for i in range(1, 5):
    for j in range(1, i+1):
        print(num, end=" ")
        num+=1
    print()

#3) to print the pattern using for loop
# 1 
# 1 0 
# 1 0 1 
# 1 0 1 0
# 1 0 1 0 1

for i in range(1,6):
    for j in range(1, i+1):
        if j%2==0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()

#4) to print the pattern using for loop
# 1 
# 0 0 
# 1 1 1 
# 0 0 0 0
# 1 1 1 1 1
for i in range(1,6):
    for j in range(1, i+1):
        if i%2==0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()