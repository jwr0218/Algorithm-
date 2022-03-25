import sys

input = sys.stdin.readline

N ,start,end, M = map(int,input().split())

INF = -1e9

dist = [INF for i in range(N)]

Map = []

for i in range(M):
    fr , to , cost = map(int, input().split())
    Map.append([fr,to,cost])
earn = list(map(int,input().split()))
#Map.sort(key = lambda x : x[0])


def check(start,end):
    visited = [0 for i in range(N)]
    queue = [start]
    while queue:
        now = queue.pop(0)
        if now == end :
            return True

        visited[now] = 1
        for i in Map:
            if i[0] == now and visited[i[1]] == 0 :
                queue.append(i[1])
    return False


def bellman(start,end):
    dist[start] = 0 + earn[start]

    for i in range(N): # 모든 노드 확인

        for j in range(M): # 모든 간선 확인
            now, next , cost = Map[j]

            if dist[now]!= INF and dist[next] < dist[now] - cost + earn[next]: # infinity 가 아니면 이미 한번 겪었다.

                dist[next] = dist[now] - cost + earn[next]

                if i == N-1:
                    if check(now,end):
                        return True
                    # N번 반복했다는 뜻은 음의 사이클이 존재한다는 뜻 !
    return False

boo = bellman(start,end)


if dist[end] == INF:
    print("gg")
else:
    if boo:
        print("Gee")
    else:
        print(dist[end])

