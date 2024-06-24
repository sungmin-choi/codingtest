from itertools import permutations

balls = list(permutations([1,2,3,4,5,6,7,8,9],3))



N = int(input())

calls = [list(map(int,input().split())) for _ in range(N)]

for call in calls:
    num, s, b = call
    str_num = str(num)
    for i in range(len(balls)):
        if balls[i] == False:
            continue
        else:
            cs=0
            cb=0
            x,y,z = balls[i]
            if x == int(str_num[0]):
                cs+=1
            elif str(x) in str_num:
                cb+=1
            if y == int(str_num[1]):
                cs+=1
            elif str(y) in str_num:
                cb+=1
            if z == int(str_num[2]):
                cs+=1
            elif str(z) in str_num:
                cb+=1
            if s != cs or b !=cb:
                balls[i]=False


cnt =0

for i in balls:
    if i != False:
        cnt+=1

print(cnt)