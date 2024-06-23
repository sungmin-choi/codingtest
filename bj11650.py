
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]


answer = sorted(arr)

for i in answer:
    print(" ".join(map(str,i)))