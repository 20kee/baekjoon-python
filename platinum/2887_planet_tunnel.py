def find(v):
    if parent[v] == v:
        return v
    
    parent[v] = find(parent[v])
    return parent[v]
 
 
def union(u, v):
    u = find(u)
    v = find(v)
 
    if u == v:
        return False
 
    if u < v:
        parent[v] = u
    else:
        parent[u] = v
    
    return True
 
 
def kruskal():
    global answer
    for w, u, v in tunnel:
        if union(u, v):
            answer += w
 
 
N = int(input())
answer = 0
parent = [n for n in range(N)]
coords = [list(map(int, input().split())) + [n] for n in range(N)]
 
tunnel = []
 
coords.sort()
for i in range(N - 1):
    tunnel.append((abs(coords[i][0] - coords[i + 1][0]), coords[i][3], coords[i + 1][3]))

coords.sort(key=lambda x: x[1])
for i in range(N - 1):
    tunnel.append((abs(coords[i][1] - coords[i + 1][1]), coords[i][3], coords[i + 1][3]))

coords.sort(key=lambda x: x[2])
for i in range(N - 1):
    tunnel.append((abs(coords[i][2] - coords[i + 1][2]), coords[i][3], coords[i + 1][3]))


tunnel.sort()
kruskal()
 
print(answer)