import sys

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

sorted_arr = sorted(arr)
result = 0
idx_a = 0
idx_b = 0
zero = 0

for i in sorted_arr:
    if i < 0:
        idx_a += 1
    elif i > 0:
        idx_b += 1
    else:
        zero += 1


while idx_a > 0:
    if idx_a == 1:
        if zero > 0:
            del sorted_arr[0]
            del sorted_arr[0]
            idx_a -= 1
            zero -= 1
            break
        else:
            result += sorted_arr[0]
            del sorted_arr[0]
            idx_a -= 1
            break
    else:
        result += sorted_arr[0] * sorted_arr[1]
        idx_a -= 2
        del sorted_arr[0]
        del sorted_arr[0]

for i in range(zero):
    del sorted_arr[0]

while idx_b > 0:
    if idx_b == 1:
        result += sorted_arr[0]
        del sorted_arr[0]
        idx_b -= 1
        break
    else:
        if sorted_arr[-1] == 1 or sorted_arr[-2] == 1:
            result += (sorted_arr[-1] + sorted_arr[-2])
        else:
            result += sorted_arr[-1] * sorted_arr[-2]
        idx_b -= 2
        del sorted_arr[-1]
        del sorted_arr[-1]

print(result)