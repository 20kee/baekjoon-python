
import sys
from collections import defaultdict
input = sys.stdin.readline
N, M = map(int, input().split())
password = defaultdict(str)
for n in range(N):
    a, p = input().split()
    password[a.rstrip()] = p
for m in range(M):
    print(password[input().rstrip()])
