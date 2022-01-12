import sys

prime = [False, False] + [True] * (1299710)
for i in range(2, int(1299710**0.5)+1):
    if prime[i]:
        for j in range(i*i, 1299709+1, i):
            prime[j] = False

def isprime(num):
    cnt = 0
    for i in range(1299709):
        if prime[num-i] == False:
            cnt += 1
        else:
            break
    for i in range(1299709):
        if prime[num+i] == False:
            cnt += 1
        else:
            break
    return cnt

    
T = int(sys.stdin.readline())

for i in range(T):
    cnt = 0
    num = int(sys.stdin.readline())
    print(isprime(num))