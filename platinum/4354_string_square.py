def get_divisor(N):
    lst = []
    s = 1
    while s*s <= N:    
        if N%s == 0:
            lst.append(s)
            lst.append(N//s)
        s += 1
    
    return lst

while True:
    S = input()
    if S[0] == '.':
        break

    lst = sorted(get_divisor(len(S)))
    for l in lst:
        if S[:l] * (len(S)//l) == S:
            print(len(S)//l)
            break

    
    