from tree import construct_tree


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def inorder_traversal(root):
    if not root:
        return []
    left = inorder_traversal(root.left)
    right = inorder_traversal(root.right)
    return left + [root.val] + right


def find_target(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        tmp = nums[l] + nums[r]
        if tmp == target:
            return True
        elif tmp < target:
            l += 1
        else:
            r -= 1
    return False


if __name__ == '__main__':
    root = construct_tree()
    nums = inorder_traversal(root)
    res = find_target(nums, 9)
    print(res)
