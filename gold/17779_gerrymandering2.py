
N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
answer = 10000000
for x in range(N-2):
    for y in range(1, N-1):

        for d1 in range(1, N):
            if y - d1 < 0:
                continue
            for d2 in range(1, N):
                if y + d2 >= N or x + d1 + d2 >= N:
                    continue
                
                temp = [0, 0, 0, 0, 0]
                left_bound = y
                right_bound = y
                left_extension = -1
                right_extension = 1

                for r in range(N):
                    if r < x:
                        for c in range(N):
                            if c <= y:
                                temp[0] += people[r][c]
                            else:
                                temp[1] += people[r][c]

                    elif r > x + d1 + d2:
                        for c in range(N):
                            if c < y - d1 + d2:
                                temp[2] += people[r][c]
                            else:
                                temp[3] += people[r][c]

                    else:
                        if r == x + d1:
                            left_extension = 1

                        for c in range(N):
                            if c < left_bound:
                                if left_extension == -1:
                                    temp[0] += people[r][c]
                                else:
                                    temp[2] += people[r][c]
                            elif left_bound <= c and c <= right_bound:
                                temp[4] += people[r][c]
                            else:
                                if right_extension == 1:
                                    temp[1] += people[r][c]
                                else:
                                    temp[3] += people[r][c]
                        
                        if r == x + d2:
                            right_extension = -1

                        left_bound += left_extension
                        right_bound += right_extension


                temp_answer = max(temp) - min(temp)
                if temp_answer < answer:
                    answer = temp_answer

print(answer)
                
                
         