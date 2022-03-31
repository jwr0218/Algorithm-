import sys


N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
dp = [[0] * N for _ in range(2)]
# dp[0][i] : 특정 원소를 제거하지 않은 경우
# dp[1][i] : 특정 원소를 제거한 경우

dp[0][0] = nums[0] # 1개는 반드시 선택해야 한다.

if N > 1:

    for i in range(1,N):
        dp[0][i] = max(dp[0][i-1]+nums[i],nums[i])
        dp[1][i] = max(dp[0][i-1] , dp[1][i-1] + nums[i] )

    print(dp)

else: # N이 1인 경우는 반드시 선택을 해야하므로 dp[0][0] 출력
    print(dp[0][0])