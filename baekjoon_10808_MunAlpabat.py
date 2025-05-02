
result = [0] * 26
s = input()
for i in s:
    check = ord(i)-97
    result[check] += 1

for i in result:
    print(i, end=' ')