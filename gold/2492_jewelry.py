from collections import defaultdict
import sys

N, M, T, K = map(int, input().split())
lst = []
for t in range(T):
    n, m = map(int, input().split())
    lst.append([n, m])

answer_x = 0
answer_y = 0
answer = 0
lst.sort()
for t in range(T):
    k1 = lst[t] # 1번째 보석을 밑변
    for u in range(t, T):
        temp = 0
        k2 = lst[u] # 그 다음을 오른쪽

        if k2[0] - K <= k1[0] and k1[1] -  K <= k2[1] and k2[1] <= k1[1]:  #두개를 모두 포함하는 정사각형을 생각해볼 수 있다면
            x = k1[0]
            y = k2[1]
            if x <= N-K and y <= M-K:
                temp = 0
                for v in range(T):
                    k3 = lst[v]
                    if k3[0] >= x and k3[0] <= x+K and k3[1] >= y and k3[1] <= y+K:
                        temp += 1

            else:
                if x > N-K:
                    x = N-K
                if y > M-K:
                    y = M-K
                
                temp = 0
                for v in range(T):
                    k3 = lst[v]
                    if k3[0] >= x and k3[0] <= x+K and k3[1] >= y and k3[1] <= y+K:
                        temp += 1


            if temp > answer:
                    answer_x = x
                    answer_y = y+K
                    answer = temp



print(answer_x, answer_y)
print(answer)
    



            