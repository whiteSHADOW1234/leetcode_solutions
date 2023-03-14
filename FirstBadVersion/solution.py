from isBadVersion import isBadVersion

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
        return left


# Simplier Binary Search
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         start, end = 0, n
#         while start < end:
#             mid = start + (end - start)//2
#             if isBadVersion(mid):
#                 end = mid
#             else:
#                 start = mid + 1
#         return start



# Remove useless API calls
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         left, right = 1, n
#         if isBadVersion(1):
#             return 1
#         while left < right:
#             mid = left + (right - left) // 2
#             if isBadVersion(mid):
#                 right = mid
#             else:
#                 left = mid + 1
#         return left

