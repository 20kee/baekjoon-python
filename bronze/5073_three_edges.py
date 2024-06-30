while True:
    a, b, c = map(int, input().split())
    if a == 0: 
        break
    if a == b and b == c:
        print("Equilateral")
    elif max(a, b, c) >= sum([a, b, c]) - max(a, b, c):
        print("Invalid")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")