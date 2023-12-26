import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for n in range(N)]
VISITED_ALL = (1 << N) - 1

dp = [[-1 for n in range(1 << N)] for n in range(N)]
INF = float('inf')


def dfs(city, visited):
    if visited == (1 << N)-1:
        if cost[city][0] != 0:
            return cost[city][0]
        return INF
    
    if dp[city][visited] != -1:
        return dp[city][visited]
    
    t = INF
    for n in range(N):
        if visited & (1 << n) == 0 and cost[city][n] != 0:
            t = min(t, dfs(n, visited | (1 << n)) + cost[city][n])
    dp[city][visited] = t
    return t

print(dfs(0, 1))