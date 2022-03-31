import sys
import heapq
input = sys.stdin.readline

N , M ,X = map(int,input().split())

Map = [[] for i in range(N)]

for i in range(M):
    fr, to , cost = map(int,input().split())
    fr -=1
    to -=1
    Map[fr].append([to,cost])
INF = 1e9
dist = [INF for i in range(N)]

def dijkstra(start):

    queue = [start]
    dist[start] = 0
    while queue:
        now = heapq.heappop(queue)
        for next ,cost in Map[now]:
            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                heapq.heappush(queue,next)


def dijkstra2(start,end):
    dist = [INF for i in range(N)]
    queue = [start]
    dist[start] = 0
    while queue:
        now = heapq.heappop(queue)
        for next ,cost in Map[now]:
            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                heapq.heappush(queue,next)
    return dist[end]

dijkstra(X-1)
MAX = 0

for i in range(N):
    MAX  = max(MAX,dist[i] + dijkstra2(i,X-1))
print(MAX)




