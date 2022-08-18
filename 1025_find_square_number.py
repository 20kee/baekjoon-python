from collections import defaultdict
N, M = map(int, input().split())
numbers = []
for n in range(N):
    numbers.append(list(input()))

is_square = defaultdict(int)
for i in range(100001):
    is_square[str(i*i)] = 1

d = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

answer = -1
for n in range(N):
    for m in range(M):
        temp = numbers[n][m]
        if is_square[temp] == 1 and int(temp) > answer:
            answer = int(temp)
        for xd in d:
            for yd in d:
                x = n
                y = m
                temp = numbers[x][y]
                if xd == 0 and yd == 0:
                    pass
                else:
                    while True:
                        x = x + xd
                        y = y + yd
                        if x >= 0 and x < N and y >= 0 and y < M:
                            temp = temp + numbers[x][y]
                            if is_square[temp] == 1 and int(temp) > answer:
                                answer = int(temp)
                        else:
                            break

print(answer)

                    

        



