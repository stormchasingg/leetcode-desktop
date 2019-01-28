class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                nums[idx] = nums[-1]
                del nums[-1]
            else:
                idx += 1
        return len(nums)
    
