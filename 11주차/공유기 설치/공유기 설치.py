import sys
N, C = map(int, sys.stdin.readline().split())

array = []
for i in range(N):
    array.append(int(sys.stdin.readline()))
array.sort()

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        cnt = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                cnt += 1
                current = array[i]

        if cnt >= C:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)