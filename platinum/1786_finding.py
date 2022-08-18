def failure_function(n):
    fail = [0] * len(n)
    matched = 0
    for i in range(1, len(n)):
        while matched > 0 and n[i] != n[matched]:
            matched = fail[matched - 1]

        if n[i] == n[matched]:
            matched += 1
            fail[i] = matched
            
    return fail

def kmp(s, p, failure):
    answer = []
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = failure[j-1]

        if s[i] == p[j]:
            if j == len(p)-1:
                answer.append(i+1-len(p)+1)
                j = failure[j]
            else:
                j += 1

    return answer

s = list(input())
p = list(input())

failure = failure_function(p)
answer = kmp(s, p, failure)
print(len(answer))
for e in answer:
    print(e, end=" ")