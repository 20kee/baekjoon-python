r1, c1, r2, c2 = map(int, input().split())
w = c2 - c1 + 1 # 너비
h = r2 - r1 + 1 # 높이
square = [[-1 for e in range(w)] for e in range(h)]
total_filled = w * h
r, c = 0, 0
value = 1
total_move = 1
count_move = 0
count_repeat = 0
direction = 0
drc = [[0, 1], [-1, 0], [0, -1], [1, 0]]
length = 0
while total_filled > 0:
    if r >= r1 and r <= r2 and c >= c1 and c <= c2:
        square[r-r1][c-c1] = value
        if len(str(value)) > length:
            length = len(str(value))
        # square 에 값을 집어넣음
        total_filled -= 1
    
    value += 1
    r += drc[direction][0]
    c += drc[direction][1]
    count_move += 1
    if count_move == total_move:
        count_move = 0
        direction += 1
        if direction == 4:
            direction = 0
        count_repeat += 1
        if count_repeat == 2:
            count_repeat = 0
            total_move += 1

for e in square:
    for e2 in e:
        print(f'{e2:{length}}', end=" ")
    print()
    
    
    


