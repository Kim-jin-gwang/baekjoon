def RepeatStr(r:int, s:str) -> str:
    for i in s:
        print(i*int(r), end='')

t = int(input())
for i in range(t):
     r,s = input().split()
     RepeatStr(r,s)
     print()
