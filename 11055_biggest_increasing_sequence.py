N = int(input())
lst = list(map(int, input().split()))
ans = 0
dp = [0 for n in range(N)] # lst[:i] 에서 가장 큰 증가 부분 수열의 합
for n in range(N):
    max = 0
    for m in range(n):
        if dp[m] > max and lst[m] < lst[n]:
            max = dp[m]
    
    dp[n] = max + lst[n]
    if dp[n] > ans:
        ans = dp[n]
    
print(ans)
