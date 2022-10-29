from collections import deque
from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
S = int(input())

adj = [[] for v in range(V+1)]
dist = [defaultdict(int) for v in range(V+1)]

for e in range(E):
    s, e, w = map(int, input().split())
    adj[s].append(e)
    if dist[s][e] == 0 or w < dist[s][e]:
        dist[s][e] = w

dijkstra = [float('inf') for v in range(V+1)]
dijkstra[S] = 0
q = []
heapq.heappush(q, [0, S])
while q:
    v = heapq.heappop(q)
    for e in adj[v[1]]:
        if dijkstra[e] > v[0] + dist[v[1]][e]:
            dijkstra[e] = v[0] + dist[v[1]][e]
            heapq.heappush(q, [dijkstra[e], e])

for v in range(1, V+1):
    if dijkstra[v] == float('inf'):
        dijkstra[v] = "INF"
    print(dijkstra[v])
    


