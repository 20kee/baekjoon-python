N = int(input())
water = list(map(int, input().split()))
water.sort()

answer = []
temp = 3000000001
for n in range(N):
    if temp == 0:
        break

    target = -water[n]
    s = 0
    e = N-1
    while True:
        if s == n or e == n:
            break

        t = water[s] + water[e]
        if abs(target-t) < temp:
            temp = abs(target-t)
            answer = [[water[n], water[s], water[e]]]

        if t > target:
            e -= 1
        elif t < target:
            s += 1
        else:
            break
print(*sorted(answer[0]))

    