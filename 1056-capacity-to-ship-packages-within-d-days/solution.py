class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)        # was 1 → capacity below the heaviest package is impossible (see trace above)
        high = 0

        for i in range(len(weights)):
            high += weights[i]

        while low <= high:
            mid = (low + high)//2

            x, day, remaining = mid, 1, mid     # was `x, day = mid, 0` → day starts at 1; remaining tracks the countdown separately so mid stays intact

            for i in range(len(weights)):
                if weights[i] > remaining:      # was `if mid < 0` → check BEFORE committing the weight, not after
                    day += 1
                    remaining = x
                remaining -= weights[i]
            
            if day > days:
                low = mid + 1
            else:
                high = mid - 1
        return low
