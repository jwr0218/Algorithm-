import sys
import heapq
from collections import deque

input = sys.stdin.readline
N , K = map(int,input().split())

INF  = 1e9
dist = [[INF,0] for i in range(100001)]

queue = deque([N])
dist[N][0] = 0
dist[N][1] = 1

while queue:

    now = queue.popleft()

    for i in (now+1,now-1,now*2):
        if i < 0 or i > 100000:
            continue
        if dist[i][0] == INF:
            dist[i][0] = dist[now][0]+1
            dist[i][1] += dist[now][1]
            queue.append(i)
        elif dist[i][0] == dist[now][0]+1:
            dist[i][1] +=dist[now][1]

print(dist[K][0])
print(dist[K][1])



