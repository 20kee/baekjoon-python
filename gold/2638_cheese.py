from collections import deque

N, M = map(int, input().split())
cheese = []
for n in range(N):
    cheese.append(list(map(int, input().split())))

dn = [0, 0, 1, -1]
dm = [1, -1, 0, 0]

count = 0
while True:
    adj_count = [[0 for n in range(M)] for n in range(N)]
    visited = [[0 for n in range(M)] for n in range(N)]
    q = deque([[0, 0]])
    visited[0][0] = 1
    while q:
        v = q.popleft()
        for i in range(4):
            n = v[0] + dn[i]
            m = v[1] + dm[i]
            if n >= 0 and n < N and m >= 0 and m < M and visited[n][m] == 0:
                if cheese[n][m] == 1:
                    adj_count[n][m] += 1
                else:
                    visited[n][m] = 1
                    q.append([n, m])

    deleted = 0
    for n in range(N):
        for m in range(M):
            if adj_count[n][m] >= 2:
                deleted += 1
                cheese[n][m] = 0
    
    if deleted == 0:
        break
    else:
        count += 1

print(count)
                    


    
    