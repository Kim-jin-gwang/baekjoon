def FindAlpabat(s:str) -> list:
    check = 'abcdefghijklmnopqrstuvwxyz'
    for i in check:
        if i in s:
            print(s.index(i), end=' ')
        else:
            print(-1, end=' ')

s = input()
FindAlpabat(s)