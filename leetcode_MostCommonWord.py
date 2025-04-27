import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^\w]',' ',paragraph)
        words = paragraph.split()
        for i in banned:
            while i in words:
                words.remove(i)
        count_words = Counter(words)
        return count_words.most_common(n=1)[0][0]

result = Solution()
paragraph = input()
banned = []
n = int(input())
for i in range(n):
    banned.append(input())

print(result.mostCommonWord(paragraph, banned))