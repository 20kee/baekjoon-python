import sys
import math
N, M, K = map(int, input().split())
lst = [0]
tree = [0 for i in range( pow(2, math.ceil( math.log(N,2) + 1) + 1))]

for n in range(N):
    lst.append(int(sys.stdin.readline()))
def init(s, e, node):
    if s == e:
        tree[node] = lst[s]
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

for i in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        gap = c - lst[b]
        lst[b] = c
        update(1, N, 1, b, gap)
    else:
        print(query(1, N, 1, b, c))