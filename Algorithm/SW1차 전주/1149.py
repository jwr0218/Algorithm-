import sys
input = sys.stdin.readline
N = int(input())

cost = []
for i in range(N):
    cost.append(list(map(int,input().split())))



dp = [[0] * 3 for _ in range(N)]
dp[N-1] = cost[-1]

for i in range(N-2,-1,-1):
    #R
    R = dp[i+1][1:]
    dp[i][0] = min(R) + cost[i][0]
    G = dp[i+1][:1]
    G.append(dp[i+1][2])
    dp[i][1] = min(G) + cost[i][1]
    B = dp[i+1][:2]
    dp[i][2] = min(B) + cost[i][2]

print(min(dp[0]))