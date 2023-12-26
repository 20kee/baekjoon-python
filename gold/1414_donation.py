import heapq

def stoi(s):
    if s == '0':
        return 0
    if ord(s) >= 97:
        return ord(s)-96
    else:
        return ord(s)-38

def find(u):
    if parent[u] == u:
        return u

    return find(parent[u])

def union(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        if u >= v:
            parent[u] = v
        else:
            parent[v] = u
    

    


def MST(heap, N):
    visited = [False for n in range(N)]
    cost = 0
    count = 0
    while heap:
        v = heapq.heappop(heap)
        s, e = v[1], v[2]
        if find(s) != find(e):
            cost += v[0]
            count += 1
            union(s, e)
    if count != N-1:
        return -1
    return cost

        

N = int(input())
parent = [n for n in range(N)]
total = 0
adj = [[] for n in range(N)]
dist = [[0 for n in range(N)] for n in range(N)]
heap = []
answer = 0
for n in range(N):
    edges = list(map(stoi, list(input())))
    for m in range(N):
        if n == 0 and m == 0:
            answer = edges[0]
        total += edges[m]
        if edges[m] != 0:
            if n != m:
                heapq.heappush(heap, [edges[m], n, m])

cost = MST(heap, N)

if N == 1:
    print(answer)
else:
    if cost == -1:
        print(-1)
    else:
        print(total-cost)

    