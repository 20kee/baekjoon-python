N = int(input())
guilty = list(map(int, input().split()))
R = []
for n in range(N):
    R.append(list(map(int,input().split())))

EN = int(input())
remain = [1 for n in range(N)]
answer = 0
def dfs(remain, guilty, p, day):
    global answer
    if p%2 == 0: # 밤
        for n in range(N):
            if remain[n] == 1 and n != EN: # 남아있고 자기자신이 아니면
                remain[n] = 0
                for m in range(N):
                    guilty[m] += R[n][m]

                dfs(remain, guilty, p-1, day+1)
                remain[n] = 1
                for m in range(N):
                    guilty[m] -= R[n][m]
            
            
    else: # 낮
        if p == 1:
            if day > answer:
                answer = day
                return
        else:
            temp = -99999999
            candi = 0
            for n in range(N):
                if remain[n] == 1 and guilty[n] > temp:
                    temp = guilty[n]
                    candi = n
            
            if candi == EN:
                if day > answer:
                    answer = day
                return
            else:
                remain[candi] = 0
                dfs(remain, guilty, p-1, day)
                remain[candi] = 1

dfs(remain, guilty, N, 0)
print(answer)