from collections import defaultdict
import heapq

import sys
input = sys.stdin.readline

N, E = map(int, input().split())

adj = [[] for n in range(N+1)]
dist = [defaultdict(int) for n in range(N+1)]

for e in range(E):
    s, e, w = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
    dist[s][e] = w
    dist[e][s] = w

F, S = map(int, input().split())

dijkstra = [[float("inf") for v in range(N+1)] for i in range(3)]

nodes = [1, F, S]
for i in range(3):
    q = []
    heapq.heappush(q, [0, nodes[i]])
    dijkstra[i][nodes[i]] = 0

    while q:
        v = heapq.heappop(q)
        for e in adj[v[1]]:
            if dijkstra[i][e] > v[0] + dist[v[1]][e]:
                dijkstra[i][e] = v[0] + dist[v[1]][e]
                heapq.heappush(q, [dijkstra[i][e], e])
    
answer = min(dijkstra[0][F] + dijkstra[1][S] + dijkstra[2][N], dijkstra[0][S] + dijkstra[2][F] + dijkstra[1][N])
if answer >= float('inf'):
    answer = -1
print(answer)