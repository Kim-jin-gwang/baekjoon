def Dial(s:str) -> int:
    result = 0
    check = ['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    
    for i in s:
        flag = 3
        for j in check:
            if i in j:
                result+=flag
                break
            else:
                flag+=1
    
    return result

s = input()
print(Dial(s))