import sys
import heapq
input = sys.stdin.readline

col,row = map(int,input().split())
Map = []
cost = [[99999 for j in range(col)] for i in range(row)]
for i in range(row):

    Map.append(list(map(int,input().replace("\n",""))))
queue = []

heapq.heappush(queue,[0,0])

move = [[1,0],[0,1],[-1,0],[0,-1]]

#움직이는 방향은 오른쪽, 왼쪽만
cost[0][0] = 0
while queue:

    now = heapq.heappop(queue)
    for m in move:
        if now[0] + m[0] >= row or now[0] + m[0] < 0 or now[1] + m[1] >= col or now[1] + m[1] < 0:
            continue
        new_cost = cost[now[0]][now[1]] + Map[now[0]+m[0]][now[1]+m[1]]
        if new_cost < cost[now[0]+m[0]][now[1]+m[1]]:
            cost[now[0] + m[0]][now[1] + m[1]] = new_cost
            heapq.heappush(queue,[now[0] + m[0],now[1] + m[1]])


print(cost[row-1][col-1])


