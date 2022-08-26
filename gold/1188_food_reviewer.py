N, M = map(int, input().split())

def get(N, M):
    if N >= M:
        if N%M == 0:
            return 0
        else:
            return get(N-M, M)
    elif M > N:
        if M%N == 0:
            return (M//N-1)*N
        else:
            return N*(M//N) + get(N, M%N)

print(get(N, M))