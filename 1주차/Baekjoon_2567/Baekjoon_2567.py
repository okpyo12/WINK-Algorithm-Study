import sys

T = int(sys.stdin.readline())

arr = []
for i in range(101):
    arr.append([])
    for j in range(101):
        arr[i].append(0)

for i in range(T):
    X, Y = map(int, sys.stdin.readline().split())
    for j in range(10):
        for k in range(10):
            arr[X+j][Y+k] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            if arr[i+1][j] == 0:
                cnt += 1
            if arr[i][j+1] == 0:
                cnt += 1
            if arr[i-1][j] == 0:
                cnt += 1
            if arr[i][j-1] == 0:
                cnt += 1
print(cnt)