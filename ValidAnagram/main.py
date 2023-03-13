from solution import Solution

# create an instance of the Solution class
sol = Solution()

# test the isAnagram method
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t)) # output: True

s = "rat"
t = "car"
print(sol.isAnagram(s, t)) # output: False
