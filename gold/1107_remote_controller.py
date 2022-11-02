from collections import defaultdict
from operator import truediv
N = int(input())
M = int(input())
broken = defaultdict(int)
if M != 0:
    for e in list(input().split()):
        broken[e] = 1

def possible(N):
    N = list(str(N))
    for e in N:
        if broken[e]:
            return False
    return True

temp1 = N
answer1 = 999999
while temp1 != 1000001:
    if possible(temp1):
        answer1 = temp1 - N + len(str(temp1))
        break
    temp1 += 1

temp2 = N
answer2 = 999999
while temp2 != -1:
    if possible(temp2):
        answer2 = N - temp2 + len(str(temp2))
        break
    temp2 -= 1

answer3 = abs(N-100)
print(min(answer1, answer2, answer3))    
