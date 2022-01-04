import sys
from collections import deque
 
N, M = map(int, sys.stdin.readline().split())
arr = []
 
for i in range(M):
    arr.append(sys.stdin.readline())
 
dist = [[-1]*N for _ in range(M)]
dist[0][0] = 0
q = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q.append([0, 0])
 
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx>=0 and nx<M and ny >=0 and ny<N:
            if dist[nx][ny] == -1:
                if arr[nx][ny] == '0':
                    q.appendleft([nx, ny])
                    dist[nx][ny] = dist[x][y]
                elif arr[nx][ny] == '1':
                    q.append([nx, ny])
                    dist[nx][ny] = dist[x][y]+1
 
print(dist[M-1][N-1])