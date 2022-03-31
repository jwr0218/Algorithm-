import sys

input = sys.stdin.readline

N , K = map(int,input().split())

dp = [[0 for i in range(K+1)] for j in range(N+1)]

items = []
for i in range(N):
    items.append(list(map(int,input().split())))


for i in range(1,N+1):
    for j in range(K+1):
        # i 번째 아이템을 넣을때 어떤 상황일 것이냐?
        w = items[i-1][0]
        v = items[i-1][1]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
                        #   안넣었을 때 높을까?     넣었을떄 높을까?
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[N][K])
