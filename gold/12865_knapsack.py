N, K = map(int, input().split())
stock = [[0, 0]]
for n in range(N):
    stock.append(list(map(int, input().split())))

dp = [[0 for k in range(K + 1)] for n in range(N + 1)]

my_max = 0
for n in range(N + 1):
    for k in range(K + 1):
        if stock[n][0] > k:
            dp[n][k] = dp[n - 1][k]
        else:
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - stock[n][0]] + stock[n][1])

        if dp[n][k] > my_max:
            my_max = dp[n][k]

print(my_max)
