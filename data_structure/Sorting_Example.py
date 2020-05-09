# bubble
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


# selection
def selection_sort(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

# insertion 
def insertion_sort(nums): 
    for i in range(1,len(nums)):
        key = nums[i]
        j = i-1
        while j>=0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

# shell
def shell_sort(nums):
    gap = len(nums)//2
    while gap:
        for i in range(gap,len(nums)):
            tmp = nums[i]
            j = i
            while j >=gap and nums[j-gap] > tmp:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = tmp
        gap = gap//2
    return nums

# shell another version, similar to interpolation sort
def shell_sort_(nums):
    gap = len(nums)//2
    while gap:
        for i in range(gap,len(nums)):
            val = nums[i]
            j = i-gap
            while j>=0 and val < nums[j]:
                nums[j+gap] = nums[j]
                j -= gap
            nums[j+gap] = val
        gap = gap // 2
    return nums

# merge
def mergeSort(nums):
    # 归并过程
    def merge(left, right):
        result = []  # 保存归并后的结果
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:] # 剩余的元素直接添加到末尾
        return result
    # 递归过程
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

# quick
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [nums[i] for i in range(1,len(nums)) if nums[i] < pivot]
    right = [nums[i] for i in range(1,len(nums)) if nums[i] > pivot]
    return quick_sort(left) + [pivot] +  quick_sort(right)

nums = [0,2,4,6,1,3]
nums = quick_sort(nums)
print(nums)
