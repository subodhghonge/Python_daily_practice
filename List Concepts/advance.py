#1. Find sublists of a list (all combinations).
def all_sublist(lst):
    sublist = []

    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublist.append(lst[i:j])
    
    return sublist

n = list(map(int, input("Enter number with comma separated : ").split(',')))
print(all_sublist(n))

#2. Find longest increasing subsequence in a list.

#3. Find the majority element (appears > n/2 times).

#4. Rotate list in-place using reversal algorithm.

#5. Find missing number from a list of 1…n.

#6. Find duplicates in a list without using extra space.

#7. Find maximum product subarray.

#8. Kadane’s Algorithm → Maximum subarray sum.

#9.  Find all triplets in a list with sum = 0.

#10. Spiral traversal of a 2D list (matrix).