lst = [1, 3, 4, 6, 6, 6, 7, 7, 9, 10]
# lower bound
def lower_bound(lst, N):
    s, e = 0, len(lst)
    while s < e:
        m = (s+e)//2
        if lst[m] < N:
            s = m+1
        else:
            e = m
    return e;   