class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        count = []

        for char in s:

            if stack and stack[-1] == char:
                count[-1] += 1
                if count[-1] == k:
                    stack.pop()
                    count.pop()
            
            else:
                stack.append(char)
                count.append(1)
        
        result = []

        return "".join(c * n for c,n in zip(stack,count))
