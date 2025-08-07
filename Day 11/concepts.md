#Agenda
#String Data types
#Indexing
#Slicing

#I. String - String is a primitive datatype. string is a collection of characters within a ' '," " or ''' '''

#1 syntax
# varname = "value"

name = "Subodh"

#2 multiline string
name = """ Python is a dynaminc language 
python is a simple language """

print(name)
print(type(name)) #print type of datatype

#3 Indexing - to get a single character from a string
#There are two types of indexing
# a. forward / positive indexing
    start from left to right
    start index = 0 and end index = len - 1
# b. backward / negative indexing
    start from right to left
    start index = -1 and end index = -n

example
a = "python"

p   y  t  h  o  n
0   1  2  3  4  5
-6 -5 -4 -3 -2 -1

#4 Slicing - to get multiple characters
    # syntax -
            var_name[start_index : stop_index : step_index]
                    start_index = included
                    stop_index = excluded
                    step = increament/decreament