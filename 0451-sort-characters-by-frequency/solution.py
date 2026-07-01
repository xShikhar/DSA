class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0) + 1
        
        t = []
        freq = dict(sorted(freq.items(),key = lambda item: item[1], reverse = True))
        for i in freq:
            t.append(i * freq[i])
        
        return "".join(t)
