N = int(input())
words = []
for n in range(N):
    words.append(list(input()))

words.sort()
answer = N
for n in range(N-1):
    if len(words[n]) <= len(words[n+1]):
        if words[n] == words[n+1][:len(words[n])]:
            answer -= 1
        
print(answer)
