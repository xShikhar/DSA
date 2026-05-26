class Solution(object):
    def fourSum(self, nums, target):
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1

            while left < n - 2:
                # Skip duplicates for left
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue

                right = n - 1       # ✅ reset right for every new left
                mid = left + 1

                while mid < right:
                    total = nums[i] + nums[left] + nums[mid] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[left], nums[mid], nums[right]])
                        # Skip duplicates for mid and right
                        while mid < right and nums[mid] == nums[mid + 1]:
                            mid += 1
                        while mid < right and nums[right] == nums[right - 1]:
                            right -= 1
                        mid += 1
                        right -= 1

                    elif total < target:
                        mid += 1
                    else:
                        right -= 1

                left += 1

        return result
