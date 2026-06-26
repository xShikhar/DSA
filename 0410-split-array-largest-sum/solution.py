class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(maxSum: int) -> bool:
            subarrays = 1
            currentSum = 0
            for num in nums:
                if currentSum + num > maxSum:
                    subarrays += 1
                    currentSum = 0
                currentSum += num
            return subarrays <= k

        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) // 2
            if canSplit(mid):
                high = mid
            else:
                low = mid + 1

        return low
