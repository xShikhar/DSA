class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def count_at_most(bound: int) -> int:
            if bound < 0:
                return 0

            left = 0
            window_sum = 0
            total = 0

            for right in range(len(nums)):
                window_sum += nums[right]

                while window_sum > bound:
                    window_sum -= nums[left]
                    left += 1

                total += right - left + 1

            return total

        return count_at_most(goal) - count_at_most(goal - 1)
