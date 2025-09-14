# #1. Find sublists of a list (all combinations).
# def all_sublist(lst):
#     sublist = []

#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)+1):
#             sublist.append(lst[i:j])
    
#     return sublist

# n = list(map(int, input("Enter number with comma separated : ").split(',')))
# print(all_sublist(n))

# #2. Find longest increasing subsequence in a list.
# def sequence(lst):
#     n = len(lst)
#     dp = [1] * n

#     for i in range(1, n):
#         for j in range(i):
#             if lst[i] > lst[j]:
#                 dp[i] = max(dp[i], dp[j]+1)
    
#     return max(dp)

# l = [10, 22, 9, 33, 21, 50, 41, 60]
# print("Length of LIS:", sequence(l))

# #3. Find the majority element (appears > n/2 times).
# def majority(nums):
#     freq = {}
#     n = len(nums)

#     for i in nums:
#         freq[i] = freq.get(i, 0) + 1
#         if freq[i] > n // 2:
#             return i
#     return None

# num = [3, 3, 4, 2, 3, 3, 3]
# print("Majority Element:", majority(num))
    

#4. Rotate list in-place using reversal algorithm.n
def reverse(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

def rotate_right(lst, k):
    n = len(lst)
    k %= n

    reverse(lst, 0, n-1)

    reverse(lst, 0, k-1)

    reverse(lst, k, n-1)

nums = [1, 2, 3, 4, 5, 6, 7]
rotate_right(nums, 3)
print("Rotated List:", nums)

#5. Find missing number from a list of 1…n.

#6. Find duplicates in a list without using extra space.

#7. Find maximum product subarray.

#8. Kadane’s Algorithm → Maximum subarray sum.

#9.  Find all triplets in a list with sum = 0.

#10. Spiral traversal of a 2D list (matrix).