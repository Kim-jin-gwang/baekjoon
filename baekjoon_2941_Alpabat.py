def Alpabat(s:str) -> int:
    check = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    for i in check:
        if i in s:
            s=s.replace(i,'*')
    return len(s)

s = input()
result = Alpabat(s)
print(result)