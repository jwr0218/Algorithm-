from collections import deque



N , M = map(int,input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int,list(input()))))

queue = [[0,0]]
queue = deque(queue)

cost = [[9999 for i in range(len(Map[k]))] for k in range(len(Map))]
cost[0][0] = 1

move = [[1,0],[-1,0],[0,1],[0,-1]]

while len(queue)>0:
    
    now = queue.popleft()
    for mv in move:
        new_now =  [now[0]+mv[0],now[1]+mv[1]]
        if new_now[0] < 0 or new_now[0] >=N:
            continue
        if new_now[1] < 0 or new_now[1] >= M :
            continue
        
        # print(new_now)
        
        if Map[now[0]][now[1]] == 1 and cost[new_now[0]][new_now[1]] > cost[now[0]][now[1]] +1 :  
            queue.append(new_now)
            cost[new_now[0]][new_now[1]] = cost[now[0]][now[1]] +1
        
        
    # 
print(cost[-1][-1])
    