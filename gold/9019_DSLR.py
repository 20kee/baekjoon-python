from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.readline

def get_left_shift(n):
    d = n//1000
    return n*10 - 10000*d + d

def get_right_shift(n):
    d = n%10
    return n//10 + 1000*d
    
def get_D(n):
    return (n*2)%10000

def get_S(n):
    if n == 0:
        return 9999
    return n-1

T = int(input())
for t in range(T):
    visited = defaultdict(int)
    s, t = map(int, input().split())
    q = deque([[s, ""]])
    visited[s] = 1
    while q:
        v = q.popleft()
        if v[0] == t:
            print(v[1])
            break
        t1 = get_left_shift(v[0])
        t2 = get_right_shift(v[0])
        t3 = get_D(v[0])
        t4 = get_S(v[0])
        if not(visited[t1]):
            q.append([t1, v[1]+"L"])
            visited[t1] = 1
        if not(visited[t2]):
            q.append([t2, v[1]+"R"])
            visited[t2] = 1
        if not(visited[t3]):
            q.append([t3, v[1]+"D"])
            visited[t3] = 1
        if not(visited[t4]):
            q.append([t4, v[1]+"S"])
            visited[t4] = 1
        
        
    