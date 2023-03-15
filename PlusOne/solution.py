from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert the list of digits to a single integer
        num = 0
        for digit in digits:
            num = num * 10 + digit
        
        # Add 1 to the integer and convert it back to a list of digits
        num += 1
        result = []
        while num > 0:
            digit = num % 10
            result.insert(0, digit)
            num //= 10
        
        return result



# Using the built-in functions
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         return [int(x) for x in str(int("".join(map(str, digits))) + 1)]