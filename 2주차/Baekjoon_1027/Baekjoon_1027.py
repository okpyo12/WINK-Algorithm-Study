import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(N):
    cnt = 0
    temp = -99999999999
    for j in range(i+1, N):
        temp2 = (arr[j]-arr[i])/(j-i)
        if temp < temp2:
            cnt += 1
            temp = temp2
    result.append(cnt)
    cnt = 0
    temp = -99999999999
    for j in range(i-1, -1, -1):
        temp2 = -((arr[j]-arr[i])/(j-i))
        if temp < temp2:
            cnt += 1
            temp = temp2
    result[i] += cnt

print(max(result))