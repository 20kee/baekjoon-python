T = int(input())
answers = []
for t in range(T):
    answer = 0
    temp = []
    numbers = list(map(int, input().split()))
    for i, number in enumerate(numbers):
        if i == 0:
            continue
        else:
            k = -1
            for j, e in enumerate(temp):
                if temp[j] > number:
                    k = j
                    break
            if k == -1:
                temp.append(number)
            else:
                answer += len(temp) - k
                temp.insert(k, number)
    
    answers.append(answer)

            
for i, answer in enumerate(answers):
    print(i+1, answer)

    