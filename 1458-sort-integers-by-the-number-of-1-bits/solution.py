class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def count_ones(n):
            return bin(n).count('1')
        
        arr.sort(key=lambda x: (count_ones(x), x))
        
        return arr
