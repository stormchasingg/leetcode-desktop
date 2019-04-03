# 01二维数组中的查找
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array[0]) == 0:
            return False
        i, j = 0, len(array[0])-1
        while array[i][j] != target:
            if i == len(array)-1 or j == 0:
                return False
            if array[i][j] < target:
                i += 1
            else:
                j -= 1
        return True

# 02替换空格
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res = ''
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res

# 03从头到尾打印链表
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]

# 04重建二叉树
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None
        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root

# 05用两个栈实现队列
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.lst = []
    def push(self, node):
        # write code here
        self.lst.append(node)
    def pop(self):
        # return xx
        return self.lst.pop(0)

# 06旋转数组的最小数字
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        return min(rotateArray)

# 07斐波那契数列
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        i = 0
        a, b = 0, 1
        while i < n:
            a, b = b, a+b
            i += 1
        return a

# 08跳台阶
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        i = 1
        a, b = 1, 1
        while i <= number:
            a, b = b, a+b
            i += 1
        return a

# 09变态跳台阶
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)

# 10矩形覆盖
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        i = 1
        a, b = 1, 1
        while i <= number:
            a, b = b, a+b
            i += 1
        return a

# 11二进制中1的个数
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n != 0:
            count += 1
            n &= n - 1
        return count

# 12数值的整数次方
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base ** exponent

# 13调整数组顺序使奇数位于偶数前面
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        lst1 = []
        lst2 = []
        for c in array:
            if c % 2 == 1:
                lst1.append(c)
            else:
                lst2.append(c)
        return lst1 + lst2

# 14链表中倒数第k个节点
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        res = []
        while head.next:
            res.append(head)
            head = head.next
        res.append(head)
        if k > len(res):
            return None
        return res[-k]

# 15反转链表
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        prev = None
        while pHead:
            nxt = pHead.next
            pHead.next = prev
            prev = pHead
            pHead = nxt
        return prev

# 16合并两个排序的链表
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        pHead = None
        if pHead1.val < pHead2.val:
            pHead = pHead1
            pHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pHead = pHead2
            pHead.next = self.Merge(pHead1, pHead2.next)
        return pHead

# 17树的子结构
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False
        return self.isSubtree(pRoot1, pRoot2)
    
    def isSubtree(self, p1, p2):
        if p2 == None:
            return True
        if p1 == None:
            return p1 == p2
        res = False
        if p1.val == p2.val:
            res = self.isSubtree(p1.left, p2.left) and self.isSubtree(p1.right, p2.right)
        return res or self.isSubtree(p1.left, p2) or self.isSubtree(p1.right, p2)

# 18二叉树的镜像
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        return self.Mirror(root.left) or self.Mirror(root.right)

# 19顺时针打印矩阵
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return []
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

# 20包含min函数的栈
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.lst = []
        
    def push(self, node):
        # write code here
        self.lst.append(node)
        
    def pop(self):
        # write code here
        return self.lst.pop()
        
    def top(self):
        # write code here
        return self.lst[::-1]
    
    def min(self):
        # write code here
        return min(self.lst)

# 21栈的压入、弹出序列
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV == [] or popV == []:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        return False if len(stack) else True

# 22从上往下打印二叉树
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        queue = []
        res = []
        queue.append(root)
        while len(queue) > 0:
            tmp = queue.pop(0)
            res.append(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return res

# 23二叉搜索树的后序遍历
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence) == 0:
            return False
        i = len(sequence)-1
        for s in sequence:
            if s > sequence[-1]:
                i = sequence.index(s)
                break
        for t in sequence[i:]:
            if t < sequence[-1]:
                return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

# 24二叉树中合为某一值的路径
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

# 25复杂链表的复制
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        # 1
        pClone = pHead
        while pClone:
            node = RandomListNode(pClone.label)
            node.next = pClone.next
            pClone.next = node
            pClone = node.next
        # 2
        pClone = pHead
        while pClone:
            node = pClone.next
            if pClone.random:
                node.random = pClone.random.next
            pClone = node.next
        # 3
        pClone = pHead
        pHead = pHead.next
        while pClone.next:
            node = pClone.next
            pClone.next = node.next
            pClone = node
            
        return pHead

# 26二叉搜索树与双向链表
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.pHead = None
        self.pTail = None
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.Convert(pRootOfTree.left)
        if not self.pHead:
            self.pHead = pRootOfTree
            self.pTail = pRootOfTree
        else:
            self.pTail.right = pRootOfTree
            pRootOfTree.left = self.pTail
            self.pTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.pHead

# 27字符串的排列
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)
        res = []
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i+1:]):
                res.append(ss[i] + j)
        return sorted(set(res))

# 28数组中出现次数超过一半的数字
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        numbers.sort()
        count = 1
        max_count = 1
        max_n = numbers[0]
        for i in range(len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                count += 1
            else:
                count = 1
            if max_count < count:
                max_count = count
                max_n = numbers[i]
        return max_n if max_count*2 > len(numbers) else 0

# 29最小的k个数
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) == 0:
            return []
        if k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]

# 30连续子数组的最大和
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum = array[0]
        res = max_sum
        for i in range(1, len(array)):
            max_sum = max(max_sum + array[i], array[i])
            res = max(res, max_sum)
        return res

# 31整数中1出现的次数（从1到n整数中1出现的次数）
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n+1):
            while i:
                if i % 10 == 1:
                    count += 1
                i /= 10
        return count

# 32把数组排成最小的数
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        str_n = [str(n) for n in numbers]
        for i in range(len(str_n)-1):
            for j in range(i, len(str_n)):
                if str_n[i]+str_n[j] > str_n[j]+str_n[i]:
                    str_n[i], str_n[j] = str_n[j], str_n[i]
        return ''.join(str_n)

# 33丑数
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        ugly_numbers = [1] * index
        count = 1
        count2, count3, count5 = 0, 0, 0
        while count < index:
            min_value = min(ugly_numbers[count2]*2, ugly_numbers[count3]*3, ugly_numbers[count5]*5)
            ugly_numbers[count] = min_value
            while ugly_numbers[count2]*2 <= ugly_numbers[count]:
                count2 += 1
            while ugly_numbers[count3]*3 <= ugly_numbers[count]:
                count3 += 1
            while ugly_numbers[count5]*5 <= ugly_numbers[count]:
                count5 += 1
            count += 1
        return ugly_numbers[-1]
                                                                                                                                                                             
