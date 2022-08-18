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

N = int(input())
L = [] # L[i] is the smallest thing taht can be the last element of the longest increasing subsequence has the length of "i".
P = [0 for n in range(N)]
adj = [0 for n in range(500001)]
wires = []
lst = []
for n in range(N):
    temp = list(map(int, input().split()))
    wires.append(temp)
    adj[temp[1]] = temp[0]
wires.sort()
for n in range(N):
    lst.append(wires[n][1])

for i in range(N):
    if len(L) == 0 or L[-1] < lst[i]:
        L.append(lst[i])
        P[i] = len(L)-1
    else:
        t = lower_bound(L, lst[i])
        L[t] = lst[i]
        P[i] = t
print(N - len(L))
result = []
m = len(L)-1
for i in range(N)[::-1]:
    if P[i] != m:
        result.append(i)
    else:
        m -= 1

for i in range(len(result)):
    result[i] = adj[lst[result[i]]]

result.sort()
for e in result:
    print(e)