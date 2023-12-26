R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
machine = []
for r in range(R):
    for c in range(C):
        if room[r][c] == -1:
            machine.append((r, c))

def valid(r, c):
    return r >= 0 and r < R and c >= 0 and c < C

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
for t in range(T):
    add_dirty = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                dirty = room[r][c]//5
                count = 0
                for i in range(4):
                    r2 = r + dr[i]
                    c2 = c + dc[i]
                    if valid(r2, c2) and room[r2][c2] != -1:
                        count += 1
                        add_dirty[r2][c2] += dirty
                room[r][c] -= dirty*count
    
    for r in range(R):
        for c in range(C):
            room[r][c] += add_dirty[r][c]
    
    q = [(machine[0][0]-1, machine[0][1])]
    room[machine[0][0]-1][machine[0][1]] = 0
    while True:
        v = q.pop()
        if v[0] == machine[0][0] and v[1] == 1:
            break

        if v[1] == 0 and v[0] != 0:
            room[v[0]][v[1]] = room[v[0]-1][v[1]]
            q.append((v[0]-1, v[1]))
        elif v[0] == 0 and v[1] != C-1:
            room[v[0]][v[1]] = room[v[0]][v[1]+1]
            q.append((v[0], v[1]+1))
        elif v[1] == C-1 and v[0] != machine[0][0]:
            room[v[0]][v[1]] = room[v[0]+1][v[1]]
            q.append((v[0]+1, v[1]))
        elif v[0] == machine[0][0]:
            room[v[0]][v[1]] = room[v[0]][v[1]-1]
            q.append((v[0], v[1]-1))
    room[machine[0][0]][machine[0][1]+1] = 0

    q = [(machine[1][0]+1, machine[1][1])]
    while True:
        v = q.pop()
        if v[0] == machine[1][0] and v[1] == 1:
            break

        if v[1] == 0 and v[0] != R-1:
            room[v[0]][v[1]] = room[v[0]+1][v[1]]
            q.append((v[0]+1, v[1]))
        elif v[0] == R-1 and v[1] != C-1:
            room[v[0]][v[1]] = room[v[0]][v[1]+1]
            q.append((v[0], v[1]+1))
        elif v[1] == C-1 and v[0] != machine[1][0]:
            room[v[0]][v[1]] = room[v[0]-1][v[1]]
            q.append((v[0]-1, v[1]))
        elif v[0] == machine[1][0]:
            room[v[0]][v[1]] = room[v[0]][v[1]-1]
            q.append((v[0], v[1]-1))
    room[machine[1][0]][machine[1][1]+1] = 0
            


    # for r in range(R):
    #     print(*room[r])
    # print()
answer = 0
for r in range(R):
    for c in range(C):
        if room[r][c] > 0:
            answer += room[r][c]
print(answer)
    
                

