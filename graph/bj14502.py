import sys
from queue import Queue
import copy

input = sys.stdin.readline
mx = 0
n, m = map(int, input().split())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))




def bfs():
    global mx
    cop = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            cop[i][j] = lst[i][j]
    que = Queue()

    for i in range(n):
        for j in range(m):
            if cop[i][j]==2:
                que.put([ i , j ])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while que.empty() == False:
        l = que.get()

        for x , y in zip(dx,dy):
            ax = l[0]+x
            ay = l[1]+y
            if ax >= 0 and ax <n and ay>=0 and ay<m:
                if cop[ax][ay] == 0:
                    que.put( [ax,ay] )
                    cop[ax][ay] = 2
               


    cnt = 0
    for i in range(n):
        cnt += len(list(filter(lambda x: x==0, cop[i])))

    mx = max( mx , cnt )

    return




def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0:
                lst[i][j] = 1
                wall(cnt + 1)
                lst[i][j] = 0

# 전체 범위를 다 1 씩 놓는 알고리즘 wall,,, dfs로 최적 벽을 세우는 방법은 없을까?


wall(0)
print(mx)

