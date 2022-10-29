from collections import deque
from operator import truediv
from functools import cache

def possible(v):
    for e in s:
        if e[0] == v[0] or e[1] == v[1] or abs(e[0]-v[0]) == abs(e[1]-v[1]):
            return False
    return True

def dfs(n):
    global N
    global count
    if (n == N):
        count += 1
        return
    
    for m in range(N):
        v = [n, m]
        if possible(v):
            s.append(v)
            dfs(n+1)
            s.pop()

    return

N = int(input())
count = 0
for n in range(N):
    s = [[0, n]]
    dfs(1)
    

print(count)
        
