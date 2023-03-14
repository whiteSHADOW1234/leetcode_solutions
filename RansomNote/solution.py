# Simplier Way (Using Counter)
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)
        
        return all(m_counter[ch] >= r_counter[ch] for ch in r_counter)




        
# Quicker Way (Using Counter)
# from collections import Counter

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         if len(ransomNote) > len(magazine):
#             return False
        
#         r_counter = Counter(ransomNote)
#         m_counter = Counter(magazine)
        
#         for i in range(len(ransomNote)):
#             if ransomNote[i] not in magazine:
#                 return False
#             elif r_counter[ransomNote[i]] > m_counter[ransomNote[i]]:
#                 return False
#         return True



# Brute Force
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         ran =  sorted(list(ransomNote))
#         mag = sorted(list(magazine))
#         for i in mag:
#             if ran and ran[0] == i:
#                 ran.pop(0)
            
#         return not ran