N = int(input())
M = int(input())
str = list(input())
t = 'I'
N =2*N+1
count = 0
answer = 0
for e in str:
    if e == t:
        count += 1
        if t == 'I':
            t = 'O'
        else:
            t = 'I'
    else:
        if e == 'I':
            count = 1
        else:
            count = 0
            

    if count == N:
        answer += 1
        count = N-2

print(answer)
