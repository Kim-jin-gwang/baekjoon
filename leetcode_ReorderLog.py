class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter, digit = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        
        letter.sort(key=lambda x:(x.split()[1:], x.split()[0]))

        return letter + digit

        

result = Solution()
logs = []
n = int(input())
for i in range(n):
    logs.append(input())

print(result.reorderLogFiles(logs))
