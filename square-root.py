# Give a non-negative integer x, compute and return the square root of x.
# return the square root of x rounded down to the nearest integer
# The returned integer should be non-negative as well
# Must not use any built-in square root function or operator

class Solution:
    # def mySqrt(self, x: int) -> int:
    #      int(x ** 0.5)
         
    def mySqrt(self, x: int) -> int:
         L, R = 1, x
         
         while L <= R:
             M = (L + R) // 2
             M_squared = M * M
             
             if M_squared == x:
                 return M
             elif M_squared < x:
                 L = M + 1
             else:
                R = M - 1
         return R
     

solution = Solution()
print(solution.mySqrt(4))