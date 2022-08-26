from collections import deque

N, S, E, M = map(int, input().split())
lst = []
adj = [[] for n in range(N)]
for m in range(M):
    lst.append(list(map(int, input().split())))
    adj[lst[m][0]].append(lst[m][1])

profit = list(map(int, input().split()))
for m in range(M):
    lst[m][2] -= profit[lst[m][1]]
    

lst.sort()
dist = [1000000000 for n in range(N)]
dist[S] = -profit[S]
temp = False
a = []
for n in range(N):
    for m in range(M):
        s = lst[m][0]
        e = lst[m][1]
        cost = lst[m][2]
        if dist[s] != 1000000000 and dist[e] > dist[s] + cost:
            dist[e] = dist[s] + cost
            if n == N-1:
                a.append(e)

visited = [0 for n in range(N)]
for e in a:
    if visited[e] == 0:
        q = deque([e])
        while q:
            v = q.popleft()
            if visited[v] == 0:
                visited[v] = 1
                for d in adj[v]:
                    q.append(d)
if visited[E] == 1:
    temp = True

if dist[E] == 1000000000:
    print("gg")
else:
    if temp:
        print("Gee")
    else:
        print(-dist[E])



