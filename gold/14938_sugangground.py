import heapq
N, M, R = map(int, input().split())
items = list(map(int, input().split()))
adj = [[] for _ in range(N+1)]
dist = [[0 for _ in range(N+1)] for _ in range(N+1)]
dijkstra = [[1000000000 for _ in range(N+1)] for _ in range(N+1)]
for r in range(R):
    a, b, c = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    dist[a][b] = c
    dist[b][a] = c

answer = 0
for s in range(1, N+1):
    dijkstra[s][s] = 0
    q = []
    heapq.heappush(q, (s, 0))
    while q:
        v, c = heapq.heappop(q)
        if c > dijkstra[s][v]:
            continue

        for e in adj[v]:
            new_dist = dijkstra[s][v] + dist[v][e]
            if new_dist < dijkstra[s][e]:
                dijkstra[s][e] = new_dist
                heapq.heappush(q, (e, dijkstra[s][e]))
    temp = 0
    for i, d in enumerate(dijkstra[s]):
        if d <= M:
            temp += items[i-1]
    if temp > answer:
        answer = temp


print(answer)