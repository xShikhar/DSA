class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def count_at_most(bound: int) -> int:
            if bound < 0:
                return 0

            left = 0
            odd_count = 0
            total = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1

                while odd_count > bound:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1

                total += right - left + 1

            return total

        return count_at_most(k) - count_at_most(k - 1)
