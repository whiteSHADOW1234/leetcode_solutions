class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}

        if len(s) == 1:
            return 1


        for char in s:
            letters[char] = letters.get(char, 0) + 1

        total = 0
        maxodd = 0

        for b in letters.values():
            if b%2 == 0:
                total += b
            else:
                total += (b - 1)
                maxodd = 1

        return total + maxodd

# Build-in Function Version
# from collections import defaultdict

# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         letters = defaultdict(int)

#         if len(s) == 1:
#             return 1

#         for char in s:
#             letters[char] += 1

#         total = 0
#         maxodd = 0

#         for b in letters.values():
#             if b % 2 == 0:
#                 total += b
#             else:
#                 total += (b - 1)
#                 maxodd = 1

#         return total + maxodd





# Simplified Version
# from collections import defaultdict

# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         letters = defaultdict(int)

#         if len(s) == 1:
#             return 1

#         for char in s:
#             letters[char] += 1

#         total = 0
#         maxodd = 0

#         for b in letters.values():
#             if b % 2 == 0:
#                 total += b
#             else:
#                 total += (b - 1)
#                 maxodd = 1

#         return total + maxodd if maxodd else total

