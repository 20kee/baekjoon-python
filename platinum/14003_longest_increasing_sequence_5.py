N = int(input())
lst = list(map(int, input().split()))
L = [] # L[i] = i길이짜리 증가하는 부분수열을 만드는 수중 가장 작은 수
P = []

def lower_bound(lst, n):
    s = 0
    e = len(lst)
    while s < e:
        mid = (s+e) // 2
        if lst[mid] >= n:
            e = mid
        else:
            s = mid + 1

    return e

for n in range(N):
    if len(L) == 0 or L[-1] < lst[n]:
        L.append(lst[n])
        P.append(len(L)-1)
    else:
        L[lower_bound(L, lst[n])] = lst[n]
        P.append(lower_bound(L, lst[n]))


result = []
print(len(L))
s = len(L)-1
i = len(P)-1
while s >= 0:
    while True:
        if P[i] == s: # 증가하는 수열의 s번째 수 == lst[i]가 증가하는 수열에서 가지는 인덱스 
            result.append(lst[i])
            i -= 1
            break
        i -= 1
    s -= 1

for e in result[::-1]:
    print(e, end=" ")