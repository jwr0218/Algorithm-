n = int(input())

wine = [0 for _ in range(n)]
dp = [0 for _ in range(n)]
check = [False for _ in range(n)]
for _ in range(n):
    w = int(input())
    wine[_]  = w

for i in range(n):
    if n == 1:
        dp[i] = wine[i]
        break

    if i < 2:
        dp[i] = sum(wine[:i+1])

    else:
        dp[i] = max(dp[i-1] , dp[i-2] + wine[i] , dp[i-3] + wine[i-1] + wine[i])

    #print(dp)
        # 앞 두개 먹었을 때 ( 빼야함 )

print(dp[-1])
# 점화식 구하는 방법 공부하기!