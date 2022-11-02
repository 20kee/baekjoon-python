import heapq
N, M = map(int, input().split())
adj = [[] for n in range(N+1)]
distance = [[0 for n in range(N+1)] for n in range(N+1)]
for m in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for n in range(1, N+1):
    dijkstra = [float('inf') for n in range(N+1)]
    dijkstra[0] = 0
    dijkstra[n] = 0
    q = []
    heapq.heappush(q, [0, n])
    while q:
        v = heapq.heappop(q)
        for e in adj[v[1]]:
            if dijkstra[e] > v[0] + 1:
                dijkstra[e] = v[0] + 1
                heapq.heappush(q, [dijkstra[e], e])

    distance[n] = dijkstra

answer = [float('inf'), N]
for n in range(N, 0, -1):
    s = sum(distance[n])
    if s <= answer[0]:
        answer[0] = s
        answer[1] = n
print(answer[1])