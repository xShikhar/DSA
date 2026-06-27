class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True

        l = 0
        c = 0

        for r in range(len(t)):
            if s[l] == t[r]:
                c += 1
                l += 1
            if c == len(s):
                return True
        return False
