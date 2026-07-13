class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = {}
        st = []

        i = len(nums2) - 1
        while i >= 0:
            num = nums2[i]

            while len(st) > 0 and st[-1] <= num:
                st.pop()

            if len(st) == 0:
                answer[num] = -1
            else:
                answer[num] = st[-1]

            st.append(num)
            i -= 1

        result = []
        for n in nums1:
            result.append(answer[n])

        return result
