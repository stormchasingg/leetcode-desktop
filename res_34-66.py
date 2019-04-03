# 34第一个只出现一次的字符
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        for i in range(len(s)-1):
            if s[i] not in s[:i]+s[i+1:]:
                return i
        return -1

# 35数组中的逆序对
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        return self.inverseCount(data[:], 0, len(data)-1, data[:])%1000000007
        
    def inverseCount(self, tmp, start, end, data):
        if end-start <1:
            return 0
        if end - start == 1:
            if data[start]<=data[end]:
                return 0
            else:
                tmp[start], tmp[end] = data[end], data[start]
                return 1
        mid = (start+end)//2
        cnt = self.inverseCount(data, start, mid, tmp) + self.inverseCount(data, mid+1, end, tmp)
        # print(start, mid, end, cnt, data)
        i = start
        j = mid + 1
        ind = start
            
        while(i <= mid and j <= end):
            if data[i] <= data[j]:
                tmp[ind] = data[i]
                i += 1
            else:
                tmp[ind] = data[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while(i<=mid):
            tmp[ind] = data[i]
            i += 1
            ind += 1
        while(j<=end):
            tmp[ind] = data[j]
            j += 1
            ind += 1
        return cnt

# 36两个链表的第一个公共结点
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        p1, p2 = pHead1, pHead2
        len1, len2 = 0, 0
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next
        if len1 > len2:
            while len1 - len2:
                pHead1 = pHead1.next
                len1 -= 1
        else:
            while len2 - len1:
                pHead2 = pHead2.next
                len2 -= 1
        while pHead1 and pHead2:
            if pHead1 is pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return None

# 37数字在排序数组中出现的次数
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        key1 = 0
        key2 = 0
        l = 0
        r = 0
        for d in data:
            if d == k and key1 == 0:
                l = data.index(d)
                key1 = 1
                key2 = 1
            if key2 == 1:
                if d != k:
                    r = data.index(d)
                    break
            if key1 == 1 and d == data[-1]:
                r = len(data)
        return r-l

# 38二叉树的深度
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        res = max(left, right) + 1
        return res

# 39平衡二叉树
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.getDepth(pRoot.left) - self.getDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        
    def getDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.getDepth(pRoot.left) + 1
        right = self.getDepth(pRoot.right) + 1
        return max(left, right)

# 40数组中只出现一次的数字
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return []
        array.sort()
        res = []
        for i in range(1, len(array)-1):
            if array[i] != array[i-1] and array[i] != array[i+1]:
                res.append(array[i])
        if array[0] != array[1]:
            res.append(array[0])
        if array[-1] != array[-2]:
            res.append(array[-1])
        return res

# 41和为S的连续正数序列
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        l, r = 1, 2
        length = (tsum + 1) / 2
        cur = l + r
        res = []
        while l < length:
            if cur == tsum:
                res.append(range(l, r+1))
            while cur > tsum and l < length:
                cur -= l
                l += 1
                if cur == tsum:
                    res.append(range(l, r+1))
            r += 1
            cur += r
        return res

# 42和为S的两个数字
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        for num in array:
            if tsum - num in array:
                return [num, tsum-num]
        return []

# 43左旋转字符串
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:] + s[:n]

# 44翻转单词顺序列
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s == '':
            return s
        if s[0] == ' ':
            return s
        tmp = s.split()
        if len(tmp) == 1:
            return s
        else:
            for i in range(1, len(tmp)):
                tmp[i] += ' '
        return ''.join(tmp[::-1])

# 45扑克牌顺子
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) == 0:
            return False
        numbers.sort()
        if numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0 and numbers[3] == 0:
            return True
        elif numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0:
            if len(set(numbers[3:])) == 2:
                return True if numbers[4] - numbers[3] < 5 else False
            else:
                return False
        elif numbers[0] == 0 and numbers[1] == 0:
            if len(set(numbers[2:])) == 3:
                return True if numbers[4] - numbers[2] < 5 else False
            else:
                return False
        elif numbers[0] == 0:
            if len(set(numbers[1:])) == 4:
                return True if numbers[4] - numbers[1] < 5 else False
            else:
                return False
        else:
            if len(set(numbers)) == 5:
                return True if numbers[4] - numbers[0] < 5 else False
            else:
                return False

# 46孩子们的游戏（圆圈中最后剩下的数）
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n+1):
            last = (last + m) % i
        return last

# 47求1+2+3+...+n
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and self.Sum_Solution(n-1) + n

# 48不用加减乘除做加法
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            tmp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = tmp & 0xffffffff
        return num1 if num1 >> 31 == 0 else num1 - 2**32

# 49把字符串转换成整数
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        s = s.strip()
        if not s or len(s) < 1:
            return 0
        lookup = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        key = 0
        if len(s) == 1:
            if s in lookup.keys():
                return lookup[s]
            else:
                return 0
        if s[0] == '+':
            s = s[1:]
        if s[0] == '-':
            s = s[1:]
            key = 1
        res = 0
        for i in s:
            if i in lookup.keys():
                res = res * 10 + lookup[i]
            else:
                return 0
        return res if key == 0 else -res

# 50数组中重复的数字
# -*- coding:utf-8 -*-
import collections
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        c = collections.Counter(numbers)
        for k, v in c.items():
            if v > 1:
                duplication[0] = k
                return True
        return False

# 51构建乘积数组
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A or len(A) == 0:
            return []
        
        B = [1 for x in A]
        for i in range(1, len(A)):
            B[i] = B[i-1] * A[i-1]
        
        tmp = 1
        for j in range(len(A)-2, -1, -1):
            tmp *= A[j+1]
            B[j] *= tmp
        return B

# 52正则表达式匹配
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (pattern[0] == s[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        if len(s) > 0 and (pattern[0] == s[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        return False

# 53表示数值的字符串
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            p = float(s)
            return True
        except:
            return False

# 54字符流中第一个不重复的数
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.lookup = {}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.lookup[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        if char in self.lookup:
            self.lookup[char] += 1
        else:
            self.lookup[char] = 1

# 55链表中环的入口结点   
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None or pHead.next == None or pHead.next.next == None:
            return None
        slow = pHead.next
        fast = pHead.next.next
        while slow != fast:
            if fast.next == None or fast.next.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
        slow = pHead
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

# 56删除链表中重复的结点
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        lst = []
        while pHead:
            lst.append(pHead.val)
            pHead = pHead.next
        lst = list(filter(lambda x: lst.count(x) == 1, lst))
        dummy = ListNode(-1)
        pre = dummy
        for i in lst:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return dummy.next

# 57二叉树的下一个结点
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        while pNode.next != None:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        return None

# 58对称的二叉树
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.helper(pRoot.left, pRoot.right)
    
    def helper(self, left, right):
        if left == None: return right == None
        if right == None: return False
        if left.val != right.val: return False
        return self.helper(left.right, right.left) and self.helper(left.left, right.right)

# 59按之字顺序打印二叉树
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        level = [pRoot]
        res = []
        flag = False
        while level:
            tmp = []
            nxt_level = []
            for i in level:
                tmp.append(i.val)
                if i.left:
                    nxt_level.append(i.left)
                if i.right:
                    nxt_level.append(i.right)
            if flag:
                tmp = tmp[::-1]
            res.append(tmp)
            level = nxt_level
            flag = not flag
        return res

# 60把二叉树打印成多行
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        level = [pRoot]
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

# 61序列化二叉树
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.flag = -1
        
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
    
    def Deserialize(self, s):
        # write code here
        self.flag += 1
        lst = s.split(',')
        if self.flag >= len(s):
            return None
        root = None
        if lst[self.flag] != '#':
            root = TreeNode(int(lst[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

# 62二叉搜索树的第k个结点
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.lst = []
    def KthNode(self, pRoot, k):
        # write code here
        if k <= 0:
            return None
        self.helper(pRoot)
        if k > len(self.lst):
            return None
        else:
            return self.lst[k-1]
    def helper(self, p):
        if not p:
            return None
        self.helper(p.left)
        self.lst.append(p)
        self.helper(p.right)

# 63数据流中的中位数
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.lst = []
    def Insert(self, num):
        # write code here
        self.lst.append(num)
        self.lst.sort()
    def GetMedian(self, lst):
        # write code here
        if len(self.lst) % 2 == 0:
            return (self.lst[len(self.lst)//2] + self.lst[len(self.lst)//2-1])/2.0
        else:
            return self.lst[len(self.lst)//2]

# 64滑动窗口的最大值
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size > len(num) or size <= 0:
            return []
        res = []
        for i in range(len(num)-size+1):
            res.append(max(num[i:i+size]))
        return res

# 65矩阵中的路径
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.find(list(matrix), rows, cols, path[1:], i, j):
                        return True
        return False
    
    def find(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i*cols+j] = '0'
        if j+1<cols and matrix[i*cols+j+1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j+1)
        elif j-1>=0 and matrix[i*cols+j-1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j-1)
        elif i+1<rows and matrix[(i+1)*cols+j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i+1, j)
        elif i-1>=0 and matrix[(i-1)*cols+j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i-1, j)
        else:
            return False

# 66机器人的运动范围
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0
    def movingCount(self, threshold, rows, cols):
        # write code here
        dp = [[1 for i in range(cols)] for j in range(rows)]
        self.helper(dp, threshold, 0, 0)
        return self.count
    
    def helper(self, dp, threshold, i, j):
        if i < 0 or j < 0 or i >= len(dp) or j >= len(dp[0]):
            return None
        tmp1 = list(map(int, list(str(i))))
        tmp2 = list(map(int, list(str(j))))
        if sum(tmp1)+sum(tmp2) > threshold or dp[i][j] == 0:
            return None
        dp[i][j] = 0
        self.count += 1
        self.helper(dp, threshold, i+1, j)
        self.helper(dp, threshold, i-1, j)
        self.helper(dp, threshold, i, j+1)
        self.helper(dp, threshold, i, j-1)
                                                                                                                                                                                                                                                                                           
