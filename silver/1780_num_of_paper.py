import sys
input = sys.stdin.readline

N = int(input())
paper = []
for n in range(N):
    paper.append(list(map(int, input().split())))

def counting(paper, N):
    re = [0, 0, 0]

    if N == 1:
        re[paper[0][0]] += 1
        return re
    
    ans = paper[0][0]
    t = True
    for n in range(N):
        for m in range(N):
            if paper[n][m] != ans:
                t = False
                break
        if t == False:
            break
    if t:
        re[ans] += 1
        return re
    
    else:
        row = [0, N//3, (N//3)*2, N]
        for n in range(3):
            for m in range(3):
                ret = counting([r[row[m]:row[m+1]] for r in paper[row[n]:row[n+1]]], row[1])
                for i in range(3):
                    re[i] += ret[i]
        return re

ans = counting(paper, N)
print(ans[-1])
print(ans[0])
print(ans[1])

        

    
        