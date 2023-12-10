import heapq

N = int(input())
doors = []

house = [list(input()) for _ in range(N)]
for r in range(N):
    for c in range(N):
        if house[r][c] == '#':
            doors.append((r, c))
            house[r][c] = '.'

distance = [[[2500, 2500, 2500, 2500] for _ in range(N)] for _ in range(N)]
distance[doors[0][0]][doors[0][1]] = [0, 0, 0, 0]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
def valid(r, c):
    return r >= 0 and r < N and c >= 0 and c < N

q = []
for i in range(4):
    r = doors[0][0] + dr[i]
    c = doors[0][1] + dc[i]
    if valid(r, c) and house[r][c] != '*':
        distance[r][c][i] = 0
        heapq.heappush(q, [distance[r][c][i], (r, c), i])

while q:
    cost, v, i = heapq.heappop(q)
    if cost > distance[v[0]][v[1]][i]:
        pass
    else:
        if house[v[0]][v[1]] == '.':  #오던 길로 감
            r = v[0] + dr[i]
            c = v[1] + dc[i]
            if valid(r, c) and house[r][c] != '*':
                if distance[r][c][i] > cost:
                    distance[r][c][i] = cost
                    heapq.heappush(q, [cost, (r, c), i])

        elif house[v[0]][v[1]] == '!': # 거울이라면 세가지로 나뉨.
            for j in range(4):
                r = v[0] + dr[j]
                c = v[1] + dc[j]
                if valid(r, c) and house[r][c] != '*':
                    if i+j == 1 or i+j == 5:
                        pass
                    elif i == j: # 그대로 진행
                        if distance[r][c][j] > cost:
                            distance[r][c][j] = cost
                            heapq.heappush(q, [cost, (r, c), j])
                    else: # 
                        if distance[r][c][j] > cost+1:
                            distance[r][c][j] = cost+1
                            heapq.heappush(q, [cost+1, (r, c), j])
                    
print(min(distance[doors[1][0]][doors[1][1]]))
                    



