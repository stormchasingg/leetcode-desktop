def select_sort(nums):
    for i in range(len(nums)-1):
        index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[index]:
                index = j
        if index != i:
            nums[i], nums[index] = nums[index], nums[i]
            
            
if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    select_sort(nums)
    print(nums)
