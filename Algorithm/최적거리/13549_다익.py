import sys
import heapq
input = sys.stdin.readline

N , K = map(int,input().split())

INF = 1e9

lst = [INF for i in range(100001)]
lst[N] = 0

queue = [N]


while queue:

    now = queue.pop(0)

    if now == K:
        print(lst[now])
        break
    if now < 0 or now > 100000:
        continue
    if 0<= now-1 <=100000:

        if lst[now-1] > lst[now] + 1:
            lst[now-1] = lst[now] + 1
            queue.append(now-1)
    if 0 <= now + 1 <= 100000:

        if lst[now+1] > lst[now] + 1:
            lst[now+1] = lst[now] + 1
            queue.append( now + 1)
    if 0 <= now *2 <= 100000:

        if lst[now*2] > lst[now]:
            lst[now * 2] = lst[now]
            queue.append( now*2 )
