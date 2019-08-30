def merge(left, right):
    l, r = 0, 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:]
    res += right[r:]
    return res


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    i = len(nums) // 2
    return merge(merge_sort(nums[:i]), merge_sort(nums[i:]))


if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    nums = merge_sort(nums)
    print(nums)
