from collections import deque

R, C = map(int, input().split())
europe = [list(input()) for _ in range(R)]

start = ()
for r in range(R):
    for c in range(C):
        if europe[r][c] == 'M':
            start = (r, c)
            break
    if len(start) == 1:
        break

def valid(r, c):
    return r >= 0 and r < R and c >= 0 and c < C


dr = [0, 0, -1, 1]  
dc = [1, -1, 0, 0]
def isPossible(pipe, i):
    if pipe == '|':
        return i >= 2, i
    elif pipe == '-':
        return i <= 1, i
    elif pipe == '+':
        return True, i
    elif pipe == '1':
        return i==2 or i==1, 0 if i == 2 else 3
    elif pipe == '2':
        return i==3 or i==1, 0 if i == 3 else 2
    elif pipe == '3':
        return i==0 or i==3, 2 if i == 0 else 1
    elif pipe == '4':
        return i==2 or i==0, 1 if i == 2 else 3
    elif pipe == '.':
        return False, 0
    elif pipe == 'Z':
        return False, 0
    
def candidates(i):
    if i == 0:
        return ['-', '3', '4', '+']
    
    if i == 1:
        return ['-', '1', '2', '+']

    if i == 2:
        return ['|', '1', '4', '+']
    
    if i == 3:
        return ['|', '3', '2', '+']


real_start = []
for i in range(4):
    r = start[0] + dr[i]
    c = start[1] + dc[i]
    if valid(r, c):
        possible, next_flow = isPossible(europe[r][c], i)
        if possible:
            real_start = [[(r,c), next_flow]]
            break

blank = [(), 0]
q = deque(real_start)
while q:
    v, i = q.popleft()
    r = v[0] + dr[i]
    c = v[1] + dc[i]

    if valid(r, c) and europe[r][c] == '.':
        blank = [(r, c), i]
        break
    else:
        q.append([(r, c), isPossible(europe[r][c], i)[1]])
        
candidate = candidates(blank[1])
count = 0
answer = ''
for candi in candidate:
    possible, i = isPossible(candi, blank[1])
    europe[blank[0][0]][blank[0][1]] = candi
    q = deque([[blank[0], i]])
    tmp = 0
    while q:
        tmp += 1
        v, i = q.popleft()
        r = v[0] + dr[i]
        c = v[1] + dc[i]
        if valid(r, c):
            if europe[r][c] == '.' or europe[r][c] == 'M':
                break
            elif europe[r][c] == 'Z' and tmp > count:
                count = tmp
                answer = candi
                break
            else:
                possible, next_flow = isPossible(europe[r][c], i)
                if possible:
                    q.append([(r, c), next_flow])

print(blank[0][0]+1, blank[0][1]+1, answer)

    
    
        

        