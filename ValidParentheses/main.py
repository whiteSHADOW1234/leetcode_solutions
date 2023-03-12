from solution import Solution

# Create an instance of the Solution class
sol = Solution()

# Test the isValid() function with different input strings
print(sol.isValid("()[]{}"))  # Expected output: True
print(sol.isValid("([)]"))    # Expected output: False
print(sol.isValid("{[]}"))    # Expected output: True
