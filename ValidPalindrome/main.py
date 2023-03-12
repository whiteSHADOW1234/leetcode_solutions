from solution import Solution

# Test the solution
s = Solution()

input_str = "A man, a plan, a canal: Panama"
print(s.isPalindrome(input_str))  # expected output: True

input_str = "race a car"
print(s.isPalindrome(input_str))  # expected output: False
