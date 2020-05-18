def find_integer(nums,target):
    if not nums:
        return False
    rows, cols = len(nums), len(nums[0])
    i = 0
    j = cols -1 # 从右上角开始
    while i< rows and j >=0:
        if nums[i][j] ==  target:
            return True
        elif nums[i][j] < target:
            i += 1
        else:
            j -= 1
    return False


nums = [[1,2,8,9],
    [2,4,9,12],
    [4,7,10,13],
    [6,8,11,15]]


ans = find_integer(nums,8)
print(ans)