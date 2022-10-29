from collections import defaultdict
import heapq

N, M, K = map(int, input().split())

adj = [[] for n in range(N+1)]
dist = [defaultdict(int) for n in range(N+1)]

for m in range(M):
    s, e, w = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
    if dist[s][e] == 0 or dist[s][e] > w:
        dist[s][e] = w
        dist[e][s] = w

dijkstra = [[50000000001 for n in range(K+1)] for k in range(N+1)]
before = [0 for n in range(N+1)]
dijkstra[1][0] = 0
q = []
cnt = 0
heapq.heappush(q, [0, 1, 0])
while q:
    w, v, c = heapq.heappop(q)
    if dijkstra[v][c] < w:
        continue
    for e in adj[v]:
        if dijkstra[e][c] > w + dist[v][e]:
            dijkstra[e][c] = w + dist[v][e]
            heapq.heappush(q, [dijkstra[e][c], e, c])
        if c < K:
            if dijkstra[e][c+1] > w:
                dijkstra[e][c+1] = w
                heapq.heappush(q, [dijkstra[e][c+1], e, c+1])

print(min(dijkstra[N]))

