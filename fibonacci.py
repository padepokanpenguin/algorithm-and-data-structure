class Solution:
    # def fibonacci(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     else:
    #         return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def fibonacci(self, n: int) -> int:
        answer = [0, 1]
        
        for i in range(2, n + 1):
            answer.append(answer[i - 1] + answer[i - 2])
        return answer[n]

solution = Solution()
print(solution.fibonacci(2)) # 1
print(solution.fibonacci(3)) # 2
print(solution.fibonacci(4)) # 3  
print(solution.fibonacci(5)) # 5
print(solution.fibonacci(6)) # 8