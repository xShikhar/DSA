class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:               # loop until the window collapses to 1 element
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1           # going uphill rightward, peak is to the right
            else:
                high = mid              # going downhill rightward, peak is here or left

        return low                      # low == high, this is the peak index
