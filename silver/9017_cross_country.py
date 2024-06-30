T = int(input())
for t in range(T):
    N = int(input())
    team_count = [0 for _ in range(201)]
    team_score = [[0, 0, 0, n] for n in range(201)]
    team_numbers = list(map(int, input().split()))
    for n in range(1, 201):
        team_count[n] = team_numbers.count(n)
    
    rank = 1
    for team_number in team_numbers:
        if team_count[team_number] < 6:
            pass
        else:
            if team_score[team_number][2] == 4:
                team_score[team_number][1] = rank
            elif team_score[team_number][2] < 4:
                team_score[team_number][0] += rank
            
            team_score[team_number][2] += 1
            rank += 1

    team_score.sort()
    for score in team_score:
        if score[2] == 6:
            print(score[3])
            break
