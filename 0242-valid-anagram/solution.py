class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}
        for c in s:
            count[c] = count.get(c,0) + 1
        for c in t:
            count[c] = count.get(c,0) - 1
            if count[c] < 0:
                return False
        
        return True
