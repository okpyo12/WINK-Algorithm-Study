import sys

def merge(a,b):
    global cnt

    la,lb=len(a),len(b)
    i,j=0,0
    temp=[]
    while i<la and j<lb:
        if a[i]>b[j]:
            temp.append(b[j])
            j+=1
            cnt+=la-i
        else:
            temp.append(a[i])
            i+=1
    if i==la:
        temp.extend(b[j:])
    else:
        temp.extend(a[i:])
    return temp

def merge_sort(A):
    if len(A)<=1:
        return A
    left=0
    right=len(A)-1
    mid=(left+right)//2
    return merge(merge_sort(A[left:mid+1]),merge_sort(A[mid+1:]))

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
cnt = 0
merge_sort(A)
print(cnt)