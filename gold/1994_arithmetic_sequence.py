def lower_bound(lst, t):
    left, right = 0, len(lst)
    s, e = 0, len(lst)
    while s < e:
        m = s + (e-s) // 2
        if lst[m] < t:
            s = m+1
        else:
            e = m
    return e

N = int(input())
numbers = []
answer = 1
for n in range(N):
    numbers.append(int(input()))
numbers.sort()

answer = 1
z = 1
for n in range(N-1):
    if numbers[n] == numbers[n+1]:
        z += 1
    else:
        if z > answer:
            answer = z
        z = 1
if z > answer:
    answer = z


visit = [[0 for n in range(N)] for n in range(N)]
for n in range(N):
    for m in range(n+1, N):
        if visit[n][m] == 0:
            visit[n][m] = 1
            d = numbers[m] - numbers[n]
            if d != 0:
                l = 2
                e = m
                while True:
                    i = lower_bound(numbers, numbers[e]+d)
                    if i < len(numbers) and numbers[i] == numbers[e]+d:
                        visit[e][i] = 1
                        e = i
                        l += 1
                    else:
                        break
                if l > answer:
                    answer = l
print(answer)

