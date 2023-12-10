from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

dw = [0, 0, -1, 1]
dh = [1, -1, 0, 0]
while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    room = [list(input()) for _ in range(H)]
    dirties = []
    robot = ()
    for h in range(H):
        for w in range(W):
            if room[h][w] == '*':
                dirties.append((h, w))
            elif room[h][w] == 'o':
                robot = (h, w)
    dirties.append(robot)
    distance = [[400 for _ in range(len(dirties))] for _ in range(len(dirties))]

    def valid(h, w):
        return h >= 0 and h < H and w >= 0 and w < W

    def get_distance(n ,dirty):
        visit = [[False for _ in range(W)] for _ in range(H)]
        visit[dirty[0]][dirty[1]] = True
        distance[n][n] = 0
        q = deque([[dirty, 0]])
        while q:
            v, c = q.popleft()
            for i in range(4):
                h2 = v[0] + dh[i]
                w2 = v[1] + dw[i]
                if valid(h2, w2) and not visit[h2][w2] and room[h2][w2] != 'x':
                    visit[h2][w2] = True
                    q.append([(h2, w2), c+1])
                    if room[h2][w2] == '*':
                        distance[n][dirties.index((h2, w2))] = c+1
                        if 400 not in distance[n]:
                            q = []
                            break
    
    for n, dirty in enumerate(dirties):
        get_distance(n, dirty)
    
    def get_total_dist(permu):
        cost = distance[-1][permu[0]]
        for i in range(len(permu)-1):
            cost += distance[permu[i]][permu[i+1]]
        return cost


    
    if 400 in distance[-1]:
        print(-1)
    else:
        permu = list(permutations([i for i in range(len(dirties)-1)]))
        cost = 4000
        for p in permu:
            total_dist = get_total_dist(p)
            if cost > total_dist:
                cost = total_dist
        print(cost)


