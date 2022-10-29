import heapq
N, K = map(int, input().split())
visited = [False] * 100001
answer = 0
q = []
heapq.heappush(q, [0, N])
visited[N] = True
while q:
    v = heapq.heappop(q)
    if v[1] == K:
        answer= v[0]
        break

    e = v[1]*2
    while e <= 100000 and not(visited[e]):
        heapq.heappush(q, [v[0], e])
        visited[e] = True
        e = e*2

    if v[1]-1 >= 0 and not(visited[v[1]-1]):
        heapq.heappush(q, [v[0]+1, v[1]-1])
        visited[v[1]-1] = True
    if v[1]+1 <= 100000 and not(visited[v[1]+1]):
        heapq.heappush(q, [v[0]+1, v[1]+1])
        visited[v[1]+1] = True
    
    
        
print(answer)