T = int(input())
for t in range(T):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0
    nx, ny = 0, 0
    bx, sx, by, sy = 0, 0, 0, 0
    control = list(input())
    for c in control:
        if c == "F":
            nx += dx[d]
            ny += dy[d]

        elif c == "B":
            nx -= dx[d]
            ny -= dy[d]

        elif c == "L":
            d -= 1
            if d == -1:
                d = 3
        else:
            d += 1
            if d == 4:
                d = 0
            
        if nx > bx:
            bx = nx
        if nx < sx:
            sx = nx
        if ny > by:
            by = ny
        if ny < sy:
            sy = ny

        
    print((bx-sx)*(by-sy))
        
        