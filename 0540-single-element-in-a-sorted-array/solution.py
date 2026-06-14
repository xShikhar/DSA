class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # Ensure mid is even so we always compare (mid, mid+1) as a candidate pair
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # Pair is intact, single must be to the right
                low = mid + 2
            else:
                # Pair is broken, single is at mid or to the left
                high = mid

        return nums[low]
