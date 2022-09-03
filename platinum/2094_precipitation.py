from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
tree1 = [0] * (N*4) # 오른쪽 큼
tree2 = [0] * (N*4) # 왼쪽 큼

def init1(s, e, node):
    if s == e:
        tree1[node] = s
    else:
        init1(s, (s+e)//2, 2*node)
        init1((s+e)//2+1, e, 2*node+1)
        v1 = P[tree1[2*node]][1]
        v2 = P[tree1[2*node+1]][1]
        if v2 < v1:
            tree1[node] = tree1[2*node]
        else:
            tree1[node] = tree1[2*node+1]

def init2(s, e, node):
    if s == e:
        tree2[node] = s
    else:
        init2(s, (s+e)//2, 2*node)
        init2((s+e)//2+1, e, 2*node+1)
        v1 = P[tree2[2*node]][1]
        v2 = P[tree2[2*node+1]][1]
        if v2 > v1:
            tree2[node] = tree2[2*node+1]
        else:
            tree2[node] = tree2[2*node]

def query1(s, e, node, fs, fe): # 큰것들중 오른쪽
    if e < fs or s > fe:
        return False
    if s >= fs and e <= fe:
        return tree1[node]
    
    t1 = query1(s, (s+e)//2, 2*node, fs, fe)
    t2 = query1((s+e)//2+1, e, 2*node+1, fs, fe)
    if t1 == False:
        return t2
    if t2 == False:
        return t1
    
    v1 = P[t1][1]
    v2 = P[t2][1]
    if v2 < v1:
        return t1
    else:
        return t2

def query2(s, e, node, fs, fe): # 큰것들중 왼쪽
    if e < fs or s > fe:
        return False
    if s >= fs and e <= fe:
        return tree2[node]
    
    t1 = query2(s, (s+e)//2, 2*node, fs, fe)
    t2 = query2((s+e)//2+1, e, 2*node+1, fs, fe)
    if t1 == False:
        return t2
    if t2 == False:
        return t1
    
    v1 = P[t1][1]
    v2 = P[t2][1]
    if v1 < v2:
        return t2
    else:
        return t1


def lower_bound(lst, target):
    s, e = 1, len(lst)
    while s < e:
        m = (s+e)//2
        if lst[m][0] < target:
            s = m+1
        else:
            e = m
    return e


P = [[-1000000000,0]]
ytoi = defaultdict(list)
for n in range(N):
    Y, p = map(int, input().split())
    ytoi[Y] = n+1
    P.append([Y, p]) 
init1(1, N, 1)
init2(1, N, 1)
M = int(input())
for m in range(M):
    sy, ey = map(int, input().split())
    fs, fe = lower_bound(P, sy), lower_bound(P, ey)
    if ytoi[sy] == fs and ytoi[ey] == fe: # 둘 다 있을 경우
        if fe - fs == ey - sy: # 그 사이 모든 년도에 대한 정보가 있음
            if fe == query2(1, N, 1, fs+1, fe) and P[fs][1] >= P[fe][1]:
                print("true")
            else:
                print("false")
        else:
            if fe == query2(1, N, 1, fs+1, fe) and P[fs][1] >= P[fe][1]:
                # if P[fs][1] == 1:
                #     print("false")
                # else:
                print("maybe")
            else:
                print("false")

    elif ytoi[sy] == list() and ytoi[ey] == fe:
        if fe == query2(1, N, 1, fs, fe):
            print("maybe")
        else:
            print("false")
    elif ytoi[sy] == fs and ytoi[ey] == list():
        if fs == query1(1, N, 1, fs, fe-1):
            # if P[fs][1] == 1:
            #     if ey == sy+1:
            #         print("maybe")
            #     else:
            #         print("false")
            # else:
            print("maybe")
        else:
            print("false")

    elif ytoi[sy] == list() and ytoi[ey] == list(): # 두 년도에 대한 정보 모두 없을 경우
        print("maybe")
                 
     
    
