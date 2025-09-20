# #1. Find first repeated character in a string using set.
# def first_r_char(s):
#     seen = set()
#     for i in s:
#         if i in seen:
#             return i
#         seen.add(i)
#     return None

# a = 'abcaabcdba'
# print(first_r_char(a))

# #2. Count frequency of words in a sentence (use set for unique words).
# def freq(s):
#     words = s.split()
#     unique = set(words)
#     freq = {}

#     for i in unique:
#         freq[i] = words.count(i)
#     return freq

# sentence = "this is a test this is only a test"
# print("Word Frequency:", freq(sentence))

# #3. Given two lists, find elements that appear in both (intersection).
# def intersection(lst1, lst2):
#     set1 = set(lst1)
#     set2 = set(lst2)
#     return list(set1.intersection(set2))

# l1 = [1, 2, 3, 4, 5]
# l2 = [3, 5, 6, 7, 4]
# print("Common Elements:", intersection(l1, l2))

# #4. Find missing numbers from range using set difference.
# #Example: nums = {1,2,4,5}, full = {1,2,3,4,5} → missing {3}
# def missing(s1, s2):
#     set1 = set(s1)
#     set2 = set(s2)
#     return set1.symmetric_difference(set2)

# nums = {1,2,4,5}
# full = {1,2,3,4,5}
# print("Missing Numbers:", missing(nums, full))

# #5. Remove all elements of one set from another.
# def elements(s1, s2):
#     return s1 - s2

# s1 = {1, 2, 3, 4, 5}
# s2 = {2, 3, 4,}

# diff = elements(s1, s2)
# print("After removing:", diff)
        

# #6. Given a list of email IDs, find unique domains.
# def unique_domains(emails):
#     domains = set()
#     for i in emails:
#         domain = i.split('@')[1]
#         domains.add(domain)
#     return domains

# email_list = [
#     "alice@gmail.com",
#     "bob@yahoo.com",
#     "charlie@gmail.com",
#     "david@outlook.com",
#     "eve@yahoo.com"
# ]
# print("Unique Domains:", unique_domains(email_list))

# #7. Find all subsets (powerset) of a given set.
# def powerset(s):
#     result = [[]]
#     for i in s:
#         result += [curr + [i] for curr in result]
#     return result

# s = {1, 2, 3}
# print("Powerset:", powerset(s))

# #8. Write function to check if two strings are anagrams (use set).
# def are_anagrams(s1, s2):
#     return set(s1) == set(s2) and len(s1) == len(s2)

# print("Anagrams:", are_anagrams('listen', 'silent'))

# #9. Find longest word in a sentence without repeating characters.

# def long_word(sentence):
#     words = sentence.split()
#     longest = ""

#     for word in words:
#         if len(set(word)) == len(word):
#             if len(word) > len(longest):
#                 longest = word
#     return longest if longest else None

# a = "The quick brown fox jumps over the lazy dog"
# print("longest word :", long_word(a))

# #10. Implement a "unique visitor tracker" using set.
# class unique_visitor:
#     def __init__(self):
#         self.visitors = set()
    
#     def add_visitor(self, visitor_id):
#         self.visitors.add(visitor_id)
    
#     def total_visitors(self):
#         return len(self.visitors)
    
#     def show_visitor(self,):
#         return self.visitors

# tracker = unique_visitor()

# tracker.add_visitor("user1")
# tracker.add_visitor("user2")
# tracker.add_visitor("user3")
# tracker.add_visitor("user4")

# print("Total Unique Visitor:", tracker.total_visitors())
# print("Visitor IDs:", tracker.show_visitor())
