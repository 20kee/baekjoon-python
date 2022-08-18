from collections import defaultdict

N, M = map(int, input().split())
lamps = []
for n in range(N):
    lamps.append(list(input()))

K = int(input())
shapes = defaultdict(int)
mins = [0 for n in range(N)]
for n in range(N):
    shapes[str(lamps[n])] += 1

    for e in lamps[n]:
        if e == '0':
            mins[n] += 1

answer = 0
for n in range(N):
    if K-mins[n] >= 0 and (K-mins[n]) % 2 == 0:
        if answer < shapes[str(lamps[n])]:
            answer = shapes[str(lamps[n])]
print(answer)
    
