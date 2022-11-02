N = int(input())
count = [0, 0]
for n in range(1, N+1):
    while n%2 == 0:
        count[0] += 1
        n //= 2
    while n%5 == 0:
        count[1] += 1
        n //= 5

print(min(count))