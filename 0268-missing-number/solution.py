class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = (n*(n+1))/2
        sum_nums = 0
        for i in range(n):
            sum_nums += nums[i]
        return int(sum_n-sum_nums)
