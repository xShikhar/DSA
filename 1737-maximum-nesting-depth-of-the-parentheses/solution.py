class Solution:
    def maxDepth(self, s: str) -> int:
        
        openparan = 0
        maxparan = float('-inf')

        for i in range(len(s)):

            if s[i] == '(':
                openparan += 1
                maxparan = max(maxparan, openparan)
            elif s[i] == ')':
                openparan -= 1
        return maxparan if maxparan != float('-inf') else 0
