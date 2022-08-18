N = int(input())
lst = list(map(int, input().split()))
length = [0 for n in range(N)]
ans = 0
for n in range(N):
    t = 1
    for i in range(n):
        if length[i] >= t and lst[i] > lst[n]:
            t = length[i] + 1
    length[n] = t

    if length[n] > ans:
        ans = length[n]

print(ans)