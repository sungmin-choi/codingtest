# 세 종목 곱해서 작은 수 우선
# 두 선수 점수 같을 시 세 종목 합산 점수가 낮은 선수 우선
# 두 경우 다 같으면 등번호 낮은 선수가 우선



N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]


infos = sorted(arr, key=lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

for b,p,q,r in infos[:3]:
    print(b, end=' ')

# sort_arr = []


# for a in arr:
#     cur_arr = []
#     cur_arr.append(a[1]*a[2]*a[3])
#     cur_arr.append(a[1] + a[2] + a[3])
#     cur_arr.append(a[0])
#     sort_arr.append(cur_arr)



# answer = sorted(sort_arr)


# print(" ".join(map(str,list(map(lambda x: x[2], answer[0:3])))))
    