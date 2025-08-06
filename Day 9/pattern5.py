#1) to print the pattern using for loop
#         *
#       * *
#     * * *
#   * * * *
# * * * * * 

for i in range(1, 6):
    for j in range(5-i):
        print(" ", end=" ")
    
    for k in range(i):
        print("*",end=" ")
    print()

#2) to print the pattern using for loop
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# **      **
# ***    ***
# ****  ****
# **********

#Upper Pattern
for i in range(5,0,-1):
    print("*"*i+ " "*(2*(5-i))+ "*"*i)

#lower pattern
for i in range(1,6):
    print("*"*i+ " "*(2*(5-i))+ "*"*i)

#3) to print the pattern using for loop
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

#upper pattern
for i in range(1,6):
    print("*"*i+ " "*(2*(5-i))+ "*"*i)

#lower Pattern
for i in range(4,0,-1):
    print("*"*i+ " "*(2*(5-i))+ "*"*i)