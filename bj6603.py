from itertools import combinations
import sys
input = lambda: sys.stdin.readline().rstrip()


while True:
    nums = list(map(int,input().split()))
    cnt = nums.pop(0)

    
    if cnt == 0:
        break

    items =combinations(nums,6)

    for item in items:
        print(" ".join(map(str, item)))
    print()
        

# from itertools import combinations

# while True:
# 	I = list(map(int, input().split()))

# 	k = I[0]
# 	arr = I[1:]
# 	if k == 0:
# 		break

# 	for comb in combinations(arr, 6):
# 		for u in comb:
# 			print(u, end=' ')
# 		print()
# 	print()