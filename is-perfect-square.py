class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        
        while l <= r:
            mid = (l + r) // 2
            mid_square = mid * mid
            
            if num == mid_square:
                return True
            elif mid_square < num:
                l = mid + 1
            else:
                r = mid - 1
        return False #Time: O(log n), Space: O(1)
    
solution = Solution()
print(solution.isPerfectSquare(16)) # True
print(solution.isPerfectSquare(14)) # False
print(solution.isPerfectSquare(1)) # True