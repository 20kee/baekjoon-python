def duplicate(N, stars):
    if N == 3:
        return
    L = len(stars)
    for l in range(L):
        stars.append(stars[l] + ' '*(2*(L-l) - 1) + stars[l])
    duplicate(N//2, stars)

N = int(input())
stars = ['*', '* *', '*****']
duplicate(N, stars)
for n in range(N):
    print(' ' * (N-n-1) + stars[n] + ' ' * (N-n-1))