import sys
from collections import deque
import re
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N , K = map(int,input().split())
    Ds = list(map(int,input().split()))

    graph = [[] for i in range(N)]
    dp = [Ds[i] for i in range(N)]
    start = []

    inDegree = [ 0 for i in range(N)]

    for i in range(K):
        fr, to  = map(int,input().split())
        start.append(fr-1)
        graph[fr-1].append(to-1)
        inDegree[to-1] +=1
    queue = []
    queue = deque(queue)

    for i in range(N):  # 진입차수 0인거 찾아서 큐에 넣기
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] =Ds[i]



    #print(queue)
    for i in start:

        while queue:
            now = queue.popleft();
            for to in graph[now]:
                #to로 진입 했음
                inDegree[to] -= 1
                #총 N번 접근 했는데도 남아 있다? 다른 곳에서 들어올 곳이 있다는 것.
                #0이 된다면 진입차수가 0이 되어 여기서 시작되어야 한다는 뜻.
                if dp[to] < dp[now] + Ds[to] :
                    dp[to] = dp[now] + Ds[to]
                if inDegree[to] == 0 :
                    queue.append(to)

    final = int(input())
    print(dp[final-1])



