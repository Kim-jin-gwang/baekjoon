from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())



result = Solution()
n = int(input())
strs = []

for i in range(n):
    strs.append(input())
print(result.groupAnagrams(strs))