class Solution(object):
    def summaryRanges(self, nums):
        num_set = set(nums)
        result = []

        for i in nums:  # ✅ nums is already sorted, skip set iteration
            if i - 1 not in num_set:
                length = 1
                while i + length in num_set:
                    length += 1

                if length == 1:
                    result.append(str(i))
                else:
                    result.append(str(i) + "->" + str(i + length - 1))

        return result
