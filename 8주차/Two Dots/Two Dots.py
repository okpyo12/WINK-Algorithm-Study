import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cycle = False

def dfs(x, y, cx, cy, cnt, color):
    global cycle

    if cycle:
        return

    visited[cx][cy] = 1
    if cnt >= 4 and x == cx and y == cy:
        cycle = True
        return
    
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == color and visited[nx][ny] == 0:
                dfs(x, y, nx, ny, cnt+1, color)
            elif nx == x and ny == y and cnt >= 4:
                dfs(x, y, nx, ny, cnt, color)
    return

for i in range(N):
    for j in range(M):
        visited = [[0] * M for _ in range(N)]
        visited[i][j] = 1
        dfs(i, j, i, j, 1, graph[i][j])

if cycle == True:
    print("Yes")
else:
    print("No")