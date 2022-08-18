from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    M, N = map(int, input().split())
    con = []

    if N == 0:
        break
    
    for n in range(N):
        con.append(list(map(int, input().split())))
    
    count = 0
    q = deque([])
    for n in range(N):
        for m in range(M):
            if con[n][m] == 1:
                con[n][m] = 0
                count += 1
                q.append([n, m])
                while q:
                    v = q.popleft()
                    for i in range(8):
                        x = v[0] + dx[i]
                        y = v[1] + dy[i]
                        if x >= 0 and x < N and y >= 0 and y < M:
                            if con[x][y] == 1:
                                con[x][y] = 0
                                q.append([x, y])
    
    print(count)

                        
    