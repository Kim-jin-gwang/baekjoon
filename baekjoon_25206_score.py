

total_grade, result = 0, 0
score ={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,
        'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}

for _ in range(20):
    s,p,g = input().split()  #과목, 학점, 등급
    p = float(p)
    if g != 'P':
        total_grade += p
        result += p * score[g]

print('%.6f' % (result/total_grade))