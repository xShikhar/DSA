class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        nums_set = set(nums)
        nums_list = list(nums_set)
        m = len(nums_list)
        count = list(range(m))
        x= 0
        for i in nums_list:
            count[x] = nums.count(i)
            x = x + 1
        
        for i in range(m):
            if count[i] > n//2:
                return nums_list[i]
