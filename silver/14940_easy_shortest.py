from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dist = [[-1 for _ in range(M)] for _ in range(N)]
start = None
for n in range(N):
    for m in range(M):
        if board[n][m] == 2:
            start = (n, m)
            dist[n][m] = 0
        
        elif board[n][m] == 0:
            dist[n][m] = 0

q = deque([start])
dn = [0, 0, -1, 1]
dm = [1, -1, 0, 0]
def valid(n, m):
    return n>=0 and n<N and m>=0 and m<M
while q:
    v = q.popleft()
    for i in range(4):
        n = v[0] + dn[i]
        m = v[1] + dm[i]
        if valid(n, m) and dist[n][m] == -1 and board[n][m] == 1:
            dist[n][m] = dist[v[0]][v[1]] + 1
            q.append((n, m))
for e in dist:
    print(*e)
