N, B, H, W = map(int, input().split())
prices = [0 for h in range(H)]
acs = [[] for h in range(H)]
answer = 500001
for h in range(H):
    prices[h] = int(input())
    acs[h] = list(map(int, input().split()))
    if max(acs[h]) >= N:
        if N*prices[h] < B and N*prices[h] < answer:
            answer = N*prices[h]

if answer == 500001:
    print("stay home")
else:
    print(answer)
    