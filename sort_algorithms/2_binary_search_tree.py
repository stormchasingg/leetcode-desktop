class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST:
    def __init__(self, nums):
        self.root = TreeNode(nums[0])
        for num in nums[1:]:
            self.insert(num)

    def insert(self, num):
        flag, node, parent = self.search(self.root, self.root, num)
        if not flag:
            if num < parent.val:
                parent.left = TreeNode(num)
            elif num > parent.val:
                parent.right = TreeNode(num)

    def search(self, node, parent, num):
        if not node:
            return False, node, parent
        if num == node.val:
            return True, node, parent
        elif num < node.val:
            return self.search(node.left, node, num)  # 尾递归
        elif num > node.val:
            return self.search(node.right, node, num)


def inorder_traversal(root):
    if not root:
        return []
    left = inorder_traversal(root.left)
    right = inorder_traversal(root.right)
    return left + [root.val] + right


if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    binary_search_tree = BST(nums)
    res = inorder_traversal(binary_search_tree.root)
    print(res)
