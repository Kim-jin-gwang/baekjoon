import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        counts = Counter(words)
        return counts.most_common(n=1)[0][0]

result = Solution()
paragraph = input()
banned = []
n = int(input())
for i in range(n):
    banned.append(input())

print(result.mostCommonWord(paragraph, banned))