class Solution(object):
    def containsDuplicate(self, nums):
        count = {}
        for n in nums:
            if n in count:
                return True          # duplicate found → exit immediately
            count[n] = 1
        return False
