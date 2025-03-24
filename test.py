def star(n:int):
    for i in range(n):
        print(" "*(n-i-1)+"*"*(i+1))

n = int(input())
star(n)