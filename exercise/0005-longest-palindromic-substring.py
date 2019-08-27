class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def preProcess(s):
            if not s:
                return ['^', '&']
            T = ['^']
            for i in s:
                T += ['#', i]
            T += ['#', '$']
            return T
        T = preProcess(s)
        P = [0] * len(T)
        id, mx = 0, 0
        for i in range(1, len(T)-1):
            j = 2 * id - i
            if mx > i:
                P[i] = min(P[j], mx - i)
            else:
                P[i] = 0
            while T[i+P[i]+1] == T[i-P[i]-1]:
                P[i] += 1
            if i + P[i] > mx:
                id, mx = i, i + P[i]
        max_i = P.index(max(P))
        start = (max_i - P[max_i] - 1) // 2
        res = s[start:start+P[max_i]]
        return res
        
