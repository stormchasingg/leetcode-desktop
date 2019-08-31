def adjust_heap(nums, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    largest = i
    if i < size / 2:
        if lchild < size and nums[lchild] > nums[largest]:
            largest = lchild
        if rchild < size and nums[rchild] > nums[largest]:
            largest = rchild
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            adjust_heap(nums, largest, size)


def build_heap(nums, size):
    for i in range(size // 2, -1, -1):
        adjust_heap(nums, i, size)


def heap_sort(nums):
    size = len(nums)
    for i in range(size-1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        adjust_heap(nums, 0, i)


if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    heap_sort(nums)
    print(nums)
