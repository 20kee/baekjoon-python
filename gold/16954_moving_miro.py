from collections import deque
maze = [list(input()) for _ in range(8)]
walls = [[] for _ in range(9)]
for r in range(8):
    for c in range(8):
        if maze[r][c] == '#':
            walls[0].append((r, c))

for i in range(1, 8):
    for wall in walls[i-1]:
        if wall[0] <= 6:
            walls[i].append((wall[0]+1, wall[1]))


def valid(r, c):
    return r >= 0 and r < 8 and c >= 0 and c < 8
dr = [0, 0, 1, -1, 1, 1, -1, -1, 0]
dc = [1, -1, 0, 0, 1, -1, 1, -1, 0]
q = deque([])
q.append([(7, 0), 0])
answer = 0
while q:
    v, sec = q.popleft()
    if walls[sec] == []:
        answer = 1
        break
    for i in range(9):
        r = v[0] + dr[i]
        c = v[1] + dc[i]
        if valid(r, c):
            if (r,c) not in walls[sec] and (r,c) not in walls[sec+1]:
                q.append([(r, c), sec+1])
print(answer)
        

