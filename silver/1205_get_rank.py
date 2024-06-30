N, score, P = map(int, input().split())
if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    scores.sort()
    if N == P and score <= scores[-P]:
        print(-1)
    else:
        count = 0
        for real_score in scores:
            if real_score > score:
                count += 1
        print(count + 1)
