t = int(input())
for _ in range(t):
    result = 0
    cnt = 0
    quiz = list(input())

    for i in range(len(quiz)):
        if quiz[i] == 'X':
            cnt = 0
        elif quiz[i] == 'O':
            cnt+=1
        result += cnt
    
    print(result)