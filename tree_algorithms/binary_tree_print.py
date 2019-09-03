from tree import construct_tree


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def print_binary_tree(root):
    if not root:
        return []
    level = [root]
    res = []
    while level:
        tmp = []
        nxt_level = []
        for i in level:
            tmp.append(i.val)
            if i.left:
                nxt_level.append(i.left)
            if i.right:
                nxt_level.append(i.right)
        res.append(tmp)
        level = nxt_level
    return res


if __name__ == '__main__':
    root = construct_tree()
    res = print_binary_tree(root)
    print(res)
