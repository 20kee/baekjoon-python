from collections import deque
s, e = map(int, input().split())

q = deque([[s, 1]])

answer = -1
while q:
    n, count = q.popleft()
    if n == e:
        answer = count
        break
    elif n < e:
        q.append([n*2, count+1])
        q.append([int(str(n) + '1'), count+1])

print(answer)
