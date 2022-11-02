from collections import defaultdict
N, G = input().split()
N = int(N)
people = defaultdict(int)
count = 0
for n in range(N):
    name = input()
    if people[name] == 0:
        count += 1
        people[name] = 1

if G == 'Y':
    print(count//1)
elif G == 'F':
    print(count//2)
elif G == 'O':
    print(count//3)