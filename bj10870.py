import sys
input = lambda: sys.stdin.readline().rstrip()


n = int(input())

if n==0:
    print(0)
elif 0<n<=2:
    print(1)
else:
    visited = [-1] * (n+1)
    visited[0] = 0
    visited[1] = 1
    visited[2] = 1

    for i in range(1,n-1):
        visited[i+2] = visited[i]+visited[i+1]



    print(visited[n])