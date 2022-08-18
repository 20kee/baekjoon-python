import math
import sys
N, M = map(int, input().split())
waiting = list(map(int, input().split()))
if N < M:
    print(N)
    sys.exit(0)
s = 0
e = max(waiting) * N // M + 10
answer = 0
while s <= e:
    mid = (s+e) // 2
    sum = 0
    for m in range(M):
        sum += math.ceil(mid / waiting[m])

    if sum >= N:
        answer = mid
        e = mid-1
    else:
        s = mid+1
e = max(waiting)
numbers = [[0,0] for n in range(M)]
for m in range(M):
    numbers[m] = [math.ceil(answer / waiting[m]), answer%waiting[m], m]
    if numbers[m][1] == 0:
        numbers[m][1] = e
sum = 0
for e in numbers:
    sum += e[0]
numbers.sort(key = lambda x : (x[1],-x[2]))
n = sum
for e in numbers:
    if n == N:
        print(e[2]+1)
        break
    else:
        n -= 1
