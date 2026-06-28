class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        x = 0
        res = []
        for i in range(len(s)):
            if s[i] == '(':
                if x > 0:
                    res.append(s[i])
                x += 1
            else:
                x -= 1
                if x > 0:
                    res.append(s[i])
        return ''.join(res)
