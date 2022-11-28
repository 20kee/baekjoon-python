T = int(input())
for t in range(T):
    S, A, B = list(input()), 0, 0
    s = S[0]
    count = 0
    counts = []
    for e in S:
        if e != s:
            counts.append(count)
            count = 1
            s = e
        else:
            count += 1
    counts.append(count)
print("컴맹 김소희")
    

