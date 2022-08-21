import math
def lower_bound(lst, t):
    s, e = 0, len(lst)
    while s < e:
        m = s + (e-s) // 2
        if lst[m] < t:
            s = m+1
        else:
            e = m
    return e

N, k = map(int, input().split())
r = 0
if N > k:
    r += (N-k) * k
    N = k
start = [0 for n in range(int(math.sqrt(k))+1)]

for n in range(1, int(math.sqrt(k))+1):
    start[n-1] = k // n
start.sort()
e = lower_bound(start, N)
start[lower_bound(start, N)] = N
start = start[:e+1]
start.sort(reverse=True)
for i in range(len(start)-2):
    n1 = k%start[i] #첫항
    n2 = k%(start[i+1]+1) #막항
    r += (n1+n2) * (start[i]-start[i+1]) // 2

for n in range(start[-2], 0, -1):
    r += k%n

print(r)


