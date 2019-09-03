from tree import construct_tree


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def max_depth(root):
    if not root:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return max(left, right) + 1


if __name__ == '__main__':
    root = construct_tree()
    res = max_depth(root)
    print(res)
