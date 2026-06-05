class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        index = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        
        if index == -1:
            l = 0 
            r = len(nums)-1
            while l<r:
                nums[l] , nums[r] = nums[r], nums[l]
                l +=1
                r -=1
            return
        
        for i in range(n-1,index,-1):
            if nums[i] > nums[index]:
                nums[i] , nums[index] = nums[index] , nums[i]
                break
        
        l = index + 1
        r = len(nums) - 1
        while l<r:
                nums[l] , nums[r] = nums[r], nums[l]
                l +=1
                r -=1

