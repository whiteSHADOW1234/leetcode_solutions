from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize dictionary to store seen values and their indices
        seen = {}
        
        for i, num in enumerate(nums):
            # Compute the value that, when added to num, equals target
            complement = target - num
            
            # Check if the complement has been seen before
            if complement in seen:
                return [seen[complement], i]
            
            # Store the current value and index in the dictionary
            seen[num] = i
        
        # If no solution is found, return an empty list
        return []