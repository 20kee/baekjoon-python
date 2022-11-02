from collections import deque
N = int(input())
adj = [[*map(int, input().split())] for n in range(N)]

for n in range(N):
    visited = [0 for n in range(N)]
    q = deque([n])
    while q:
        v = q.popleft()
        for m in range(N):
            if adj[v][m] and not(visited[m]):
                visited[m] = 1
                q.append(m)
    print(*visited)
