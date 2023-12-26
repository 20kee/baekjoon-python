N = int(input())
price = [list(map(int, list(input()))) for n in range(N)]

dp = [[[-1 for n in range(1<<N)] for n in range(10)] for n in range(N)]

def dfs(n, p, visited):
    if dp[n][p][visited] != -1:
        return dp[n][p][visited]

    t = -1
    for i in range(N):
        if price[n][i] >= p and visited & (1 << i) == 0:
            t = max(t, dfs(i, price[n][i], visited | (1 << i)))
    if t == -1:
        t = 1
    dp[n][p][visited] = t
    return t+1
        
dfs(0, 0, 1 << 0)
print(max(dp[0][0]))