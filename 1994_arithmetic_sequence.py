from collections import defaultdict

N = int(input())
numbers = []
answer = 1
for n in range(N):
    numbers.append(int(input()))
numbers.sort()

now = defaultdict(int)

candis = [[] for n in range(N)]
for n in range(N):
    number = numbers[n]
    candis[n].append([number])
    for m in range(n):
        for i in range(len(candis[m])):
            if len(candis[m][i]) == 1:
                if now[str(number)+","+str(candis[m][i][0])] == 0:
                    candis[m].append(candis[m][i] + [number])
                    now[str(number)+","+str(candis[m][i][0])] = 1
            else:
                if candis[m][i][-1]-candis[m][i][-2] == number - candis[m][i][-1] and now[str(number)+","+str(candis[m][i][-1])] == 0:
                    now[str(number)+","+str(candis[m][i][-1])] = 1
                    candis[m][i].append(number)
                    
            if len(candis[m][i]) > answer:
                answer = len(candis[m][i])

print(answer)
