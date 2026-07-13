class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        nge = [-1] * len(nums)

        for i in range(2*len(nums)-1,-1,-1):

            while stack and stack[-1] <= nums[i%len(nums)]:
                stack.pop()
            
            if i < len(nums):
                if not stack:
                    nge[i] = -1
                else:
                    nge[i] = stack[-1]
            
            stack.append(nums[i%len(nums)])

        
        return nge
