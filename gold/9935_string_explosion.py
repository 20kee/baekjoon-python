S = list(input())
E = list(input())
L = len(E)
l = 0
stack = []
dp = []
for s in range(len(S)):
    stack.append(S[s])
    if stack[-1] == E[l]:
        l += 1
    else:
        if stack[-1] == E[0]:
            l = 1
        else:
            l = 0

    dp.append(l)
    if l == L:
        for i in range(L):
            stack.pop()
            dp.pop()
        if len(dp) > 0:
            l = dp[-1]
        else:
            l = 0
if stack == []:
    print("FRULA")
else:
    print(''.join(stack))