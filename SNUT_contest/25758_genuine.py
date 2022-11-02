N = int(input())
lst = list(set(list(input().split())))
answer = set()
for n in range(len(lst)):
    for m in range(n+1, len(lst)):
        answer.add(max(lst[n][0], lst[m][1]))
        answer.add(max(lst[n][1], lst[m][0]))
print(len(answer))
print(*sorted(list(answer)))