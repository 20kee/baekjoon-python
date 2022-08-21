import math

def shortcut(dp, n, m):
    global X, Y, N, M, visit
    if m == M or visit[n][m] == 1:
        return dp[n][m]

    visit[n][m] = 1

    t1 = 1000000000
    t2 = 1000000000
    t3 = 1000000000 #없애고 가기
    t4 = 1000000000 #길대로 가기
    if rows[m] == n-1:
        t3 = shortcut(dp, n, m+1) + X
        t4 = shortcut(dp, n-1, m+1)
    elif rows[m] == n:
        t3 = shortcut(dp, n, m+1) + X
        t4 = shortcut(dp, n+1, m+1)
    else:
        t4 = shortcut(dp, n, m+1)

    if n > 0 and visit[n-1][m] == 0:
        t1 = shortcut(dp, n-1, m) + Y

    if n < N-1 and visit[n+1][m] == 0:
        t2 = shortcut(dp, n+1, m) + Y

    dp[n][m] = min(t1, t2, t3, t4)
    return dp[n][m]

N, M = map(int, input().split())
a, b, X, Y = map(int, input().split())
a -= 1
b -= 1

rows = []
for m in range(M):
    rows.append(int(input())-1)

dp = [[-1 for m in range(M+1)] for n in range(N)]
for n in range(N):
    dp[n][M] = abs(n-b) * Y
visit = [[0 for m in range(M+1)] for n in range(N)]

shortcut(dp, a, 0)
print(dp[a][0])


