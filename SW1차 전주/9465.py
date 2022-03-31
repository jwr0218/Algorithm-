import sys
from collections import deque
import re

input = sys.stdin.readline

N = int(input())
move = [[0,1],[0,-1],[1,0],[-1,0]]
for i in range(N):
    n = int(input())
    Map = []
    dp = [[0 for __ in range(n)] for _ in range(2)]
    for _ in range(2):
        Map.append(list(map(int,input().split())))
    dp[0][0] = Map[0][0]
    dp[1][0] = Map[1][0]
    for j in range(1,n):
        dp[0][j] = max(dp[0][j-1],dp[1][j-1]+Map[0][j])
        dp[1][j] = max(dp[1][j-1],dp[0][j-1]+Map[1][j])

    print(max(dp[0][n-1],dp[1][n-1]))





