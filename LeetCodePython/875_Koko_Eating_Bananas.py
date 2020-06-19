# 875. Koko Eating Bananas
# source: https://leetcode.com/problems/koko-eating-bananas/
class Solution(object):

    def minEatingSpeed(self, piles, H):
        left, right = 0, max(piles)
        while left < right: # O(lgn) for binary search, totally O(NlgN)
            mid = (left + right) / 2
            # print(left, right, mid)
            if self.whether(piles, H, mid): # this will take O(n)
                right = mid
            else:
                left = mid + 1
        return left
        
    def whether(self, piles, H, K):
        # print(K)
        total = [ (bananas+K-1)//K for bananas in piles]
        return sum(total) <= H
