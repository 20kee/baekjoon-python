import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [0] + [*map(int, input().split())]
sum = []
s = 0
for e in lst:
    s += e
    sum.append(s)

for m in range(M):
    s, e = map(int, input().split())
    print(sum[e]-sum[s-1])
