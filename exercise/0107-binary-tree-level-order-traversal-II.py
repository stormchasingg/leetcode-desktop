# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, level, res):
            if not node:
                return
            if len(res) < level:
                res.append([])
            res[level-1].append(node.val)
            dfs(node.left, level+1, res)
            dfs(node.right, level+1, res)
            
        res = []
        dfs(root, 1, res)
        return res[::-1]
    
