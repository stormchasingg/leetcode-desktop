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

    """
一、题目
    给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
二、案例
    输入:
        5
       / \
      3   6
     / \   \
    2   4   7
    Target = 9
    输出: True（因为存在 2 + 7 = 9）
三、思路
    使用中序遍历得到有序数组之后，再利用双指针对数组进行查找。
    应该注意到，这一题不能用分别在左右子树两部分来处理这种思想，因为两个待求的节点可能分别在左右子树中。
"""
