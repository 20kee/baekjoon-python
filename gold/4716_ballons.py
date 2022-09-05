import sys
from functools import cmp_to_key
import math

def diff(a, b):
    if abs(a[1]-a[2]) > abs(b[1]-b[2]):
        return -1
    return 1
while True:
    N, A, B = map(int, input().split())
    if N == 0:
        sys.exit(0)

    team = []

    for n in range(N):
        team.append(list(map(int, input().split())))

    team.sort(key=cmp_to_key(diff))
    answer = 0
    for e in team:
        if e[1] < e[2]:
            if A > e[0]:
                answer += e[0]*e[1]
                A -= e[0]
            else:
                answer += A*e[1]
                answer += (e[0]-A)*e[2]
                B -= (e[0]-A)
                A = 0
                
        else:
            if B > e[0]:
                answer += e[0]*e[2]
                B -= e[0]
            else:
                answer += B*e[2]
                answer += (e[0]-B)*e[1]
                A -= (e[0]-B)
                B = 0
    print(answer)

