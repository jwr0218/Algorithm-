import sys

input = sys.stdin.readline

N , E = map(int,input().split())

INF = int(1e9)

dist = [INF for i in range(N)]

Map = []

for i in range(E):
    fr , to , cost = map(int, input().split())
    fr , to = fr-1 , to - 1
    Map.append([fr,to,cost])


def bellman(start):
    dist[start] = 0

    for i in range(N): # 모든 노드 확인

        for j in range(E): # 모든 간선 확인
            now, next , cost = Map[j]

            if dist[now]!= INF and dist[next] > dist[now] + cost: # infinity 가 아니면 이미 한번 겪었다.
                dist[next] = dist[now] + cost

                if i == N-1:
                    # N번 반복했다는 뜻은 음의 사이클이 존재한다는 뜻 !
                    return True
    return False

boo = bellman(0)

if boo:
    print(-1)
else:
    for i in range(1,len(dist)):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])

