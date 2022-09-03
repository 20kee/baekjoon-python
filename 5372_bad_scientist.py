import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(n):
    global answer
    d = False
    for e in adj[n]:
        if count[e] == 1:
            d = True
            break

    if d: # 나 없어져야 함
        answer += 1 
        count[n] = 0
        for e in adj[n]:
            if count[e] > 0:
                count[e] -= 1
    
    if 1 not in count:
        return

    for e in adj[n]:
        if count[e] > 0:
            dfs(e) 

T = int(input())
for t in range(T):
    N = int(input())
    K = int(input())
    M = int(input())
    adj = [[] for n in range(N+1)]
    count = [0 for n in range(N+1)]
    count_zero = [[0, n] for n in range(N+1)]
    update = [0 for n in range(N+1)]
    for m in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        count[a] += 1
        count[b] += 1
    answer = 0
    while True:
        b = True
        max = 0
        i = 0
        no_count = True
        for n in range(1, N+1):
            c = count[n]
            if c > 0:
                b = False
                if c == 1:
                    no_count = False
                    for e in adj[n]:
                        if count[e] > 0:
                            count[e] = 0
                            answer += 1
                            for e2 in adj[e]:
                                count[e2] -= 1
                else:
                    if c > max:
                        max = c
                        i = n
        
        if b:
            break
        
        if no_count:
            answer += 1
            count[i] = 0
            for e in adj[i]:
                count[e] -= 1
        
        if answer > K:
            break

    
    if answer > K:
        print("IMPOSSIBLE")
    else:
        print(answer)
                     

    
        
    
    


                
    
    
        
    