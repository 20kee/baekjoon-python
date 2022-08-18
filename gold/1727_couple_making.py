N, M = map(int, input().split())
men = list(map(int, input().split()))
women = list(map(int, input().split()))
men.sort()
women.sort()
dp = [[0 for m in range(M)] for n in range(N)]
for n in range(N):
    for m in range(M):
        try:
            dp[n][m] = dp[n-1][m-1] + abs(men[n] - women[m])
        except:
            dp[n][m] = abs(men[n] - women[m])
        if n > m:
            dp[n][m] = min(dp[n][m], dp[n-1][m])
        elif n < m:
            dp[n][m] = min(dp[n][m], dp[n][m-1])

print(dp[N-1][M-1])
