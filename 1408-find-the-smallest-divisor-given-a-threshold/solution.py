import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:


        def divideSum(mid,nums,threshold):
            sum_division = 0
            for i in range(len(nums)):
                sum_division += math.ceil(nums[i]/mid)
            
            return sum_division <= threshold


        low = 1                 
        high = max(nums)         
    
        while low <= high:
            mid = (low + high)//2
            
            if divideSum(mid,nums,threshold):
                high = mid - 1     
            else:
                low = mid + 1      
            
        return low
