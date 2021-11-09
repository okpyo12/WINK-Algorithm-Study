def solution(n):
    answer = [[0]*i for i in range(1,n+1)]
    
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
                answer[x][y] = num
                num += 1
            elif i % 3 == 1:
                y += 1
                answer[x][y] = num
                num += 1
            else:
                x -= 1
                y -= 1
                answer[x][y] = num
                num += 1
    result = []
    for i in answer:
        for j in i:
            result.append(j)
    return result

n = 4
print(solution(n))