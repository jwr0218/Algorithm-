import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())

nums = list(map(int,input().split()))

dp = [1 for i in range(N)]

for i in range(1,N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i] , dp[j] + 1)
            #print(dp)


print(max(dp))
