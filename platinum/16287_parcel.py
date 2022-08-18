from collections import defaultdict
import sys
W, N = map(int, sys.stdin.readline().split())
how = defaultdict(int)
lst = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    for j in range(i+1, N):
        if lst[i] + lst[j] < W:
            if how[W-lst[i]-lst[j]] == 1:
                print("YES")
                sys.exit(0)
    for j in range(i):
        if lst[i] + lst[j] < W:
            how[lst[i]+lst[j]] = 1

print("NO")