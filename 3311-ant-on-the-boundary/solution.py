class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:

        sum1 = 0 
        count = 0

        for i in range(len(nums)):
            sum1 = sum1 + nums[i]
            if sum1 == 0:
                count += 1
        
        return count

