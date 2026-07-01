class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        # Step 1: skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: read digits
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num *= sign
        
        # Step 4: clamp to 32-bit signed range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num
