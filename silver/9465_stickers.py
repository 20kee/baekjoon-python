T = int(input())
for t in range(T):
    N = int(input())
    lst = []
    lst.append(list(map(int, input().split())))
    lst.append(list(map(int, input().split())))
    
    dp = [[0 for n in range(N)] for n in range(2)] # 이 위치의 스티커를 골랐을 때와 고르지 않았을 때 각각의 최댓값
    dp[0][0] = lst[0][0]
    dp[1][0] = lst[1][0]

    if N >= 2:
        dp[0][1] = lst[1][0] + lst[0][1]
        dp[1][1] = lst[0][0] + lst[1][1]
    
    for n in range(2, N):
        dp[0][n] = max(dp[1][n-1], dp[1][n-2]) + lst[0][n]
        dp[1][n] = max(dp[0][n-1], dp[0][n-2]) + lst[1][n]
    
    print(max(dp[0][-1], dp[1][-1]))
    
    
    

