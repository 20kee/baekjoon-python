import math
from functools import cmp_to_key

def ccw(x, y, z):
    temp = x[0]*y[1] + y[0]*z[1] + z[0]*x[1] - x[1]*y[0] - y[1]*z[0] - z[1]*x[0]
    if temp > 0:
        return 1 # 반시계
    elif temp == 0:
        return 0 # 직선
    else:
        return -1 # 시계방향
        
def distance(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def compare(x, y):
    global first
    if x[0] == first[0] and x[1] == first[1]:
        return -1
    if y[0] == first[0] and y[1] == first[1]:
        return 1
    
    temp = ccw(first, x, y)
    if temp == 1:
        return -1
    elif temp == -1:
        return 1
    else:
        if distance(x, first) < distance(y, first):
            return 1
        else:
            return -1
        
N = int(input())
dots = []
first = [40000, 40000]
for n in range(N):
    dot = list(map(int, input().split()))
    if dot[1] < first[1]:
        first[1] = dot[1]
        first[0] = dot[0]
    elif dot[1] == first[1]:
        if dot[0] < first[0]:
            first[0] = dot[0]
    dots.append(dot)
dots.sort(key=cmp_to_key(compare))
stack = []
stack.append(dots[0])
stack.append(dots[1])
n = 2
while n <= N-1:
    f = stack[-2]
    s = stack[-1]
    if ccw(f, s, dots[n]) == 1:
        stack.append(dots[n])
    else:
        if len(stack) > 2:
            stack.pop()
            n -= 1
    n += 1

if ccw(stack[0], stack[-1], stack[-2]) == 0:
    stack.pop()
print(len(stack))