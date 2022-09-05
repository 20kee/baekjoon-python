N = int(input())
M = list(map(int, input().split()))
W = list(map(int, input().split()))
sm = []
tm = []
sw = []
tw = []
for n in range(N):
    if M[n] < 0:
        sm.append(-M[n])
    else:
        tm.append(M[n])

    if W[n] < 0:
        sw.append(-W[n])
    else:
        tw.append(W[n])
    
sm.sort()
tm.sort()
sw.sort()
tw.sort()

m = 0
answer = 0
for n in range(len(sm)):
    if m >= len(tw):
            break

    if tw[m] < sm[n]:
        answer += 1
        m += 1

m = 0
for n in range(len(sw)):
    if m >= len(tm):
            break

    if tm[m] < sw[n]:
        answer += 1
        m += 1

print(answer)