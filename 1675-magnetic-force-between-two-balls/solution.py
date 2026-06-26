class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        low , high = 1 , position[-1] - position[0]

        def canPlace(d):
            count = 1 
            last_placed = position[0]
            for i in range(1,len(position)):
                if position[i] - last_placed >= d:
                    count += 1
                    last_placed = position[i]

            return count >= m

        while low <= high:
            mid = ( low + high )//2
            if canPlace(mid):
                low = mid + 1
            else: 
                high = mid - 1

        return high
