from collections import deque

def solution(prices):
    answer = []
    dq = deque(i for i in prices)
    while dq:
        cnt = 0
        num = dq.popleft()
        for i in dq:
            if i >= num:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer