class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if x < 0:
            sign = '-'
            digits = str(x)[1:]   # strip the '-'
        else:
            sign = ''
            digits = str(x)

        res = sign
        for i in range(len(digits) - 1, -1, -1):
            res += digits[i]

        result = int(res)

        if result < INT_MIN or result > INT_MAX:
            return 0

        return result
