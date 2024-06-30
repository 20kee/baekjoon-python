N, K = map(int, input().split())
medals = []
ta, tb, tc = 0, 0, 0
for _ in range(N):
    n, a, b, c = map(int, input().split())
    medals.append([a, b, c, n])
    if n == K:
        ta, tb, tc = a, b, c

medals.sort(reverse=True)
count = 0
for medal in medals:
    if ta == medal[0] and tb == medal[1] and tc == medal[2]:
        break
    else:
        count += 1
print(count+1)
