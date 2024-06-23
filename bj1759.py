from itertools import combinations
import sys

input = lambda: sys.stdin.readline().rstrip()

l,c = map(int,input().split())

arr = list(input().split())
arr.sort()




for list in list(combinations(arr,l)):
    # res = "".join(list)
    cnt_1=0
    for a in ['a','e','i','o','u']:
        if a in list:
            cnt_1 +=1
    if cnt_1 >0 and l-cnt_1 >=2:
        print("".join(list))

   