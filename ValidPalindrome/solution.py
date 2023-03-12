# No build-in function or import any library Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alnum(s[l]):
                l += 1
            while r > l and not self.alnum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        
        return True

    def alnum(self, c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        






# Solution with build-in function
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
#         while l < r:
#             while l < r and not s[l].isalnum():
#                 l += 1
#             while l < r and not s[r].isalnum():
#                 r -= 1
            
#             if s[l].lower() != s[r].lower():
#                 return False
#             l, r = l + 1, r - 1

#         return True





# Solution with import re
# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = re.sub('[^0-9a-zA-Z]', '', s).lower()
#         return s == s[::-1]
        