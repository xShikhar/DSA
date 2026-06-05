class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:

        l= 0
        res  = [0] * len(nums)
        r = 0

        while l<len(nums):
            res[l] = nums[r]
            l +=1
            if nums[r] == 0 and l<len(nums):
                res[l] = 0
                l +=1
            r += 1

        nums[:] = res
