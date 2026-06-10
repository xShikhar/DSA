class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = suffix = 1
        result = float('-inf')

        for i in range(len(nums)):
            prefix *= nums[i]
            suffix *= nums[len(nums)-1-i]
            result = max(result,prefix,suffix)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        
        return result
                
