D, K = map(int, input().split())
fibo = [0, 1, 1]
for n in range(3, 31):
    fibo.append(fibo[n - 1] + fibo[n - 2])
A, B = 0, 0
for a in range(1, K):
    if (K - (fibo[D - 2] * a)) % fibo[D - 1] == 0:
        A = a
        B = (K - fibo[D - 2]*a) // fibo[D - 1]
        break
print(A, B, sep="\n")
