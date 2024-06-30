N = int(input())

dp = [False for _ in range(N+5)]
dp[0] = False
dp[1] = True
dp[2] = False
dp[3] = True
for i in range(4, N+1):
    dp[i] = True if dp[i-1] == False or dp[i-3] == False else False

print('SK' if dp[N] == True else 'CY')  