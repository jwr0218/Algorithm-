import sys
input = sys.stdin.readline
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
dp = [0 for i in range(N+1)]
for i in range(N-1,-1,-1):
    if lst[i][0] + i > N:
        if i == N-1:
            continue
        dp[i] = dp[i+1]
    else:

        dp[i] = max(dp[i+1],lst[i][1] + dp[lst[i][0]+i])



print(dp[0])
