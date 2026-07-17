class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)

        # ---- MIN contribution (unchanged from your code) ----
        prev_smaller = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        next_smaller_eq = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                next_smaller_eq[stack.pop()] = i
            stack.append(i)

        min_total = 0
        for i in range(n):
            left = i - prev_smaller[i]
            right = next_smaller_eq[i] - i
            min_total += arr[i] * left * right

        # ---- MAX contribution (mirror: flip comparisons) ----
        prev_greater = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            prev_greater[i] = stack[-1] if stack else -1
            stack.append(i)

        next_greater_eq = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                next_greater_eq[stack.pop()] = i
            stack.append(i)

        max_total = 0
        for i in range(n):
            left = i - prev_greater[i]
            right = next_greater_eq[i] - i
            max_total += arr[i] * left * right

        return max_total - min_total
