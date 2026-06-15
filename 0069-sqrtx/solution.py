class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        low = 1
        high = x // 2

        while low <= high:
            mid = (low + high) // 2

            if mid * mid < x:
                low = mid + 1
            elif mid * mid == x:
                return mid
            else:                  
                high = mid - 1
            
        return high               
