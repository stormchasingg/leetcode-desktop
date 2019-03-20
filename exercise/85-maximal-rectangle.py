class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) < 1:
            return 0
        raw, col, res = len(matrix), len(matrix[0]), 0
        dp = [[0 for x in range(col)] for x in range(raw)]
        for i in range(raw):
            for j in range(col):
                if i == 0 and matrix[i][j] == '1':
                    dp[i][j] = 1
                if i > 0 and matrix[i][j] == '1':
                    dp[i][j] = 1 + dp[i-1][j]
        for r in range(raw):
            res = max(res, self.maximalHistogram(dp[r]))
        return res
    
    def maximalHistogram(self, height):
        height.append(0)
        stack = [-1]
        res = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        height.pop()
        return res
