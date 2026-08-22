class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        prev = 0
        current = 1
        ans = 0

        for i in range(1,len(s)):

            if s[i] == s[i-1]:
                current += 1
            
            else:
                ans += min(prev,current)
                prev = current 
                current = 1
            
        
        ans += min(prev,current)

        return ans
