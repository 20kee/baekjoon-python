import copy
N = int(input())
cost = list(map(int, input().split()))
M = int(input())
dp = [[[] for n in range(N)] for m in range(M+1)]
for m in range(1, M+1):
    for n in range(N):
        if m < cost[n]:
            if n != 0:
                dp[m][n] = dp[m][n-1]

        else:
            if n == 0:
                dp[m][n] = dp[m-cost[n]][n] + [str(n)]
            else:
                if dp[m][n-1] == list():
                    dp[m][n] = dp[m-cost[n]][n] + [str(n)]
                else:
                    t1 = int("".join(copy.deepcopy(dp[m][n-1])))
                    t2 = dp[m-cost[n]][n] + [str(n)]
                    t2.sort(reverse=True)
                    t2 = int("".join(t2))
                    t3 = int("".join([str(n)] + dp[m-cost[n]][0]))

                    if t1 >= t2 and t1 >= t3:
                        dp[m][n] = dp[m][n-1]
                    elif t2 >= t1 and t2 >= t3:
                        dp[m][n] = dp[m-cost[n]][n] + [str(n)]
                    else:
                        dp[m][n] = [str(n)] + dp[m-cost[n]][0]

        dp[m][n].sort(reverse=True)
print(int("".join(dp[M][N-1])))
            

