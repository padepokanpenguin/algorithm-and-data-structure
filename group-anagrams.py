class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        
        for s in strs:
            key = tuple(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        return list(anagrams.values()) #Time: O(n * k log k), Space: O(n * k)
    
solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
print(solution.groupAnagrams(["cat", "tac", "dog", "god", "act"])) # [["cat", "tac", "act"], ["dog", "god"]]