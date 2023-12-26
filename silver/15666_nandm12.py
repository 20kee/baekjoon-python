N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

answers = []
visit = [False for _ in range(N)]
now = [numbers[0]]

def dfs(i, now):
    now.append(numbers[i])
    if len(now) == M:
        answers.append(tuple(now))

    else:
        for j in range(i, N):
            dfs(j, now)
    
    now.pop()


for i in range(N):
    now = []
    dfs(i, now)
    

answer = sorted(list(set(answers)))
for ans in answer:
    print(*ans)