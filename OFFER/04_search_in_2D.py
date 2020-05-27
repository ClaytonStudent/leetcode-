class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:  # 注意为空的情况out of range
            return False
        m,n = len(matrix),len(matrix[0])
        i,j = 0,n-1 # 从右上角开始
        while i < m and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


nums = [[1,2,8,9],
    [2,4,9,12],
    [4,7,10,13],
    [6,8,11,15]]

S = Solution()
ans = S.findNumberIn2DArray(nums,8)
print(ans)