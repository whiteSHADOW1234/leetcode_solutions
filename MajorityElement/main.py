from solution import Solution

# Create an instance of the Solution class
sol = Solution()

# Example input: a list of integers
nums = [1, 2, 2, 2, 3, 4, 2]

# Call the majorityElement method on the instance of the Solution class
majority = sol.majorityElement(nums)

# Print the result
print("The majority element in the list", nums, "is:", majority)
