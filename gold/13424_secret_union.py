from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    friends = []
    dijkstra = [[1000000 for n in range(N+1)] for n in range(N+1)]
    dist = [[0 for n in range(N+1)] for n in range(N+1)]
    adj = [[] for n in range(N+1)]
    for m in range(M):
        a, b, c = map(int, input().split())
        dist[a][b] = c
        dist[b][a] = c
        adj[a].append(b)
        adj[b].append(a)

    K = int(input())
    friends = list(map(int, input().split()))
    
    for n in range(N+1):
        dijkstra[n][n] = 0
        q = deque([n])
        while q:
            o = q.popleft()
            for d in adj[o]:
                if dist[o][d] + dijkstra[n][o] < dijkstra[n][d]:
                    dijkstra[n][d] = dist[o][d] + dijkstra[n][o]
                    q.append(d)

    min = 100000000
    answer = 0
    for n in range(1, N+1):
        temp = 0
        for friend in friends:
            temp += dijkstra[n][friend]
        
        if temp < min:
            min = temp
            answer = n

    print(answer)

            


        