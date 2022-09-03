N, M = map(int, input().split())
mine = []
for n in range(N):
    mine.append(list(input()))
    for m in range(M):
        mine[n][m] = int(mine[n][m])

dp = [[[0, 0, 0, 0] for m in range(M)] for n in range(N)]
dx = [-1, -1, 1, 1]
dy = [-1, 1, 1, -1]
for n in range(N):
    for m in range(M):
        if mine[n][m] == 1:
            for i in range(2):
                x = n + dx[i]
                y = m + dy[i]
                if x >= 0 and x < N and y >= 0 and y < M:
                    dp[n][m][i] = dp[x][y][i] + 1
                else:
                    dp[n][m][i] = 1

for n in range(N-1, -1, -1):
    for m in range(M-1, -1, -1):
        if mine[n][m] == 1:
            for i in range(2, 4):
                x = n + dx[i]
                y = m + dy[i]
                if x >= 0 and x < N and y >= 0 and y < M:
                    dp[n][m][i] = dp[x][y][i] + 1
                else:
                    dp[n][m][i] = 1

answer = 0
for n in range(N):
    for m in range(M):
        if mine[n][m] == 1:
            # 왼쪽 꼭짓점
            l = min(dp[n][m][2], dp[n][m][1])
            for i in range(answer+1, l+1):
                y = m+(i-1)*2
                if y < M:
                    if min(dp[n][y][0], dp[n][y][3]) >= i:
                        answer = i
                else:
                    break

print(answer)


        

                    
