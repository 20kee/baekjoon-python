N = int(input())
M = int(input())
xs = list(map(int, input().split()))
minimum = 0
for i, x in enumerate(xs):
    if i == 0:
        if x > minimum:
            minimum = x
    
    if i == len(xs)-1:
        if N-x > minimum:
            minimum = N-x
    else:
        if (xs[i+1]-x+1)//2 > minimum:
            minimum = (xs[i+1]-x+1)//2
print(minimum)
        
