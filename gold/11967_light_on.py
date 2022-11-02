from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

light = [[False for n in range(N+1)] for n in range(N+1)]
real_visited = [[False for n in range(N+1)] for n in range(N+1)]
light[1][1] = True
adj = [[[] for n in range(N+1)] for n in range(N+1)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for m in range(M):
    x, y, a, b = map(int, input().split())
    adj[x][y].append([a,b])

def bfs():
    global N
    count = 1
    visited = [[False for n in range(N+1)] for n in range(N+1)]
    q = deque([[1, 1]])
    visited[1][1] = True
    while q:
        v = q.popleft()
        n, m = v
        if not(real_visited[n][m]):
            real_visited[n][m] = True
            for e in adj[n][m]:
                if not(light[e[0]][e[1]]):
                    light[e[0]][e[1]] = True
                    for i in range(4):
                        x = n+dx[i]
                        y = m+dy[i]
                        if 1 <= x <= N and 1 <= y <= N and visited[x][y]:
                            count += 1
                            visited[e[0]][e[1]] = True
                            q.append([e[0], e[1]])
                            break
        
        for i in range(4):
            x = n+dx[i]
            y = m+dy[i]
            if 1 <= x <= N and 1 <= y <= N and not(visited[x][y]) and light[x][y]:
                count += 1
                visited[x][y] = True
                q.append([x, y])
    
    return count

bfs()
answer = 0
for e in light:
    for e2 in e:
        if e2:
            answer += 1
print(answer)