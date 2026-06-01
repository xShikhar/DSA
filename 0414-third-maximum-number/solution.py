class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float("-inf")

        for n in set(nums):
            if n > first:
                first, second, third = n, first, second
            elif n > second:
                first, second, third = first, n, second
            elif n > third:
                third = n

        if third == float("-inf"):   
            return first
        return third
