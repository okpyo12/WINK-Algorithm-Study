import sys

N, L = map(int, sys.stdin.readline().rsplit())
arr = list(map(int, sys.stdin.readline().rsplit()))
arr = sorted(arr)

cnt = 0
while arr:
    cnt += 1
    idx = 0
    while idx != len(arr)-1:
        idx += 1
        if (arr[0]-0.5)+L >= arr[idx]+0.5:
            del arr[idx]
            idx -= 1
    del arr[0]
print(cnt)