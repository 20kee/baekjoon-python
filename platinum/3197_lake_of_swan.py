from collections import deque
R, C = map(int, input().split())
lake = []
swans = []
for r in range(R):
    lake.append(list(input()))

for r in range(R):
    for c in range(C):
        if lake[r][c] == "L":
            swans.append([r, c])
            lake[r][c] = "."
            if len(swans) == 2:
                break
    

def find(v):
    if v == root[v[0]][v[1]]:
        return v
    root[v[0]][v[1]] = find(root[v[0]][v[1]])
    return root[v[0]][v[1]]


def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)

    if rank[r1[0]][r1[1]] > rank[r2[0]][r2[1]]:
        root[r2[0]][r2[1]] = r1
    elif rank[r1[0]][r1[1]] < rank[r2[0]][r2[1]]:
        root[r1[0]][r1[1]] = r2
    else:
        root[r2[0]][r2[1]] = r1
        rank[r1[0]][r1[1]] += 1

root = [[(i, j) for j in range(C)] for i in range(R)]
rank = [[0 for j in range(C)] for i in range(R)]  # union 최적화
visit = [[False for _ in range(C)] for _ in range(R)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0] 
waters = deque()
for r in range(R):
    for c in range(C):
        if not visit[r][c] and lake[r][c] == ".":
            visit[r][c] = True
            q = deque([(r, c)])
            while q:
                r2, c2 = q.popleft()
                root[r2][c2] = (r, c)
                for i in range(4):
                    r3, c3 = r2+dr[i], c2+dc[i]
                    if r3 >= 0 and r3 < R and c3 >= 0 and c3 < C and not visit[r3][c3] and lake[r3][c3] == '.':
                        visit[r3][c3] = 1
                        q.append([r3, c3])
                    elif r3 >= 0 and r3 < R and c3 >= 0 and c3 < C and not visit[r3][c3] and lake[r3][c3] == 'X':
                        visit[r3][c3] = 1
                        waters.append([r3, c3])
count = 0
while True:
    if find(swans[0]) == find(swans[1]):
        print(count)
        break
    
    tmp = deque()
    while waters:
        r, c = waters.popleft()
        lake[r][c] = '.'
        merge_point = []
        for i in range(4):
            r2, c2 = r+dr[i], c+dc[i]
            if r2 >= 0 and r2 < R and c2 >= 0 and c2 < C and not visit[r2][c2] and lake[r2][c2] =='X':
                visit[r2][c2] = 1
                tmp.append([r2, c2])
            elif r2 >= 0 and r2 < R and c2 >= 0 and c2 < C and lake[r2][c2] == ".":
                merge_point.append([r2, c2])

        for p in merge_point:
            if find((p[0], p[1])) != find((r, c)):
                union(p, (r, c)) 
    count += 1
    waters = tmp
    
