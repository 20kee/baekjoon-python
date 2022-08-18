import copy
import sys
input = sys.stdin.readline
N, T = map(int, input().split())
A = list(map(int, input().split()))

def can_make(mid):
    B = copy.deepcopy(A)
    count = 0
    for i in range(N-1):
        if B[i+1]-B[i] > mid:
            count += B[i+1]-(B[i]+mid)
            B[i+1] = B[i]+mid
            
    for i in range(N-1, 0, -1):
        if B[i-1]-B[i] > mid:
            count += B[i-1]-(B[i]+mid)
            B[i-1] = B[i]+mid
            
    if count > T:
        return False
    return B
    
s = 0
e = 1000000000
ans = []
while s<=e:
    mid = (s+e)//2
    t = can_make(mid)
    if t == False:
        s = mid+1
    else:
        ans = copy.deepcopy(t)
        e = mid-1

print(*ans)