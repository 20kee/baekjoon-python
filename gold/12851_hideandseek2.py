from collections import deque
N, K = map(int, input().split())
visited = [False for n in range(100001)]
dp = [100000 for n in range(100001)]
count = [0 for n in range(100001)]

if N == K:
    count[K] = 1
min = 100001
q = deque([[N, 0]])
visited[N] = True
dp[N] = 0
while q:
    v = q.popleft()
    if v[0]-1 >= 0:
        if v[1]+1 < dp[v[0]-1]:
            dp[v[0]-1] = v[1]+1
            count[v[0]-1] = 1
            q.append([v[0]-1, v[1]+1])

        elif v[1]+1 == dp[v[0]-1]:
            count[v[0]-1] += 1
            q.append([v[0]-1, v[1]+1])
        
        
        
    if v[0]+1 <= 100000:
        if v[1]+1 < dp[v[0]+1]:
            dp[v[0]+1] = v[1]+1
            count[v[0]+1] = 1
            q.append([v[0]+1, v[1]+1])

        elif v[1]+1 == dp[v[0]+1]:
            count[v[0]+1] += 1
            q.append([v[0]+1, v[1]+1])

    if v[0]*2 <= 100000:
        if v[1]+1 < dp[v[0]*2]:
            dp[v[0]*2] = v[1]+1
            count[v[0]*2] = 1
            q.append([v[0]*2, v[1]+1])

        elif v[1]+1 == dp[v[0]*2]:
            count[v[0]*2] += 1
            q.append([v[0]*2, v[1]+1])

print(dp[K])
print(count[K])
    

    