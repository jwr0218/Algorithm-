
#2133
n = int(input())

dp = [ 0 for _ in range(31)]
dp[0] = 1
dp[2] = 3


for i in range(4, n+1 , 2):
    dp[i] = dp[2] * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2
#print(dp)
print(dp[n])