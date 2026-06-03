class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_n = 0 

        max_sum = float('-inf')

        for r in range(len(nums)):
            sum_n += nums[r]

            if sum_n > max_sum:
                max_sum = sum_n
            if sum_n < 0:
                sum_n = 0
        return max_sum

           
