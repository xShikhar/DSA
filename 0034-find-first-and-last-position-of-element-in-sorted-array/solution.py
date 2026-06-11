class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    idx = mid        # candidate found, but keep going left
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return idx

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    idx = mid        # candidate found, but keep going right
                    left = mid + 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return idx

        return [findLeft(nums, target), findRight(nums, target)]
