from collections import deque

N = int(input())
D = []
for n in range(N):
    D.append(list(input()))
visited = [[False for n in range(N)] for n in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer1 = 0
for n in range(N):
    for m in range(N):
        if not (visited[n][m]):
            answer1 += 1
            q = deque([[n, m]])
            color = D[n][m]
            while q:
                v = q.popleft()
                if not (visited[v[0]][v[1]]):
                    visited[v[0]][v[1]] = True
                    for i in range(4):
                        x = v[0] + dx[i]
                        y = v[1] + dy[i]
                        if x >= 0 and x < N and y >= 0 and y < N:
                            if not (visited[x][y]) and D[x][y] == color:
                                q.append([x, y])

for n in range(N):
    for m in range(N):
        if D[n][m] == "G":
            D[n][m] = "R"

visited = [[0 for n in range(N)] for n in range(N)]
answer2 = 0
for n in range(N):
    for m in range(N):
        if not (visited[n][m]):
            answer2 += 1
            q = deque([[n, m]])
            color = D[n][m]
            while q:
                v = q.popleft()
                if not (visited[v[0]][v[1]]):
                    visited[v[0]][v[1]] = 1
                    for i in range(4):
                        x = v[0] + dx[i]
                        y = v[1] + dy[i]
                        if x >= 0 and x < N and y >= 0 and y < N:
                            if not (visited[x][y]) and D[x][y] == color:
                                q.append([x, y])

print(answer1, answer2)
