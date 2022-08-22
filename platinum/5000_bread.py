import math

N = int(input())
original = [0] + list(map(int, input().split()))
target = [0] + list(map(int, input().split()))

now = [0 for n in range(N+1)]
for n in range(1, N+1):
    now[original[n]] = n

filled = [1 for n in range(N+1)]
filled[0] = 0
tree = [0 for i in range( pow(2, math.ceil( math.log(N,2) + 1) + 1))]

def init(s, e, node):
    if s == e:
        tree[node] = filled[s]
    else:
        s1 = s
        e1 = (s+e)//2
        s2 = e1 + 1
        e2 = e
        init(s1, e1, node*2)
        init(s2, e2, node*2+1)
        tree[node] = tree[node*2] + tree[node*2+1]

init(1, N, 1)

def query(s, e, node, fs, fe):
    if fe < fs or fs == fe and filled[fs] == 0:
        return 0

    if fs > e or fe < s:
        return False
    if fs <= s and e <= fe:
        return tree[node]

    s1 = s
    e1 = (s+e) // 2
    s2 = e1 + 1
    e2 = e
    a = query(s1, e1, node*2, fs, fe)
    b = query(s2, e2, node*2+1, fs, fe)
    if a == False:
        return b
    if b == False:
        return a
    
    return a+b

def update(s, e, node, b, gap):
    if s <= b and b <= e:
        if s == b and b == e:
            tree[node] += gap
        else:
            tree[node] += gap
            s1 = s
            e1 = (s+e)//2
            s2 = e1 + 1
            e2 = e
            update(s1, e1, node*2, b, gap)
            update(s2, e2, node*2+1, b, gap)


init(1, N, 1)

answer = []
f = 1
s = 2
for n in range(1, N-1):
    t = target[n]
    i = query(1, N, 1, 1, now[t]-1)
    filled[now[t]] = 0
    original[now[t]] = 0
    if now[t] == f:
        f = s
        s += 1
        while filled[s] == 0:
            s += 1

    elif now[t] == s:
        s += 1
        while filled[s] == 0:
            s += 1

    if i%2 != 0: #맨앞에서 2, 3번째 자리 바뀜
        now[original[f]], now[original[s]] = now[original[s]], now[original[f]]
        original[f], original[s] = original[s], original[f]
    
    update(1, N, 1, now[t], -1)


for n in range(1, N+1):
    if original[n] != 0:
        if original[n] == target[-2]:
            print("Possible")
        else:
            print("Impossible")
        break
    

