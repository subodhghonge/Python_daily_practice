# Sets :- Comma separated values enclosed with in curly({}) brackets.
        - unordered, mutable(add/remove), duplicates not allowed, any data typle allowed in one set except list and dict.
        - len() used to determine the items count in set.
        - heterogenous collection of immutable elements where insertion order of immutable elements is allowed
        - Useful for membership testing, duplicate removal, mathematical operations.

# Accessing elements in sets
1. Membership operator
    eg:- a = {'apple', 'mango', 'banana', 'cherry'}
        print('apple' in a)

2. for loop
    eg :- a = {'apple', 'mango', 'banana', 'cherry'}
          for i in a:
            print(i)

# Add elements in set
    1. add() - insert element in set
       eg:- a.add("value")
    
    2. update() - to add multiple values in set / merge two set in one set.
       eg:- a.update(var_name)

# Updation not possible in sets

# Removing element in set
    1. remove() - if element not present in set to delete then throws error.
        eg :- a.remove("value")
    2. discard() - if element not present in set to delete thne do not throw error.
        eg :- a.discard("value")
    3. pop() - remove element randomly from set.
        eg :- a.pop()
    4. clear() - empty set
        eg :- a.clear()
    5. del - delete the set completely
        eg :- del a

# Create a empty set
    1. set() - empty set.

# Set Operations methods
    1. union() - merge two sets all element, duplicate element wil be printed only once.
        eg :- var1.union(var2)
    2. intersection() - common elements will be displayed from two sets.
        eg :- var1.intersection(var2)
    3. difference() - returns element that are in var1 and not in var2.
        eg :- var1.difference(var2)
    4. difference_update()
    5. symmetric_difference - it will return a new set of elements that are in either of the sets but not in both.
    6. symmetric_differenct_update()
    7. issubset() - check subset
    8. issuperset() - check superset
    9. disjoint() - True if no element is common
