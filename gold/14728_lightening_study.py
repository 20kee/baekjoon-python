N, T = map(int, input().split())
chapters = []
for _ in range(N):
    chapters.append(list(map(int, input().split())))
dp = [[0]*(T+1) for _ in range(N)]
for n in range(N):
    for t in range(1, T+1):
        if n == 0:
            if t >= chapters[n][0]:
                dp[n][t] = chapters[n][1]
        else:
            dp[n][t] = dp[n-1][t]
            if t-chapters[n][0] >= 0:
                dp[n][t] = max(dp[n][t], dp[n-1][t-chapters[n][0]] + chapters[n][1])

print(dp[-1][-1])
