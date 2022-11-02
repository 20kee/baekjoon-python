from collections import defaultdict
T = int(input())
for t in range(T):
    N = int(input())
    clothes = defaultdict(int)
    for n in range(N):
        n, c = input().split()
        clothes[c] += 1
    answer = 1
    for v in clothes.values():
        answer *= v+1
    print(answer-1)
