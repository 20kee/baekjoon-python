T = int(input())
for t in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    lst1 = [logs[i] for i in range(len(logs)) if i % 2 == 0]
    lst2 = [logs[i] for i in range(len(logs)) if i % 2 == 1]
    lst2.reverse()
    lst1.extend(lst2)

    answer = 0
    for i in range(len(lst1) - 1):
        if abs(lst1[i] - lst1[i + 1]) > answer:
            answer = abs(lst1[i] - lst1[i + 1])

    if abs(lst1[0] - lst1[-1]) > answer:
        answer = abs(lst1[0] - lst1[-1])
    print(answer)
