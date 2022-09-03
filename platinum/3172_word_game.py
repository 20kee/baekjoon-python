import sys
input = sys.stdin.readline

def init(s, e, node):
    if s == e:
        tree[node] = valid[s-1]
    else:
        init(s, (s+e)//2, 2*node)
        init((s+e)//2 + 1, e, 2*node+1)
        tree[node] = tree[2*node] + tree[2*node+1]

def update(s, e, node, f, gap):
    if s <= f and f <= e:
        if s == f and e == f:
            tree[node] += gap
        else:
            tree[node] += gap
            update(s, (s+e)//2, 2*node, f, gap)
            update((s+e)//2+1, e, 2*node+1, f, gap)

def query(s, e, node, fs, fe):
    if fe < s or fs > e:
        return False
    if fs <= s and fe >= e:
        return tree[node]
    
    t1 = query(s, (s+e)//2, 2*node, fs, fe)
    t2 = query((s+e)//2+1, e, 2*node+1, fs, fe)
    if t1 == False:
        return t2
    if t2 == False:
        return t1
    return t1 + t2

def lower_bound(lst, target):
    s, e = 0, len(lst)
    while s < e:
        m = (s+e)//2
        if lst[m] < target:
            s = m+1
        else:
            e = m
    
    return e


N = int(input())
tree = [0] * (N*4)
words = []
re_words = []
valid = [1 for n in range(N+1)]
for n in range(N):
    words.append(input())
    re_words.append(words[n][::-1])

words.sort()
re_words.sort()
init(1, N, 1)
answer = 0
for n in range(N):
    word = words[n]
    i = lower_bound(re_words, word[::-1])
    answer += query(1, N, 1, 1, i)
    update(1, N, 1, i+1, -1)

print(answer)


