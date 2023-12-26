from collections import defaultdict
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visit = [0 for _ in range(26)]

def valid(r, c):
    return r>=0 and r<R and c>=0 and c<C

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = 0
def dfs(coord, count):
    global answer
    if count > answer:
        answer = count
    visit[ord(board[coord[0]][coord[1]])-ord('A')] = 1
    for i in range(4):
        r = coord[0] + dr[i]
        c = coord[1] + dc[i]
        if valid(r, c) and not visit[ord(board[r][c])-ord('A')]:
            dfs((r, c), count+1)



    visit[ord(board[coord[0]][coord[1]])-ord('A')] = 0

dfs((0, 0), 1)
print(answer)