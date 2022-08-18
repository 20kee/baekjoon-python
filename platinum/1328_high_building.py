N, L, R = map(int, input().split())


dp = [[[0 for r in range(N+1)] for l in range(N+1)] for n in range(N+1)]

dp[1][1][1] = 1
for n in range(2, N+1):
    for l in range(1, n+1):
        for r in range(1, n+1):
            dp[n][l][r] = (dp[n-1][l-1][r] + dp[n-1][l][r-1] + dp[n-1][l][r] * (n-2)) % 1000000007

print(dp[N][L][R])