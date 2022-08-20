from collections import deque
from collections import defaultdict

N, T, W = map(int, input().split())
q = deque([])
c = defaultdict(int)
for n in range(N):
    px, tx = map(int, input().split())
    q.append([px, tx])

M = int(input())
for m in range(M):
    px, tx, cx = map(int, input().split())
    c[cx] = [px, tx]

w = 0
if c[w] != 0:
    q.append(c[w])
while w < W:
    n = q.popleft()
    if n[1] <= T:
        for k in range(n[1]):
            print(n[0])
            w += 1
            if c[w] != 0:
                q.append(c[w])
            if w == W:
                break
    else:
        for k in range(T):
            n[1] -= 1
            print(n[0])
            w += 1
            if c[w] != 0:
                q.append(c[w])
            if w == W:
                break
        q.append(n)
        



