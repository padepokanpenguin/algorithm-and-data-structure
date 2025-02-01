# example 1
# input: arr = [1, 2, 2, 1, 1, 3]
# output: true
# explanation: the value 1 has 3 occurrences, 2 has 2 occurrences, and 3 has 1 occurrence. No two values have the same number of occurrences.

# example 2
# input: arr = [1, 2]
# output: false

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counter = Counter(arr)
        s = set()
        
        for value in counter.values():
            if value in s:
                return False
            else:
                s.add(value)
        return True
    
solution = Solution()
print(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3])) # True
print(solution.uniqueOccurrences([1, 2])) # False