def CountWord(s:str) -> int:
    result = s.split()
    return len(result)


s = input()
print(CountWord(s))