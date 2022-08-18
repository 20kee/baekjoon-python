import sys
N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
answer = 0


now = [[i,i%3] for i in range(N)] # 처음 i번째에 있던 놈이 현재 있는 위치
while True:
    for n in range(N):
        if P[n] != now[n][1]:
            break

        if n == N-1:
            print(answer)
            sys.exit(0)
    
    answer += 1
    for n in range(N):
        now[n][0] = S[now[n][0]]
        now[n][1] = now[n][0]%3

    for n in range(N):
        if now[n][1] != n%3:
            break
        
        if n == N-1:
            print(-1)
            sys.exit(0)