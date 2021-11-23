import sys


alphabet = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
            'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0,
            'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
N = int(sys.stdin.readline())
num = [9,8,7,6,5,4,3,2,1,0]
arr = [0 for i in range(N)]
result = 0

for i in range(N):
    arr[i] = sys.stdin.readline().rstrip()

for i in range(N):
    for j in range(len(arr[i])):
        alphabet[arr[i][j]] += 10**(len(arr[i])-j-1)
sorted_alphabet = sorted(alphabet.items(), key = lambda item: item[1], reverse = True)

while sorted_alphabet:
    result += sorted_alphabet[0][1]*num[0]
    del sorted_alphabet[0]
    del num[0]
    if sorted_alphabet[0][1] == 0:
        break
print(result)