N = int(input())
ips = []
for n in range(N):
    ips.append(list(map(int, input().split("."))))


def convert_ip(ip):
    bin_ip = [0, 0, 0, 0]
    for n in range(4):
        bin_ip[n] = "{:8}".format(bin(ip[n])[2:])
    return bin_ip


i = 0
for ip in ips:
    ips[i] = convert_ip(ip)
    i += 1

m = 32
temp = True
for n in range(32):
    if temp:
        for k in range(len(ips) - 1):
            if ips[k][n // 8][n % 8] != ips[k + 1][n // 8][n % 8]:
                temp = False
                break
            if k == len(ips) - 2:
                m = 31 - n
answer = ["", "", "", ""]
for n in range(32 - m):
    answer[n // 8] += ips[0][n // 8][n % 8]
for n in range(32 - m, 32):
    answer[n // 8] += "0"
mask = ["", "", "", ""]
for n in range(32 - m):
    mask[n // 8] += "1"
for n in range(32 - m, 32):
    mask[n // 8] += "0"

if len(ips) == 1:
    answer = ips[0]
    mask = ["11111111", "11111111", "11111111", "11111111"]

for i in range(4):
    answer[i] = str(int(answer[i], 2))
    mask[i] = str(int(mask[i], 2))
print(".".join(answer))
print(".".join(mask))
