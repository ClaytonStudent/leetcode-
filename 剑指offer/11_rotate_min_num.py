# 题目：旋转数组中的最小数字
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if not numbers:
            return None
        left, right = 0, len(numbers)-1
        while left < right:
            mid = (left+right)//2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1 # 无法判断在哪里， 执行j=j−1 缩小判断范围
        return numbers[left]



nums = [3,3,1,3]
S = Solution()
print(S.minArray(nums))