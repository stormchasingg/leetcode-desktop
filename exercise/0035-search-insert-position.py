class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx = 0
        while nums[idx] < target:
            idx += 1
            if idx == len(nums):
                return idx
        return idx
        
