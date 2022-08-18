from collections import defaultdict
import math
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
numbers = defaultdict(int)
for n in range(1, N+1):
    numbers[A[n-1]] = n
    A[n-1] = n
for n in range(N):
    B[n] = numbers[B[n]]
lst = [0 for n in range(N)]
for n in range(N):
    lst[B[n]-1] = n+1

tree = [0]*(pow(2,math.ceil(math.log(N,2))+1))
def make_tree(s, e, n):
    if s == e:
        tree[n] = 1
    else:
        s1 = s
        e1 = (s+e)//2
        s2 = e1+1
        e2 = e
        make_tree(s1, e1, 2*n)
        make_tree(s2, e2, 2*n+1)
        tree[n] = tree[2*n]+tree[2*n+1]

def get_value(s, e, fs, fe, n):
    if s > fe or fs > e:
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
    if s == e and s == t:
        tree[n] = 0
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

make_tree(1, N, 1)
answer = 0
for e in lst:
    temp = get_value(1, N, 1, e, 1)
    answer = answer + temp - 1
    update(1, N, e, 1)

print(answer)
    