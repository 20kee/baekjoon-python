N = int(input())
L = list(map(int, input().split()))
f = input()
ans = 0
for l in L:
    ans = ans^(l-2)

if ans == 0:
    if f == "Whiteking":
        print("Blackking")
    else:
        print("Whiteking")
else:
    if f == "Whiteking":
        print("Whiteking")
    else:
        print("Blackking")