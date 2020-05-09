# Introduction : https://www.jianshu.com/p/bbbab7fa77a2
# 1.Insertion Sorting
# 插入排序如同打扑克一样，每次将后面的牌插到前面已经排好序的牌中(进阶版:拆半插入)
# 2. Shell Sorting
# 它与插入排序的不同之处在于，它会优先比较距离较远的元素。核心在于间隔序列的设定
# 特性: https://www.jianshu.com/p/d730ae586cf3
# 3. Selection Sorting
# 选择排序每次选出最小的元素,
# 特性: 选择排序不受输入数据的影响，即在任何情况下时间复杂度不变
# 4. Heap Sort (有点难)
# 堆排序: build max heap: O(n), heapify O(logn)
# 5. bubble Sorting
# 冒泡排序每次找出一个最大的元素
# 6. quick Sorting
# 冒泡排序基础上的递归分治法, 处理大数据最快的排序算法之一

# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 


def shellSort_dynamic(nums):
    lens = len(nums)
    gap = 1
    while gap < lens // 3:
        gap = gap * 3 + 1  # 动态定义间隔序列
    while gap > 0:
        for i in range(gap, lens):
            curNum, preIndex = nums[i], i - gap  # curNum 保存当前待插入的数
            while preIndex >= 0 and curNum < nums[preIndex]:
                nums[preIndex + gap] = nums[preIndex] # 将比 curNum 大的元素向后移动
                preIndex -= gap
            nums[preIndex + gap] = curNum  # 待插入的数的正确位置
        gap //= 3  # 下一个动态间隔
    return nums


def shellSort_static(nums):
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            curNum, preIndex = nums[i], i - gap  # curNum 保存当前待插入的数
            while preIndex >= 0 and curNum < nums[preIndex]:
                nums[preIndex + gap] = nums[preIndex] # 将比 curNum 大的元素向后移动
                preIndex -= gap
            nums[preIndex + gap] = curNum  # 待插入的数的正确位置
        gap //= 2  # 下一个动态间隔
    return nums
    
def shellSort(arr): 
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n/2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap /= 2
    return nums

# 大根堆（从小打大排列）
def heapSort(nums):
    # 调整堆
    def adjustHeap(nums, i, size):
        # 非叶子结点的左右两个孩子
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        # 在当前结点、左孩子、右孩子中找到最大元素的索引
        largest = i
        if lchild < size and nums[lchild] > nums[largest]:
            largest = lchild
        if rchild < size and nums[rchild] > nums[largest]:
            largest = rchild
        # 如果最大元素的索引不是当前结点，把大的结点交换到上面，继续调整堆
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            # 第 2 个参数传入 largest 的索引是交换前大数字对应的索引
            # 交换后该索引对应的是小数字，应该把该小数字向下调整
            adjustHeap(nums, largest, size)
    # 建立堆
    def builtHeap(nums, size):
        for i in range(len(nums)//2)[::-1]: # 从倒数第一个非叶子结点开始建立大根堆
            adjustHeap(nums, i, size) # 对所有非叶子结点进行堆的调整
        # print(nums)  # 第一次建立好的大根堆
    # 堆排序
    size = len(nums)
    builtHeap(nums, size)
    for i in range(len(nums))[::-1]:
        # 每次根结点都是最大的数，最大数放到后面
        nums[0], nums[i] = nums[i], nums[0]
        # 交换完后还需要继续调整堆，只需调整根节点，此时数组的 size 不包括已经排序好的数
        adjustHeap(nums, 0, i)
    return nums  # 由于每次大的都会放到后面，因此最后的 nums 是从小到大排列


def bubbleSort_1(nums): # 每次找到最大得放最后一个
    for i in range(len(nums) - 1): # 遍历 len(nums)-1 次
        for j in range(len(nums) - i - 1): # 已排好序的部分不用再次遍历
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] # Python 交换两个数不用中间变量
        print(nums)
    return nums

def bubbleSort_2(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
        print(nums)
    return nums


def selectionSort(nums): # 每次找到最小得元素放第一个
    for i in range(len(nums) - 1):  # 遍历 len(nums)-1 次
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:  # 更新最小值索引
                minIndex = j  
        nums[i], nums[minIndex] = nums[minIndex], nums[i] # 把最小数交换到前面
    return nums

def quickSort(nums):  # 这种写法的平均空间复杂度为 O(nlogn)
    if len(nums) <= 1:
        return nums
    pivot = nums[0]  # 基准值
    left = [nums[i] for i in range(1, len(nums)) if nums[i] < pivot]
    right = [nums[i] for i in range(1, len(nums)) if nums[i] >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)
    
def quickSort2(nums, left, right):  # 这种写法的平均空间复杂度为 O(logn)
    # 分区操作
    def partition(nums, left, right):
        pivot = nums[left]  # 基准值
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]  # 比基准小的交换到前面
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]  # 比基准大交换到后面
        nums[left] = pivot # 基准值的正确位置，也可以为 nums[right] = pivot
        return left  # 返回基准值的索引，也可以为 return right
    # 递归操作
    if left < right:
        pivotIndex = partition(nums, left, right)
        quickSort2(nums, left, pivotIndex - 1)  # 左序列
        quickSort2(nums, pivotIndex + 1, right) # 右序列
    return nums


# source: https://brilliant.org/wiki/counting-sort/
# analysis: counting sort不同于以对比为基础的sorting，只能用于正数的排序。

def counting_sort(A, digit, radix):
    #"A" is a list to be sorted, radix is the base of the number system, digit is the digit
    #we want to sort by

    #create a list B which will be the sorted list
    B = [0]*len(A)
    C = [0]*int(radix)
    #counts the number of occurences of each digit in A
    for i in range(0, len(A)):
        digit_of_Ai = (A[i]//radix**digit)%radix
        C[digit_of_Ai] = C[digit_of_Ai] +1
        #now C[i] is the value of the number of elements in A equal to i

    #this FOR loop changes C to show the cumulative # of digits up to that index of C
    for j in range(1,radix):
        C[j] = C[j] + C[j-1]
    print(C)
        #here C is modifed to have the number of elements <= i
    for m in range(len(A)-1, -1, -1): #to count down (go through A backwards)
        digit_of_Ai = (A[m]//radix**digit)%radix
        print(digit_of_Ai)
        C[digit_of_Ai] = C[digit_of_Ai] -1
        B[C[digit_of_Ai]] = A[m]

    return B

def radix_sort(A, radix):
    #radix is the base of the number system
    #k is the largest number in the list
    k = max(A)
    #output is the result list we will build
    output = A
    #compute the number of digits needed to represent k
    digits = int(math.floor(math.log(k, radix)+1))
    print('Digits:',digits)
    for i in range(digits):
        output = counting_sort(output,i,radix)
        print(output)
    return output