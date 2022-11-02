N = int(input())
lst = list(map(int, input().split()))

s = 1
for e in lst:
    s = s * (1 - e/100.0)
    print(100.0*(1-s))
