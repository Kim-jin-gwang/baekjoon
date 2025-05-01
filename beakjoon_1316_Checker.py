
n = int(input())
cnt = n
for _ in range(n):
    group = input()
    for i in range(len(group)-1):
        if group[i] == group[i+1]:
            pass
        elif group[i] in group[i+1:]:
            cnt-=1
            break

print(cnt)