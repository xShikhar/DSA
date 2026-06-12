class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        less = 0
        equal = 0 

        for n in nums:
            if n < target:
                less += 1
            if n == target:
                equal += 1
        
        return list(range(less,less+equal))
