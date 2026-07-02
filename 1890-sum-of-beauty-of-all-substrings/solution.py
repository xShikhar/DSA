class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        n = len(s)

        for i in range(n):
            counts = [0] * 26          # frequency of each letter, reset for new start i

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                counts[idx] += 1        # extend substring by one char, update count

                most = max(counts)
                least = min(c for c in counts if c > 0)   # ignore letters with 0 count

                total += most - least

        return total
