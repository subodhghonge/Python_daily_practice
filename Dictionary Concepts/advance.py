#1. Write a program to group anagrams using dictionary.
# Example: ["bat","tab","cat"] → {"abt":["bat","tab"],"act":["cat"]}

def grp_anagrams(words):
    anagrams = {}
    
    for i in words:
        sorted_w = "".join(sorted(i))
        if sorted_w in anagrams:
            anagrams[sorted_w].append(i)
        else:
            anagrams[sorted_w] = [i]
    
    return anagrams

l = ["bat","tab","cat"]
print("Anagram: ",grp_anagrams(l))

#2. Write a program to find the most frequent element in a list using dictionary.
def most_freq(lst):
    freq = {}

    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return max(freq, key=freq.get)

lst = [1,2,3,4,5,1,2,1,1,1,3,4,5,1]
print("Most frequent: ", most_freq(lst))

#3. Implement a dictionary without using built-in dict (simulate with list of tuples).

#4. Convert a list of tuples to dictionary.
# Example: [("a",1),("b",2)] → {"a":1,"b":2}

#5. Write program to count frequency of vowels in a string using dictionary.

#6. Check if two strings are isomorphic (mapping chars with dict).

#7. Build histogram of numbers using dictionary.

#8. Write program to check if dictionary is subset of another.

#9. Find common key-value pairs in two dictionaries.

#10. Write program to flatten nested dictionary.