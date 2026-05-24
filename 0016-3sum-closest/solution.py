class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')
        n = len(nums)

        for i in range(n - 2):

            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # pruning — best case this i can offer is too far above target
            if nums[i] + nums[i+1] + nums[i+2] > target:
                if abs(nums[i]+nums[i+1]+nums[i+2] - target) < abs(closest - target):
                    closest = nums[i] + nums[i+1] + nums[i+2]
                break

            # pruning — even best case for this i is below target, skip
            if nums[i] + nums[n-2] + nums[n-1] < target:
                closest = nums[i] + nums[n-2] + nums[n-1]
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if abs(target - total) < abs(target - closest):
                    closest = total

                if total == target:
                    return total
                elif total < target:
                    j += 1
                else:
                    k -= 1

        return closest
