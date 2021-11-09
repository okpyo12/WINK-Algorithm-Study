import sys

N, K = map(int, sys.stdin.readline().split())

arr = [[0,0]]
matrix = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    arr.append([W,V])

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = arr[i][0] 
        value = arr[i][1]
       
        if j < weight:
            matrix[i][j] = matrix[i - 1][j]
        else:
            matrix[i][j] = max(value + matrix[i - 1][j - weight], matrix[i - 1][j])

print(matrix[N][K])