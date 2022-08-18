from collections import deque

origin = list(input())
N = int(input())
words = [[] for n in range(len(origin)+1)]
for n in range(N):
    word = list(input())
    if len(word) <= len(origin):
        words[len(word)].append(word)

dp = [[-1 for n in range(len(origin)+1)] for n in range(len(origin)+1)]
# dp[a:b] => a위치부터 b-1위치까지의 단어를 만드는 비용의 최솟값
for l in range(1, len(origin)+1):
    for s in range(len(origin)+1-l):
        for word in words[l]:
            str1 = sorted(origin[s:s+l])
            str2 = sorted(word)
            temp2 = True
            for n in range(l):
                if str1[n] != str2[n]:
                    temp2 = False
                    break
            if temp2:
                temp = 0
                for n in range(l):
                    if origin[s+n] != word[n]:
                        temp += 1
                if dp[s][s+l] == -1 or temp < dp[s][s+l]:
                    dp[s][s+l] = temp
        
        if l > 1:
            for mid in range(1, l):
                t1 = dp[s][s+mid]
                t2 = dp[s+mid][s+l]
                if t1 != -1 and t2 != -1:
                    if t1 + t2 < dp[s][s+l] or dp[s][s+l] == -1:
                        dp[s][s+l] = t1 + t2
                        
print(dp[0][-1])


