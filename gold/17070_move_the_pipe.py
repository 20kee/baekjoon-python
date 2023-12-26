from collections import deque
N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
def valid(r, c, i):
    if i == 0:
        c -= 1
    elif i == 1:
        r -= 1
    else:
        r -= 1
        c -= 1
    return r >= 0 and r < N and c >= 0 and c < N

for r in range(N):
    for c in range(N):
        if room[r][c] != 1:
            for i in range(3):
                if i == 0:
                    if valid(r, c-1, 0):
                        dp[r][c][0] += dp[r][c-1][0]
                    if valid(r, c-1, 2):
                        dp[r][c][0] += dp[r][c-1][2]
                elif i == 1:
                    if valid(r-1, c, 1):
                        dp[r][c][1] += dp[r-1][c][1]
                    if valid(r-1, c, 2):
                        dp[r][c][1] += dp[r-1][c][2]
                
                elif i == 2 and room[r-1][c] != 1 and room[r][c-1] != 1:
                    if valid(r-1, c-1, 0):
                        dp[r][c][2] += dp[r-1][c-1][0]
                    if valid(r-1, c-1, 1):
                        dp[r][c][2] += dp[r-1][c-1][1]
                    if valid(r-1, c-1, 2):
                        dp[r][c][2] += dp[r-1][c-1][2]

print(sum(dp[N-1][N-1]))
                
            
                