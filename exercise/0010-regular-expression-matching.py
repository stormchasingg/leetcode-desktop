class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        dp[0][0] = 1
        
        for i in range(2, n+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    if p[j-2] != s[i-1] and p[j-2] != '.':
                        dp[i][j] = dp[i][j-2]
                    elif p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                
                elif s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[m][n] == 1
    
