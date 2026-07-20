class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in range(rows):
            # Step 1: update the histogram heights for this row
            for col in range(cols):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0

            # Step 2: find the largest rectangle in this row's histogram
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # stores indices of bars, heights increasing
        max_area = 0
        # sentinel 0 at the end forces everything remaining to be popped
        extended_heights = heights + [0]

        for i, h in enumerate(extended_heights):
            # pop and finalize rectangles while current bar is shorter
            # than the bar at the top of the stack
            while stack and extended_heights[stack[-1]] > h:
                popped_index = stack.pop()
                height = extended_heights[popped_index]
                # width = current index - index of new stack top - 1
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
