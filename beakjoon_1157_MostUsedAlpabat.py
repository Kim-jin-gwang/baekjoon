def MostUsedAlpabat(s:str) -> str:
    s = s.upper()
    check_s = list(set(s))
    cnt = []
    for i in check_s:
        count = s.count(i)
        cnt.append(count)
    if cnt.count(max(cnt)) >=2:
        return '?'
    else:
        return check_s[cnt.index(max(cnt))]
    

s = input()
result = MostUsedAlpabat(s)
print(result)