N, M = map(int, input().split())
seat = []
for n in range(N):
    seat.append(list(input()))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0 ,1]
sang = 0
answer = 0
for n in range(N):
    for m in range(M):
        if seat[n][m] == ".":
            temp = 0
            for i in range(8):
                x = n + dx[i]
                y = m + dy[i]
                if x < N and x >= 0 and y < M and y >= 0:
                    if seat[x][y] == "o":
                        temp += 1
            if temp > sang:
                sang = temp
                        
        else:
            for i in range(4, 8):
                x = n + dx[i]
                y = m + dy[i]
                if x < N and x >= 0 and y < M and y >= 0:
                    if seat[x][y] == "o":
                        answer += 1

print(answer + sang)


