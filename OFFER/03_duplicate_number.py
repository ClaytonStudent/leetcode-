# 题目：找出数组中的重复数字
# 时间复杂度 O(nlogn)
def duplicate_number(nums):
    if len(nums) <= 1:
        return -1
    nums.sort()  # sort need O(nlogn)
    for i in range(len(nums)-2):    # O(n)
        if nums[i] == nums[i+1]:
            return nums[i]

# 时间复杂度 O(n) , 空间复杂度 O(n) ， 因为需要有字典来存储所有的元素
def duplicate_number_dict(nums):
    if len(nums) <= 1:
        return -1
    h1 = {}
    for i in nums:
        h1[i] = h1[i] +1 if h1.get(i) else 1
    for i in h1.keys():
        if h1[i] > 1:
            return i
    return -1

# 尽管双重循环，每个数字最多交换两次就能找到它的位置。
# 时间复杂度是 O(n), 空间复杂度是O(1)
def duplicate_number_dict_0(nums):
    if len(nums) <= 1:
        return False
    for i in range(len(nums)):
        while i != nums[i]:
            if nums[i] == nums[nums[i]]:
                return True
            temp = nums[i]
            nums[i] = nums[temp]
            nums[temp] = temp
    return False

# ----------------------------
# 要求：可以修改原数组，可以用上面的dict方法，空间复杂度为O(n)
# 时间复杂度O(nlogn), 空间复杂度为 O(1) 使用了二分查找的想法
def duplicate_number_no_change(nums):
    if len(nums)<= 0:
        return -1
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (end-start)//2 + start
        count = countrange(nums,start,mid)
        if start == end:
            if count > 1:
                return start
            else:
                break
        if count > (mid-start+1):
            end = mid
        else:
            start = mid+1
    return -1

def countrange(nums,start,end):
    if len(nums) <= 0:
        return 0
    count = 0
    for i in range(len(nums)):
        if nums[i]>=start and  nums[i] <= end:
            count+=1
    return count


nums = [2,3,1,0,2,5,3]
ans = duplicate_number(nums)
print(ans)
ans = duplicate_number_dict(nums)
print(ans)
nums = [2,3,1,0]
ans = duplicate_number_dict_0(nums)
print(ans)