class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if len(bloomDay) < m*k:
            return -1
        

        def calVal(mid,bloomDay):

            x = k
            cur = 0
            bouquets = 0    

            for day in bloomDay:
                if day <= mid:                  
                    cur += 1
                    if cur == x:
                        bouquets += 1
                        cur = 0
                else:
                    cur = 0

            return bouquets >= m              
                

        low = 1
        high = max(bloomDay)

        while low <= high:
            mid = (low + high)//2

            if calVal(mid,bloomDay):            
                high = mid - 1
            else:
                low = mid + 1

        return low
