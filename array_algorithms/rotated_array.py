def rotated_array(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < nums[r]:
            r = mid
        elif nums[mid] > nums[r]:
            l = mid + 1
        else:
            r -= 1
    return nums[l]


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2, 3]
    res = rotated_array(nums)
    print(res)
