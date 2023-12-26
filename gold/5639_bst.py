import sys
sys.setrecursionlimit(100000)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

def lower_bound(lst, N):
    s, e = 0, len(lst)
    while s < e:
        m = (s+e)//2
        if lst[m] <= N:
            s = m+1
        else:
            e = m
    return e;   

def pretopost(preorder):
    if len(preorder) == 1:
        print(preorder[0])
    elif len(preorder) > 1:
        i = lower_bound(preorder, preorder[0])
        if i > 1:
            pretopost(preorder[1:i])
        if i < len(preorder):
            pretopost(preorder[i:])
        print(preorder[0])

pretopost(preorder)