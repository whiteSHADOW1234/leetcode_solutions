from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid +1
            else:
                return mid
        return -1




# A more clear solution

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2

#             # if the middle element is the target, return its index
#             if nums[mid] == target:
#                 return mid

#             # if the middle element is greater than the target, search the left half
#             if nums[mid] > target:
#                 right = mid - 1

#             # if the middle element is less than the target, search the right half
#             else:
#                 left = mid + 1

#         # if the target was not found, return -1
#         return -1
