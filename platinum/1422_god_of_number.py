from functools import cmp_to_key
def compare(a, b):
    t = int(a+b)
    t2 = int(b+a)
    if t > t2:
        return -1
    else:
        return 1
        
    
K, N = map(int, input().split())
lst = []
for k in range(K):
    lst.append(int(input()))
t = max(lst)
for i in range(N-K):
    lst.append(t)
    
for i in range(len(lst)):
    lst[i] = str(lst[i])
    
lst.sort(key=cmp_to_key(compare))
print(int("".join(lst)))
