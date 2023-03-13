from solution import Solution

# create an instance of the Solution class
sol = Solution()

# test the search method
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(sol.search(nums, target)) # output: 4

target = 2
print(sol.search(nums, target)) # output: -1

nums = [5]
target = 5
print(sol.search(nums, target)) # output: 0
