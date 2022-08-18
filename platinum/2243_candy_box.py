import math
import sys
input = sys.stdin.readline
N = int(input())
h = math.ceil(math.log(1000000, 2)+1)
tree = [0 for n in range(pow(2, h)+1)]
candy = [0 for n in range(1000001)]

def update(s, e, t, n):
    if s == e:
        tree[n] = candy[t]
    else:
        s1 = s
        e1 = (s+e)//2
        s2 = e1+1
        e2 = e
        if s1 <= t and t <= e1:
            update(s1, e1, t, 2*n)
        elif s2 <= t and t <= e2:
            update(s2, e2, t, 2*n+1)
        tree[n] = tree[2*n] + tree[2*n+1]

def get_value(s, e, fs, fe, n):
    if s > fe or e < fs:
        return -1
    if s >= fs and e <= fe:
        return tree[n]

    s1 = s
    e1 = (s+e)//2
    s2 = e1 + 1
    e2 = e
    t1 = get_value(s1, e1, fs, fe, 2*n)
    t2 = get_value(s2, e2, fs, fe, 2*n+1)
    if t1 == -1:
        return t2
    elif t2 == -1:
        return t1
    return t1 + t2

for n in range(N):
    command = list(map(int, input().split()))
    if len(command) == 3:
        candy[command[1]] += command[2]
        update(1, 1000000, command[1], 1)
        
    else:
        s=1
        e=1000000
        while s < e:
            mid = (s+e)//2
            t = get_value(1, 1000000, 1, mid, 1)
            if t >= command[1]:
                e = mid
            else:
                s = mid+1

        candy[e] -= 1
        update(1, 1000000, e, 1)
        print(e)