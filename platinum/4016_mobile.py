import sys
sys.setrecursionlimit(100001)

def level(n, depth):
    if lr[n][0] == -1 and lr[n][1] == -1:
        dp[n] = 0
        return [depth, depth]

    elif lr[n][0] == -1:
        t = level(lr[n][1], depth+1) # 오른쪽에 매달린 막대에 대해서 level함수 호출
        if t[1] > depth+1:
            dp[n] = -1
        else:
            dp[n] = 1
        return [depth, t[1]]

    elif lr[n][1] == -1:
        t = level(lr[n][0], depth+1)
        if t[1] > depth+1:
            dp[n] = -1
        else:
            dp[n] = 0
        return [depth, t[1]]

    else:
        t1 = level(lr[n][0], depth+1)
        t2 = level(lr[n][1], depth+1)
        if dp[lr[n][0]] == -1 or dp[lr[n][1]] == -1:
            dp[n] = -1
    
        else:
            if t1[0] == t1[1]: # 왼쪽 막대가 수평일때
                if t2[1] > t1[0]+1 or t2[0] < t1[0]-1: # 두 막대에 달린 장난감의 level 차이가 클 때
                    dp[n] = -1
                elif t2[1] > t1[0]:
                    dp[n] = dp[lr[n][1]] + 1
                elif t2[0] < t1[0]:
                    dp[n] = dp[lr[n][1]]
                else:
                    dp[n] = 0
                
            elif t2[0] == t2[1]: # 오른쪽 수평일때
                if t1[1] > t2[0]+1 or t1[0] < t2[0]-1: # level 차이가 클 때
                    dp[n] = -1
                elif t1[1] > t2[0]:
                    dp[n] = dp[lr[n][0]]
                elif t1[0] < t2[0]:
                    dp[n] = dp[lr[n][0]] + 1
                else:
                    dp[n]  = 0
            else:
                dp[n] = -1
        return [min(t1[0], t2[0]), max(t1[1], t2[1])]


N = int(input())
lr = [[-1, -1]]
for n in range(N):
    lr.append(list(map(int, input().split())))
dp = [0 for n in range(N+1)]
t = level(1, 1)
print(dp[1])


