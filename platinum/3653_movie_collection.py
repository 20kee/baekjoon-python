import sys
import math
input = sys.stdin.readline

def make_tree(s, e, n):
    global tree
    global temp
    
    if s == e:
        tree[n] = temp[s]
    else:
        s1 = s
        e1 = (s+e)//2
        s2 = e1 + 1
        e2 = e
        make_tree(s1, e1, 2*n)
        make_tree(s2, e2, 2*n+1)
        tree[n] = tree[2*n] + tree[2*n+1]

def get_value(s, e, fs, fe, n):
    global tree
    global temp

    if e < fs or s > fe:
        return -1
    if s >= fs and e <= fe:
        return tree[n]

    s1 = s
    e1 = (s+e)//2
    s2 = e1+1
    e2 = e
    temp1 = get_value(s1, e1, fs, fe, 2*n)
    temp2 = get_value(s2, e2, fs, fe, 2*n+1)
    if temp1 == -1:
        return temp2
    elif temp2 == -1:
        return temp1
    else:
        return temp1 + temp2

def update(s, e, t, n):
    global tree
    global temp
    
    if s == e:
        tree[n] = temp[s]
    else:
        s1 = s
        e1 = (s+e)//2
        s2 = e1+1
        e2 = e
        if s1 <= t and t <= e1:
            update(s1, e1, t, 2*n)
        if s2 <= t and t <= e2:
            update(s2, e2, t, 2*n+1)
        tree[n] = tree[2*n] + tree[2*n+1]


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    M2 = M
    lst = list(map(int, input().split()))
    temp = [0] + [0 for m in range(M)] + [1 for n in range(N)]
    h = math.ceil(math.log(len(temp), 2))
    tree = [0 for n in range(pow(2, h+1)+1)]
    make_tree(1, N+M, 1)
    location = [0]
    for n in range(N):
        location.append(M+n+1)
    for e in lst:
        now = location[e]
        print(get_value(1, N+M2, 1, now-1, 1), end=" ")
        temp[M] = 1
        location[e] = M
        M -= 1
        temp[now] = 0
        update(1, N+M2, now, 1)
        location[e] = M+1
        update(1, N+M2, M+1, 1)
    print()
