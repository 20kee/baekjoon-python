def find(u):
    if u == parent[u]:
        return u

    parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return False

    if u > v:
        parent[v] = u
    else:
        parent[u] = v

    return True

def upper_bound(lst, n):
    s = 0
    e = len(lst)
    while s < e:
        mid = (s+e) // 2
        if lst[mid] > n:
            e = mid
        else:
            s = mid + 1

    return e

N, M, K = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
# 2 3 4 5 7 8 9

card = list(map(int, input().split()))
parent = [i for i in range(M+1)]
for k in range(K):
    i = upper_bound(lst, card[k])
    j = find(i)
    union(i, j+1)
    print(lst[j])
    