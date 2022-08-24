from collections import deque
N, M = map(int, input().split())
campus = []
q = deque([])
for n in range(N):
    campus.append(list(input()))
    if len(q) == 0:
        for m in range(M):
            if campus[n][m] == "I":
                q.append([n, m])

visited = [[False for m in range(M)] for n in range(N)]
dn = [0, 0, -1 ,1]
dm = [1, -1, 0, 0]
answer = 0
while q:
    v = q.popleft()
    if not(visited[v[0]][v[1]]):
        visited[v[0]][v[1]] = True
        if campus[v[0]][v[1]] == "P":
            answer += 1
        for i in range(4):
            n = v[0] + dn[i]
            m = v[1] + dm[i]
            if n >= 0 and n < N and m >= 0 and m < M:
                if campus[n][m] == "O" or campus[n][m] == "P":
                    q.append([n,m])

if answer == 0:
    print("TT")
else:
    print(answer)


