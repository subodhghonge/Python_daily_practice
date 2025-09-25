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
class MyDict:
    def __init__(self):
        self.data = []
    
    def set(self, key, value):
        for i, (k,v) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))
    
    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return None
    
    def __repr__(self):
        return str({k:v for k, v in self.data})

d = MyDict()
d.set("a", 1)
d.set("b", 2)
d.set("a", 3)  # update
print("Custom Dictionary:", d)
print("Get 'b':", d.get("b"))


#4. Convert a list of tuples to dictionary.
# Example: [("a",1),("b",2)] → {"a":1,"b":2}
def tuple_dict(lst):
    return dict(lst)

pairs = [("a", 1), ("b", 2), ("c", 3)]
print("Dictionary: ", tuple_dict(pairs))

#5. Write program to count frequency of vowels in a string using dictionary.
def v_freq(s):
    vowels = 'aeiouAEIOU'
    freq = {}

    for i in s:
        if i in vowels:
            freq[i] = freq.get(i,0)+1
    
    return freq

sentence = "Programming in Python is awesome"
print("Vowel Frequency:", v_freq(sentence))

#6. Check if two strings are isomorphic (mapping chars with dict).
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for ch1, ch2 in zip(s, t):
        if ch1 in s_to_t:
            if s_to_t[ch1] != ch2:
                return False
        else:
            s_to_t[ch1] = ch2
    
        if ch2 in t_to_s:
            if t_to_s[ch2] != ch1:
                return False
        else:
            t_to_s[ch2] = ch1
    
    return True

print(is_isomorphic("egg", "add"))   
print(is_isomorphic("foo", "bar"))   
print(is_isomorphic("paper", "title")) 
print(is_isomorphic("ab", "aa"))     


#7. Build histogram of numbers using dictionary.
def build_histogram(numbers):
    histogram = {}
    
    for num in numbers:
        if num in histogram:
            histogram[num] += 1
        else:
            histogram[num] = 1
    
    return histogram


# 🔹 Test
nums = [1, 2, 2, 3, 3, 3, 4, 2, 1, 5, 5, 5, 5]
print("Histogram:", build_histogram(nums))

#8. Write program to check if dictionary is subset of another.

#9. Find common key-value pairs in two dictionaries.

#10. Write program to flatten nested dictionary.