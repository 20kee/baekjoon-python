from collections import defaultdict
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
words = defaultdict(int)
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words[word] += 1

real_words = []
M = 0
for k, v in words.items():
    if v > M:
        M = v


for k, v in words.items():
    real_words.append([M-v, 10-len(k), k])

real_words.sort()
for word in real_words:
    print(word[2])
