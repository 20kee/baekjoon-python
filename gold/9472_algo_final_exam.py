T = int(input())
dp = [[0 for n in range(18)] for n in range(18)]
dp[1][0] = 1
for n in range(2, 18):
    dp[n][0] = dp[n-1][0] * n

for n in range(2, 18):
    for m in range(1, 18):
        if m <= n:
            if m == 1:
                dp[n][m] = dp[n-1][m-1]*(n-1)
            else:
                dp[n][m] = dp[n-1][m-2]*(m-1) + dp[n-1][m-1]*(n-m)

answer = [0 for t in range(T)]
for t in range(T):
    c, N, k = map(int, input().split())
    answer[c-1] = dp[N][k]

for t in range(T):
    print(t+1, answer[t])
    