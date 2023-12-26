def getDP(n, m, i):
    global c
    if dp[n][m][i] != -1:
        return dp[n][m][i]
    
    if i != 0:
        dp[n][m][i] = 0

    for x in range(N):
        for y in range(M):
            if ( (abs(x-n)>= 2 and abs(y-m) >= 3) or (abs(x-n)>= 3 and abs(y-m) >= 2) ) and chess[x][y] == answer[i-1]:
                dp[n][m][i] += getDP(x, y, i-1)
    
    dp[n][m][i] %= 1000000007
    return dp[n][m][i]
c = 0
N, M, L = map(int, input().split())
answer = list(input())
chess = [list(input()) for _ in range(N)]
dp = [ [ [-1]*len(answer) for _ in range(M)] for _ in range(N)]
for n in range(N):
    for m in range(M):
        if chess[n][m] == answer[0]:
            dp[n][m][0] = 1

length = len(answer)
total = 0
for n in range(N):
    for m in range(M):
        if chess[n][m] == answer[length-1]:
            total += getDP(n, m, length-1)

print(total % 1000000007)
            
        