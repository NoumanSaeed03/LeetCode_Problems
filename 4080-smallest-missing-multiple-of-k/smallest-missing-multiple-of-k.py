class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        present = [False] * 101
        
        for num in nums:
            present[num] = True
            
        current_multiple = k
        
        while current_multiple <= 100:
            if not present[current_multiple]:
                return current_multiple
            current_multiple += k
            
        return current_multiple