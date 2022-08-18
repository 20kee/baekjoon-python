from itertools import product
import sys
N = int(input())
ad = []
for i in range(5):
    ad.append(list(input()))
set_list = [{1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 14, 15},
                                    {3, 6, 9, 12, 15},
                {1, 2, 3, 6, 7, 8, 9, 10, 13, 14, 15},
                {1, 2, 3, 6, 7, 8, 9, 12, 13, 14, 15},
                        {1, 3, 4, 6, 7 ,8, 9, 12, 15},
                {1, 2, 3, 4, 7, 8, 9, 12, 13, 14, 15},
            {1, 2, 3, 4, 7, 8, 9, 10, 12, 13, 14, 15},
                              {1, 2, 3, 6, 9, 12, 15},
         {1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15},
             {1, 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 15}]

num_set = [set() for n in range(N)]
for n in range(5):
    for m in range(4*N - 1):
        if ad[n][m] == "#":
            num_set[m//4].add(1 + 3*n+ m%4)
candis = [[] for n in range(N)]
for n in range(N):
    for i in range(10):
        if num_set[n] <= set_list[i]:
            candis[n].append(i)


answer = 0.0
total = 0
all_multi = 1
for c in candis:
    all_multi *= len(c)

for n in range(N):
    e1 = sum(candis[n])
    try:
        e2 = all_multi // len(candis[n])
    except:
        print(-1)
        exit(0)
    answer += e1 * e2 * 10**(N-n-1)

answer /= all_multi

if answer == 0:
    print(-1)
    exit(0)
print(answer)