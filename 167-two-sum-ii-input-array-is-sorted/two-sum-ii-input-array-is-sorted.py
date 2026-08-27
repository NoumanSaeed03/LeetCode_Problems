class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 1
        high = len(numbers)

        while low <= high:
            current_sum = numbers[low - 1] + numbers[high - 1]
            if current_sum == target:
                return [low,high]
            elif current_sum > target:
                high -= 1
            else:
                low +=1

        return []