import sys
from heapq import heappop, heappush
input = sys.stdin.readline
inf = sys.maxsize

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [inf] * (n + 1)
heap = []
def dijkstra(start):
    heappush(heap, [0, start])
    dp[start] = 0
    while heap:
        w, n = heappop(heap)  # weight, now !
        for n_n, wei in graph[n]:
            # n 노드와 연결된 그래프 ( hash를 할당해서 해결하기 )
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1]) # n 노드와 연결된 그래프
dijkstra(x)
ans = []
for i in range(1, n + 1):
    if dp[i] == k:
        ans.append(i)
if ans:
    for i in ans:
        print(i)
else:
    print(-1)
