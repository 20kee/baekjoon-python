import copy

N, B = map(int, input().split())
matrix = []
answer = []
for n in range(N):
    matrix.append(list(map(int, input().split())))

def matrix_mul(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= 1000
    return result

def matsquare(matrix, B):
    answer = copy.deepcopy(matrix)
    if B == 1:
        return answer
    else:
        if B % 2 == 0:
            return matsquare(matrix_mul(answer, answer, N), B//2)
        else:
            return matrix_mul(matsquare(matrix_mul(answer, answer, N), (B-1)//2), matrix, N)

answer = matsquare(matrix, B)

for  n in range(N):
    for m in range(N):
        answer[n][m] = answer[n][m]%1000

for e in answer:
    print(*e)