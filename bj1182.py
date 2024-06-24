from itertools import combinations



N,S = map(int, input().split())
arr = list(map(int,input().split()))

cnt=0

for i in range(1,N+1):
    subs_s = list(combinations(arr,i))
    for s in subs_s:
        if sum(list(s)) == S:
            cnt+=1

print(cnt)



    