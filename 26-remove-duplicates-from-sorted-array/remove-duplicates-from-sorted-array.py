class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low = 1
        
        for high in range(1, len(nums)):
            if nums[high] != nums[high - 1]:
                nums[low] = nums[high]
                low += 1
                
        return low