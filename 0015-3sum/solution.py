class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # If smallest remaining number > 0, no triplet possible
            if nums[i] > 0:
                break

            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If even the three largest can't sum to 0, skip
            if nums[i] + nums[n-1] + nums[n-2] < 0:
                continue

            # If smallest two + nums[i] > 0, no point going further
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
