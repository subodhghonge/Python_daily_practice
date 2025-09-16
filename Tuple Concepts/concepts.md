# Tuple - Tuple is comma separated values within parathesis
        - Ordered, immutable, duplicates are allowed, allow multiple datatypes in on tuple
        - Faster the list
        - len() used to check the number of items in TUPLE

# Accessing items of List - using indexing and slicing
    1. Indexing 
        I. Forward Indexing / Positive Indexing
            start from 0 and end with len-1
        II. Backward Indexing / Negative Indexing
            start from -1 and end with -n 
    
    2. Slicing - to get range of items from a TUPLE
        
        example :-  a = ("apple", "banana", "cherry", "mango", "watermelon")
                    a[0]            #['apple']
                    a[-1]           #['watermelon']
                    a[1:4]          #['banana', 'cherry', 'mango']
                    a[-1:-3:-1]     #['watermelon'] 
                    a[-5:-1]        #['apple', 'banana', 'cherry', 'mango']

# Create tuple with one element.
    - To create tuple with one element we need to write 'comma(,)' infront of element, otherwise it will not be considered as a tuple.
        eg :- t_tuple = ("hello",)

# Add Elements in Tuple
    - Tuple is immutable but we can convert tuple to list then add values and again convert it into tuple.
    Method 1 :- Convert to LIST
            x = ("apple", "banana", "cherry")
            y = list(x)
            y.append("Orange")
            x = tuple(y)
    Method 2 :- x = ("apple", "banana", "cherry")
            y = ("Orange",)
            x = x + y

# Update Element in Tuple
    - Tuple is immutable but we can convert tuple to list then update and again convert it into tuple.
            x = ("apple", "banana", "cherry")
            y = list(x)
            y[0] = 'orange'
            x = tuple(y)

# Remove Elements from Tuple
    - Tuple is immutable but we can convert tuple to list then remove element and again convert it into tuple.
            x = ("apple", "banana", "cherry")
            y = list(x)
            y.remove("orange")
            x = tuple(y)

# Size of Tuple in bytes
    - import getsizeof() - returns size of list, tuple, sets, dictionary etc.
    - based on size we can know the execution speed.
            1. tuples requires less memory and is fast in execution because of immutable
            2. list requires more memory then tuple
            3. dictionary requires more memory than list
            4. set requires more memory then dictionary

# Supports Packing and Unpacking                          # interview point of view
    1. Packing - Wrapping of multiple values into a single variable
        eg :- x, y, z = 10, 20, 3
              t = x, y, z
              print(t)

    2. Unpacking - Taking values out of collection and assiging to different variables.
        # Tuple - supports packing and unpacking
        # list - supports only unpacking
        # set - packing and unpacking not allowed

6. Tuple is Hasble beacuse it is immutable(can be used as key in dicitonary)
    list and set are not hashable but they can be used as values in dictionary

# For loop 
    x = ("apple", "banana", "cherry")

    for i in x:
        print(i)
    
    for i in range(len(a)):
        print(a[i])

# Multiple Tuples
    x = ("apple", "banana", "cherry")
    y = x * 2

# Common Methods
1. count() → count occurrences of a value.
2. index() → returns index of first occurrence.