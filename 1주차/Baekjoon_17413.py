import sys

S = sys.stdin.readline()

a = ''
temp = ''
TorF = False

def switchstr(a):
    arr = []
    result = ''
    for i in range(len(a)-1, -1, -1):
        arr.append(a[i])
    result = ''.join(arr)
    return result

for i in S:
    if i == '<':
        TorF = True
        a += switchstr(temp) + '<'
        temp = ''
    elif i == '>':
        TorF = False
        a += '>'
    elif i == ' ':
        if TorF == True:
            a += ' '
        else:
            a += switchstr(temp) + ' '
            temp = ''
    else:
        if TorF == True:
            a += i
        else:
            temp += i

a += switchstr(temp)[1:]
print(a)