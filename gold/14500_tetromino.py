N, M = map(int, input().split())
paper = [[*map(int, input().split())] for n in range(N)]
shapes = [[[0, 1], [0, 2], [0, 3]], 
          [[1, 0], [2, 0], [3, 0]],
          [[1, 1], [1, 0], [0, 1]],
          [[1, 0], [2, 0], [2, 1]],
          [[1, 0], [2, 0], [2, -1]],
          [[0, 1], [0, 2], [1, 2]],
          [[1, 0], [1, 1], [2, 1]],
          [[1, 0], [1, -1], [2, -1]],
          [[0, -1], [1, -1], [1, -2]],
          [[0, 1], [1, 1], [1, 2]],
          [[1, 0], [1, -1], [1, 1]],
          [[0, 1], [1, 1], [0, 2]],
          [[0, 1], [1, 1], [-1, 1]], 
          [[1, 0], [1, 1], [2, 0]],
          [[0, 1], [0, 2], [-1, 2]],
          [[1, 0], [0, 1], [0, 2]],
          [[0, 1], [1, 1], [2, 1]],
          [[0, 1], [1, 0], [2, 0]],
          [[1, 0], [1, 1], [1, 2]]]
answer = 0
for n in range(N):
    for m in range(M):
        for shape in shapes:
            temp = paper[n][m]
            count = 0
            for dot in shape:
                x = n+dot[0]
                y = m+dot[1]
                if x >= 0 and x < N and y >= 0 and y < M:
                    count += 1
                    temp += paper[x][y]
            if temp > answer:
                answer = temp

print(answer)
