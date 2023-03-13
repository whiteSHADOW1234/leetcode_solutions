class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True




# Solution without building two dictionaries
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         count = {}
#         for c in s:
#             count[c] = count.get(c, 0) + 1
        
#         for c in t:
#             if c not in count:
#                 return False
#             count[c] -= 1
#             if count[c] == 0:
#                 del count[c]
        
#         return not count







# Using build-in function to achieve the same result
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)




# Sorted Way using build-in function
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)