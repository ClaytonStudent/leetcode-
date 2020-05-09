# fibonacci
def fibonacci_recu(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci_recu(num-1) + fibonacci_recu(num-2)

def fibonacci_iter(num):
    a,b = 0,1
    for _ in range(num):
        a,b = b, a+b
    return a 

# Most Frequent
from collections import Counter 
def most_frequent(List): 
    occurence_count = Counter(List) 
    return list(occurence_count.most_common(1)[0])


def sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [i for i in nums[1:] if i<=pivot]
    right = [j for j in nums[1:] if j>pivot]
    return sort(left) + [pivot] + sort(right)
nums = [6,3,5,2,4,1]
#nums = [2,1]
nums = sort(nums)
print(nums)
