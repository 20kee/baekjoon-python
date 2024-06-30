N = int(input())
states = list(map(int, input().split()))
S = int(input())
for _ in range(S):
    s, number = map(int, input().split())
    if s == 1:
        for n in range(number-1, N, number):
            states[n] = 0 if states[n] == 1 else 1
    elif s == 2:
        mid = number-1
        left = mid
        right = mid
        while True:
            left -= 1
            right += 1
            if left >= 0 and right < N:
                if states[left] != states[right]:
                    left += 1
                    right -= 1
                    break
            else:
                left += 1
                right -= 1
                break
        
        for n in range(left, right+1):
            states[n] = 0 if states[n] == 1 else 1

for i, state in enumerate(states):
    if i % 20 == 0 and i != 0:
        print()
    print(state, end=' ')