from collections import deque

N = int(input())
forest = []
visited = [[0, 0] for j in range(N*N)]
q = deque([])
log = []
end = []
goal = []
for n in range(N):
    forest.append(list(input()))
    for m in range(N):
        if forest[n][m] == "B":
            log.append(n*N+m)
            forest[n][m] = 0
        elif forest[n][m] == "E":
            end.append(n*N+m)
            forest[n][m] = 0
        else:
            forest[n][m] = int(forest[n][m])

if log[1] != log[0]+1:
    q.append([log[0], 1, 0])
else:
    q.append([log[0], 0, 0])

if end[1] != end[0]+1:
    goal = [end[0], 1]
else:
    goal = [end[0], 0]

answer = 0
while q:
    v = q.popleft()
    if v[0] == goal[0] and v[1] == goal[1]: 
        answer = v[2]
        break

    if visited[v[0]][v[1]] == 0:
        visited[v[0]][v[1]] = 1
        x = v[0] // N
        y = v[0] % N
        temp = 0
        if v[1] == 0: # 가로
            if x > 0 and forest[x-1][y] == 0 and forest[x-1][y+1] == 0 and forest[x-1][y+2] == 0: # 위로
                temp += 1
                q.append([v[0]-N, 0, v[2]+1])

            if x < N-1 and forest[x+1][y] == 0 and forest[x+1][y+1] == 0 and forest[x+1][y+2] == 0: # 아래로
                temp += 1
                q.append([v[0]+N, 0, v[2]+1])

            if y > 0 and forest[x][y-1] == 0: # 왼쪽으로
                q.append([v[0]-1, 0, v[2]+1])

            if y < N-3 and forest[x][y+3] == 0: # 오른쪽으로
                q.append([v[0]+1, 0, v[2]+1])

            if temp == 2:
                q.append([v[0]-N+1, 1, v[2]+1])
        else: # 세로
            if x > 0 and forest[x-1][y] == 0: # 위로
                q.append([v[0]-N, 1, v[2]+1])

            if x < N-3 and forest[x+3][y] == 0: # 아래로
                q.append([v[0]+N, 1, v[2]+1])
            
            if y > 0 and forest[x][y-1] == 0 and forest[x+1][y-1] == 0 and forest[x+2][y-1] == 0: # 왼쪽으로
                temp += 1
                q.append([v[0]-1, 1, v[2]+1])
            
            if y < N-1 and forest[x][y+1] == 0 and forest[x+1][y+1] == 0 and forest[x+2][y+1] == 0: # 오른쪽으로
                temp += 1 
                q.append([v[0]+1, 1, v[2]+1])

            if temp == 2:
                q.append([v[0]+N-1, 0, v[2]+1])

print(answer)