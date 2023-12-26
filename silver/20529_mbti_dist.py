from collections import defaultdict
from itertools import combinations_with_replacement

def count_diff(mbtis):
    count = 0
    for i in range(4):
        if mbtis[0][i] != mbtis[1][i]:
            count += 1
    for i in range(4):
        if mbtis[1][i] != mbtis[2][i]:
            count += 1
    for i in range(4):
        if mbtis[0][i] != mbtis[2][i]:
            count += 1
    return count
T = int(input())
answers = [0 for _ in range(T)]
for t in range(T):
    N = int(input())
    mbti = defaultdict(int)
    for m in input().split():
        mbti[m] += 1
    answer = 100
    for data in combinations_with_replacement(mbti.keys(), 3):
        for i in range(3):
            if data.count(data[i]) <= mbti[data[i]]:
                pass
            else:
                break

            if i == 2:
                temp = count_diff(data)
                if temp < answer:
                    answer = temp

    answers[t] = answer

for answer in answers:
    print(answer)