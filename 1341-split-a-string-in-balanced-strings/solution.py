class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c ,x = 0, 0
        for i in range(len(s)):
            if s[i] == 'R':
                c += 1
            else:
                c -= 1
            if c == 0:
                x += 1
        return x
