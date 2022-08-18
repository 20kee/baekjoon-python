from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(500000)
lst = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
N = lst[0]
lst.pop(0)
for n in range(4):
    lst[n] = lst[n] / 100
x = 0
y = 0
visited = defaultdict(int)
answer = 0

def dfs(x, y, depth, p):
    global answer
    visited[str(x)+","+str(y)] = 1
    if depth == N:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[str(nx)+","+str(ny)] == 0:
                answer += p*lst[i]
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[str(nx)+","+str(ny)] == 0:
                dfs(nx, ny, depth+1, p*lst[i])
                visited[str(nx)+","+str(ny)] = 0

dfs(0, 0, 1, 1)
print(answer)


