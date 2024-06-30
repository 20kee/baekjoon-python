N = int(input())
answers = [0, 0, 0, 0, 0]
body = [list(input()) for _ in range(N)]
heart = None
for n in range(N):
    for m in range(N):
        if body[n][m] == '*':
            heart = (n+1, m)
            break
    if heart != None:
        break

for m in range(heart[1]-1, -1, -1):
    if body[heart[0]][m] == '*':
        answers[0] += 1
    else:
        break

for m in range(heart[1]+1, N):
    if body[heart[0]][m] == '*':
        answers[1] += 1
    else:
        break

end = None
for n in range(heart[0]+1, N):
    if body[n][heart[1]] == '*':
        answers[2] += 1
        end = (n, heart[1])
    else:
        break

for n in range(end[0]+1, N):
    if body[n][end[1]-1] == '*':
        answers[3] += 1
    else:
        break


for n in range(end[0]+1, N):
    if body[n][end[1]+1] == '*':
        answers[4] += 1
    else:
        break
print(heart[0]+1, heart[1]+1)
print(*answers)