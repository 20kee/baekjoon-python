from collections import defaultdict
from collections import deque
import decimal

N, M = map(int,input().split())
king = input()
blood = defaultdict(list)
adj = defaultdict(list)
visited = defaultdict(int)
blood[king] = 1.0

for n in range(N):
    a, b, c = input().split()
    adj[a].append(b)
    adj[a].append(c)

def dfs(name):
    if visited[name] == 1:
        return blood[name]

    if adj[name] == list():
        if name == king:
            return 1.0
        else:
            blood[name] = 0.0
            return 0.0
    
    b1 = dfs(adj[name][0])
    b2 = dfs(adj[name][1])
    blood[name] = (b1+b2) / 2
    visited[name] = 1
    return blood[name]

max_blood = -1.0
answer = ""
for m in range(M):
    c = input()
    dfs(c)
    if blood[c] > max_blood:
        answer = c
        max_blood = blood[c]
        
print(answer)
