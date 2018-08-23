'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
'''
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in d:
                return (d[target-x], i)
            d[x] = i


