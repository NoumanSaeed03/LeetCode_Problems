class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        seen = {}
        k = 0
        for i in range(n):
            if nums[i] not in seen:
                seen[nums[i]] = 1
                nums[k] = nums[i]
                k += 1
        return k