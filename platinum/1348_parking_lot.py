from collections import deque

N, M = map(int, input().split())
park = []
cars = []
lots = []
cari = [[-1 for m in range(M)] for n in range(N)]
loti = [[-1 for m in range(M)] for n in range(N)]
for n in range(N):
    park.append(list(input()))
    for m in range(M):
        if park[n][m] == "C":
            cars.append([n, m])
            cari[n][m] = len(cars)-1
        elif park[n][m] == "P":
            lots.append([n, m])
            loti[n][m] = len(lots)-1


dist = [[0 for m in range(len(lots))] for n in range(len(cars))]
adjc = [[] for n in range(len(cars))]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for n in range(len(cars)):
    visited = [[0 for m in range(M)] for n in range(N)]
    q = deque([[cars[n], 0]])
    while q:
        v = q.popleft()
        visited[v[0][0]][v[0][1]] = 1
        for i in range(4):
            x = v[0][0] + dx[i]
            y = v[0][1] + dy[i]
            if x >= 0 and x < N and y >= 0 and y < M:
                if park[x][y] != "X":
                    if visited[x][y] == 0:
                        visited[x][y] = 1
                        if park[x][y] == "P":
                            adjc[n].append(loti[x][y])
                            dist[n][loti[x][y]] = v[1]+1
                        q.append([[x, y], v[1]+1])

def bimatch(n, m):
    if visited[n]:
        return False
    visited[n] = True
    for e in adjc[n]:
        if dist[n][e] <= m:
            if selected[e] == -1 or bimatch(selected[e], m):
                selected[e] = n
                return True
    return False
   
while True:
    s, e = 0, 10000
    while s < e:
        m = (s+e) // 2
        selected = [-1 for m in range(len(lots))]
        for n in range(len(cars)):
            visited = [False for c in range(len(cars))]
            bimatch(n, m)
        result = 0
        for n in range(len(lots)):
            if selected[n] >= 0:
                result += 1
        
        if result != len(cars):
            s = m+1
        else:
            e = m
    break

if e == 10000:
    print(-1)
else:
    print(e)


