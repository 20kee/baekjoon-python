T = int(input())
for t in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [[0 for n in range(N)] for m in range(M+1)]
    dp[0] = [1 for n in range(N)]
    for m in range(1, M+1):
        for n in range(N):
            coin = coins[n]
            if coin <= m:
                dp[m][n] += dp[m-coin][n]
            if n > 0:
                dp[m][n] += dp[m][n-1]
    print(dp[M][N-1])
            

            
