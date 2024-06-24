from itertools import permutations

arr = list(input())
cnt=0

def fact(x):
    if x==0:
        return 1
    return fact(x-1) * x

for p in permutations(arr,len(arr)):
    is_lucky=True
    list_p = list(p)
    a=list_p[0]
    for i in list_p[1:]:
        if a==i:
            is_lucky = False
            break
        else:
            a=i
    if is_lucky:
        cnt+=1

for i in range(ord('a'), ord('z')+1):
    cnt //=fact(arr.count(chr(i)))

print(cnt)

