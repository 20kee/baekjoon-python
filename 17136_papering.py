import sys
# 타입을 미리 정해놓고 하면 bfs 돌면서 뒷부분이 이미 지워졌음에도 색종이가 겹치게 되는 case 발생
# 돌면서 붙일 수 있은 종이를 붙이고 그 다음 좌표에서 붙일 수 있는 색종이의 종류를 바로 구해야함
paper = []
for n in range(10):
    paper.append(list(map(int, input().split())))

def papering(n, m, l):
    for n2 in range(n, n+l):
        for m2 in range(m, m+l):
            paper[n2][m2] = 0

def de_papering(n, m, l):
    for n2 in range(n, n+l):
        for m2 in range(m, m+l):
            paper[n2][m2] = 1
answer = 26
used = [0 for n in range(6)]

def is_type(n, m, l):    
    if n+l <= 10 and m+l <= 10:
        for n2 in range(n, n+l):
            for m2 in range(m, m+l):
                if paper[n2][m2] == 0:
                    return False
        return True
    else:
        return False

def dfs(n, m, count):
    global answer

    if count >= answer:
        return

    if n >= 9 and m >= 10:
        if count < answer:
            answer = count

    elif m > 9:
        dfs(n+1, 0, count)

    elif paper[n][m] == 1:
        for l in range(5, 0, -1):
            if is_type(n, m, l):
                if used[l] < 5:
                    used[l] += 1
                    papering(n, m, l)
                    dfs(n, m+1, count+1)
                    used[l] -= 1
                    de_papering(n, m, l)
    else:
        dfs(n, m+1, count)

dfs(0, 0, 0)
if answer == 26:
    print(-1)
else:
    print(answer)
