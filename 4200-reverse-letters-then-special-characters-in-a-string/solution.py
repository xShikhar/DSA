class Solution:
    def reverseByType(self, s: str) -> str:
        letter = []
        symbol = []
        for i in s:
            if 97 <= ord(i) and ord(i) <= 122:
                letter.append(i)
            else:
                symbol.append(i)
        result = []
        l = len(letter) - 1 
        r = len(symbol) - 1
        for i in range(len(s)):
            if 97 <= ord(s[i]) and ord(s[i]) <= 122:
                result.append(letter[l])
                l -= 1
            else:
                result.append(symbol[r])
                r -= 1
        return "".join(result)
