class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:

        left = 0
        right = len(arr) - 1

        while left<=right:
            mid = (left + right)//2
            if target == arr[mid]:
                return mid
            elif target>arr[mid]:
                left = mid + 1
            else:
                right = mid -1
        return left
