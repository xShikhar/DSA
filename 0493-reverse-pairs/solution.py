class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge(arr, low, mid, high):
            temp = []
            left, right = low, mid + 1
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left]); left += 1
                else:
                    temp.append(arr[right]); right += 1
            while left <= mid:
                temp.append(arr[left]); left += 1
            while right <= high:
                temp.append(arr[right]); right += 1
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        def countPairs(arr, low, mid, high):
            count = 0
            right = mid + 1
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:  # ← arr[right], not arr[j]
                    right += 1
                count += right - (mid + 1)
            return count

        def mergeSort(arr, low, high):
            if low >= high:
                return 0                              # ← return 0, not None
            mid = (low + high) // 2
            count  = mergeSort(arr, low, mid)
            count += mergeSort(arr, mid + 1, high)
            count += countPairs(arr, low, mid, high)
            merge(arr, low, mid, high)               # ← don't add return value
            return count

        return mergeSort(nums, 0, len(nums) - 1)
