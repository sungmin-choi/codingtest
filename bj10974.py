from itertools import permutations



n = int(input())


arr = [i for i in range(1,n+1)]

for items in list(permutations(arr,n)):
    # print(" ".join(map(str,items)))
    for item in items:
        print(item, end=" ")
    print()

