from collections import deque
import heapq
W, H = map(int, input().split())
world = [list(input()) for _ in range(H)]
lazers = []
count = 0
for h in range(H):
    for w in range(W):
        if world[h][w] == 'C':
            count+= 1
            lazers.append((h, w))
            world[h][w] = '.'
            if count == 2:
                break
    if count == 2:
        break


minimum_mirror = [[[10000, 10000, 10000, 10000] for _ in range(W)] for _ in range(H)]
dh = [0, 0, -1, 1]
dw = [1, -1, 0, 0]
def valid(h, w):
    return h >= 0 and h < H and w >= 0 and w < W
q = []

minimum_mirror[lazers[0][0]][lazers[0][1]]=  [0, 0, 0, 0]
for i in range(4):
    h = lazers[0][0] + dh[i]
    w = lazers[0][1] + dw[i]
    if valid(h, w) and world[h][w] != '*':
        minimum_mirror[h][w][i] = 0
        heapq.heappush(q, (minimum_mirror[h][w][i], (h, w, i)))

while q:
    v = heapq.heappop(q)
    c = v[0]
    h, w, d = v[1]
    if c > minimum_mirror[h][w][d]:
        continue

    for i in range(4):
        if i+d != 1 and i+d != 5:
            h2 = h + dh[i]
            w2 = w + dw[i]
            if valid(h2, w2) and world[h2][w2] != '*':
                if i == d: # no cost
                    c2 = c
                else:
                    c2 = c+1

                if minimum_mirror[h2][w2][i] > c2:
                    minimum_mirror[h2][w2][i] = c2
                    heapq.heappush(q, (c2, (h2, w2, i)))

print(min(minimum_mirror[lazers[1][0]][lazers[1][1]])) 
    




