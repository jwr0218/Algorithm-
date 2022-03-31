import sys
import heapq
input = sys.stdin.readline

N , M = map(int,input().split())

Map =  []
for i in range(M):
    tmp = list(map(int,input().split()))
    Map.append(tmp)
INF =  1e9
dist = [INF for i in range(N)]

def bellman(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            fr , to , weight = Map[j]
            fr -=1
            to -=1

            if dist[fr] != INF and dist[to] > dist[fr] + weight:
                dist[to] =  dist[fr] + weight
                if i ==N-1:
                    return False
    return True

boo = bellman(0)
dist = dist[1:]

for i in range(len(dist)):
    if dist[i] == INF:
        dist[i] = -1

#dist.sort(reverse=True)

if boo == False:
    print(-1)
else:

    for i in dist:
        print(i)