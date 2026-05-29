class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        best = 0
        for n in num_set:
            if n - 1 not in num_set:
                length = 1
                while n  + length in num_set:
                    length = length + 1
                best = max(length , best)
        return best

