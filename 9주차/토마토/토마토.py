import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

queue = deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append([i, j, k])

dx, dy, dz = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]

def bfs():
    while queue:
        z,x,y=queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    queue.append([nz, nx, ny])

bfs()
z = 1
result = -1

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                z = 0
            result = max(result,k)

if z == 0: #모두 익지 못한 상태
    print(-1)
elif result == 1: #모두 익어있던 상태 
    print(0)
else:
    print(result-1)