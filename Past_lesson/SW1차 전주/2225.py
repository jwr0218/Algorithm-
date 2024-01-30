import sys
input = sys.stdin.readline

N , K = map(int,input().split())

dp = [[ 0 for i in range(N+1)] for _ in range(K)]


for i in range(N+1):
    dp[0][i] = 1

for i in range(1,K):
    for j in range(0,N+1):
        if j == 0:
            dp[i][j] = 1
        else:
            for k in range(j+1):
                dp[i][j] += dp[i-1][k]
#    print(dp)

#print(dp)

print(dp[-1][-1] % 1000000000)