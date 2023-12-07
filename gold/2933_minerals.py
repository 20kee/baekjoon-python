from collections import deque
import sys
R, C = map(int, input().split())
cave = [list(input()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

def throw_stick(height, i):
    if i%2 == 0: # 왼쪽에서 던짐
        for c in range(C):
            if cave[R-height][c] == 'x':
                cave[R-height][c] = '.'
                return (R-height, c)
    else: # 오른쪽에서 던짐
        for c in range(C):
            if cave[R-height][C-1-c] == 'x':
                cave[R-height][C-1-c] = '.'
                return (R-height, C-1-c)
    return None

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
def valid(r, c):
    return r >= 0 and r < R and c >= 0 and c < C

def get_gap(point):
    r, c = point
    gap = 0
    for y in range(r+1, R):
        if cave[y][c] == '.':
            gap += 1
        else:
            break
    return gap

def cluster_move(cluster, gap):
    new_cluster = []
    for point in cluster:
        cave[point[0]][point[1]] = '.'
        new_cluster.append((point[0]+gap, point[1]))

    for point in new_cluster:
        cave[point[0]][point[1]] = 'x'
    
    


def rearrange_cluster(point, visit):
    visit[point[0]][point[1]] = True
    bottom_points = []
    cluster = []
    q = deque([point])
    check = False
    while q:
        v = q.popleft()
        cluster.append(v)
        if v[0] == R-1:
            check = True
        
        for i in range(4):
            r2 = v[0] + dr[i]
            c2 = v[1] + dc[i]
            if valid(r2, c2) and not visit[r2][c2] and cave[r2][c2] == 'x':
                visit[r2][c2] = True
                q.append((r2, c2))
    if check:
        return False
    max_height = [-1 for _ in range(C)]
    _bottom_points = [None for _ in range(C)]
    for point in cluster:
        if cave[point[0]+1][point[1]] == '.':
            if point[0] > max_height[point[1]]:
                max_height[point[1]] = point[0]
                _bottom_points[point[1]] = point

    for point in _bottom_points:
        if point != None:
            bottom_points.append(point)

    min_gap = 101
    for bottom_point in bottom_points:
        gap = get_gap(bottom_point)
        if gap < min_gap:
            min_gap = gap
    cluster_move(cluster, min_gap)
    return True
        

def rearrange_cave(point_broken):
    visit = [[False for c in range(C)] for r in range(R)]
    r, c = point_broken
    for i in range(4):
        r2 = r + dr[i]
        c2 = c + dc[i]
        if valid(r2, c2) and cave[r2][c2] == 'x' and not visit[r2][c2]: # 빠가진 곳 주변에 돌이 있었다면.
            result = rearrange_cluster((r2, c2), visit)
            if result:
                break
            

for i, height in enumerate(heights):
    point_broken = throw_stick(height, i)
    if point_broken != None:
        rearrange_cave(point_broken)
    
for c in cave:
    print(''.join(c))
    


