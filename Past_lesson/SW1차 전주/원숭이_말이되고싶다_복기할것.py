import sys
from collections import deque
import heapq
input = sys.stdin.readline
n = int(input())
C , R = map(int,input().split())
        # r,c,말,원,총
queue = [[0,0,n,0]]
queue = deque(queue)

Map = []
Visited = [[[0 for SS in range(n+1)] for i in range(C)] for _ in range(R)]
for i in range(R):
    Map.append(list(map(int,input().split())))

Visited[0][0][n] = 1
moveHorse = [[-1,-2],[-2,-1],[2,-1],[-1,2],[-2,1],[1,-2],[1,2],[2,1]]
moveMonkey = [[1,0],[-1,0],[0,1],[0,-1]]
ans = 1000000000

while queue:
    now = queue.popleft()
    horse = False
    if now[0] == R-1 and now[1] == C-1:

        ans = min(now[3],ans)
        break
    for i in moveMonkey:
        n_r = now[0] + i[0]
        n_c = now[1] + i[1]
        if n_r >=R or n_c >= C or n_r < 0 or n_c < 0 :
            continue
        if Map[n_r][n_c] == 0 and Visited[n_r][n_c][now[2]] == 0 :
            Visited[n_r][n_c][now[2]] = 1
            queue.append([n_r,n_c,now[2],now[3]+1])
    if now[2] >0:
        for i in moveHorse:
            n_r = now[0] + i[0]
            n_c = now[1] + i[1]
            if n_r >= R or n_c >= C or n_r < 0 or n_c < 0:
                continue
            if Map[n_r][n_c] == 0 and Visited[n_r][n_c][now[2]-1] == 0:
                Visited[n_r][n_c][now[2]-1] = 1
                queue.append([n_r, n_c, now[2]-1,  now[3] + 1])


if ans == 1000000000:
    print(-1)
else:
    print(ans)