def Constant(a:int, b:int) -> str:
    result_a = ''.join(list(a)[::-1])
    result_b = ''.join(list(b)[::-1])
    return max(result_a,result_b)

a,b = input().split()
result = Constant(a,b)
print(result)