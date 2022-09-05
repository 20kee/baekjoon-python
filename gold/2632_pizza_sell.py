K = int(input())
N, M = map(int, input().split())
A = [0]
B = [0]
for n in range(N):
    A.append(int(input()))

for m in range(M):
    B.append(int(input()))

dpA = [[0 for n in range(N+1)] for m in range(N+1)]
dpB = [[0 for m in range(M+1)] for m in range(M+1)]
cA = [0 for n in range(max(K+1, sum(A)+1))]
cB = [0 for n in range(max(K+1, sum(B)+1))]
s = 0
for n in range(1, N+1):
    s += A[n]
    dpA[1][n] = s
    
for s in range(2, N+1):
    for l in range(1, N+1):
        if s+l <= N+1:
            dpA[s][l] = dpA[1][s+l-1] - dpA[1][s-1]
        else:
            dpA[s][l] = dpA[1][N] - dpA[1][s-1] + dpA[1][(s+l) - (N+1)]

s = 0
for m in range(1, M+1):
    s += B[m]
    dpB[1][m] = s
    
for s in range(2, M+1):
    for l in range(1, M+1):
        if s+l <= M+1:
            dpB[s][l] = dpB[1][s+l-1] - dpB[1][s-1]
        else:
            dpB[s][l] = dpB[1][M] - dpB[1][s-1] + dpB[1][(s+l) - (M+1)]

for n in range(1, N+1):
    for m in range(1, N):
        cA[dpA[n][m]] += 1
cA[sum(A)] += 1

for n in range(1, M+1):
    for m in range(1, M):
        cB[dpB[n][m]] += 1
cB[sum(B)] += 1
cA[0] = 1
cB[0] = 1
answer = 0
for a in range(K+1):
    
    b = K-a
    answer += cA[a] * cB[b]
print(answer)