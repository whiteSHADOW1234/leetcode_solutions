class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one


# Readable solution
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         """
#         Returns the number of distinct ways to climb a staircase of size n, 
#         where you can climb 1 or 2 steps at a time.
#         """
#         prev_step, prev_prev_step = 1, 1
#         for i in range(n-1):
#             curr_step = prev_step + prev_prev_step
#             prev_prev_step = prev_step
#             prev_step = curr_step
#         return prev_step
