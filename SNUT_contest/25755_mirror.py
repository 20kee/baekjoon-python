d, N = input().split()
N = int(N)
lst = []
for n in range(N):
    lst.append(list(map(int, input().split())))

def inverse(a):
    if a == 2:
        return 5
    if a == 5:
        return 2
    if a == 8 or a == 1:
        return a
    
    return '?'
if d == 'D' or d == 'U':
    for n in range(N):
        for m in range(N):
            print(inverse(lst[N-n-1][m]), end=" ")
        print()

if d == 'L' or d == 'R':
    for n in range(N):
        for m in range(N):
            print(inverse(lst[n][N-1-m]), end=" ")
        print()
            
