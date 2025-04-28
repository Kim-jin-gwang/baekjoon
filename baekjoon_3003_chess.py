def Chess(parts:list) -> list:
    check = [1,1,2,2,2,8]
    result =[0] * 6
    for i in range(len(parts)):
        print(check[i] - parts[i], end=' ')



parts = list(map(int, input().split()))
Chess(parts)