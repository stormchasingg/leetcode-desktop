def quick_sort(nums, start, end):
    if start >= end:
        return
    base = nums[start]
    l, r = start, end
    # one quick sort
    while l < r:
        while l < r and nums[r] >= base:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] < base:
            l += 1
        nums[r] = nums[l]
    nums[l] = base
    # recursion
    quick_sort(nums, start, l - 1)
    quick_sort(nums, l + 1, end)
    
    
if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)
