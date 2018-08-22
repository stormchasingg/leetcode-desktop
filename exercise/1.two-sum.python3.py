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
        size = 0
        d = {}
        while size < len(nums):
            if not nums[size] in d:
                d[nums[size]] = size
            if target - nums[size] in d:
                if d[target - nums[size]] < d[nums[size]]:
                    result = [d[target - nums[size]], d[nums[size]]]
                    return result
            size = size + 1
