from collections import defaultdict
from collections import deque
N, M = map(int, input().split())

ladders = defaultdict(int)
snakes = defaultdict(int)
for n in range(N):
    s, e = map(int, input().split())
    ladders[s] = e

for m in range(M):
    s, e = map(int, input().split())
    snakes[s] = e

visited = [False] * 101
visited[1] = True
answer = 0
q = deque([[1, 0]])
while q:
    v = q.popleft()
    if v[0] == 100:
        answer = v[1]
        break
    for d in range(1, 7):
        x = v[0] + d
        if x <= 100 and not(visited[x]):
            visited[x] = True
            if ladders[x]:
                visited[ladders[x]] = True
                q.append([ladders[x], v[1]+1])
            elif snakes[x]:
                visited[snakes[x]] = True
                q.append([snakes[x], v[1]+1])
            else:
                q.append([x, v[1]+1])

print(answer)

