N = int(input())
X = list(map(int, input().split()))

if N > 2:
    for i in range(N-2):
        x1 = N[i]
        x2 = N[i+1]
        x3 = N[i+2]
        a = (x2-x3) // (x1-x2)
elif N == 2:
    if X[0] == X[1]:
        print(X[0])
    else:
        print('A')
else:
    print('A')
    