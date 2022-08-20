def get_dis_to_reaf(n, N):
    global W
    if n*2 > N:
        return 0
    
    return get_dis_to_reaf(2*n, N) + W[2*n-1]

def set_weight(n, N):
    global W
    if n*2 > N:
        pass
    else:
        set_weight(2*n, N)
        set_weight(2*n+1, N)
        a = get_dis_to_reaf(2*n, N) + W[2*n-1]
        b = get_dis_to_reaf(2*n+1, N) + W[2*n]
        if a < b:
            W[2*n-1] += b-a
        else:
            W[2*n] += a-b
        
        

H = int(input())
N = 2**(H+1) - 1
W = [0] + list(map(int, input().split()))
to_reaf = [0 for n in range(N)]
set_weight(1, N)
print(sum(W))
    

