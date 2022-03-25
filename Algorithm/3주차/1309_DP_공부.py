n = int(input())
dp = [1,3] + [0]*(n-1)
for i in range(2,n+1):
    dp[i] = (dp[i-2] + dp[i-1]*2)%9901
print(dp[n])



# 점화식 구하는 방법 공부하기!