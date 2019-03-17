# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root or root.val > expectNumber:
            return []
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        else:
            expectNumber -= root.val
            left = self.FindPath(root.left, expectNumber)
            right = self.FindPath(root.right, expectNumber)
            res = [[root.val] + l for l in left]
            res += [[root.val] + r for r in right]
        return sorted(res, key=lambda x: -len(x))
