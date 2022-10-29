from collections import deque

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))
answer = 0
l = 0
k = 0
q = deque([])
while True:
    if l + trucks[k] <= L:
        answer += 1
        if len(q) > 0 and q[0][0] + W == answer:
            t = q.popleft()
            l -= t[1]
        q.append([answer, trucks[k]])
        l += trucks[k]
        k += 1
    else:
        t = q.popleft()
        answer = t[0] + W
        l -= t[1]
        if l + trucks[k] <= L:
            q.append([answer, trucks[k]])
            l += trucks[k]
            k += 1

    if k == len(trucks):
        answer = q[-1][0] + W
        break
print(answer)
