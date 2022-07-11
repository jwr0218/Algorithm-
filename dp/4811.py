import sys
import heapq
from collections import deque

input = sys.stdin.readline

while True:

    N = int(input())

    if N == 0:
        break

    Map = [[0 for i in range(N+1)] for j in range(N+1)]

    Map[0][0] = 1

    for i in range(N+1):
        Map[0][i] = 1


    for  r in range(1,N+1):
        for c in range(r,N+1):
            if r > c :
                continue
            Map[r][c] = Map[r-1][c] + Map[r][c-1]



    print(Map[N][N])