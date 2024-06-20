import sys
input = lambda: sys.stdin.readline().rstrip()


# n = input()





def solution(n):
    if n == 0:
        return '-'
    else:
        return solution(n-1) + (' ' * 3**(n-1)) + solution(n-1)


while True:
    try:
        n = int(input())
        print(solution(n))
    except:
        break

