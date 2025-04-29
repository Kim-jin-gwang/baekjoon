def IsPalindrome(s:str) -> bool:
    check = list(s)
    reverse_check = list(reversed(check))
    if check == reverse_check:
        return 1
    else:
        return 0

s= input()
result = IsPalindrome(s)
print(result)