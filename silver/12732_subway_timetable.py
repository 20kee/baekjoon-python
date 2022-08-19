def time_to_int(time):
    h, m = time.split(":")
    return 60*int(h) + int(m)


N = int(input())
for n in range(N):
    T = int(input())
    A, B = map(int, input().split())
    ready_A = [0 for n in range(60*25)]
    ready_B = [0 for n in range(60*25)]
    need_A = [0 for n in range(60*25)]
    need_B = [0 for n in range(60*25)]
    now_A = 0
    now_B = 0
    answer_A = 0
    answer_B = 0

    for a in range(A):
        t1, t2 = map(time_to_int, input().split())
        need_A[t1] += 1
        ready_B[t2+T] += 1

    for b in range(B):
        t1, t2 = map(time_to_int, input().split())
        need_B[t1] += 1
        ready_A[t2+T] += 1

    for m in range(60*24):
        now_A += ready_A[m]
        now_B += ready_B[m]
        now_A -= need_A[m]
        now_B -= need_B[m]
        if now_A < 0:
            answer_A -= now_A
            now_A = 0
        if now_B < 0:
            answer_B -= now_B
            now_B = 0

    print("Case #", n+1, ": ", answer_A, " ", answer_B, sep="")



