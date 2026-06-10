class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array1 = nums[:n]
        array2 = nums[n:]

        ans = []
        for i in range(n):
            ans.append(array1[i])
            ans.append(array2[i])

        return ans
            
