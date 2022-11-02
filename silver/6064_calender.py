import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    M, N, x, y = map(int, input().split())
    answer = -1
    for D in range(x, N*M+1, M):
        if D%N == y or D%N==0 and N==y:
            answer = D
            break
    print(answer)