import sys

N = int(sys.stdin.readline())

lst  = [[0 for _ in range(10)] for i in range(N)]

for i in range(10):
    lst[0][i] = 1

for i in range(1,N):
    for j in range(10):
        if j == 9:
            lst[i][j] = lst[i-1][j]
        else:
            lst[i][j] = sum(lst[i-1][j:])
#print(lst)
print(sum(lst[N-1])%10007)

