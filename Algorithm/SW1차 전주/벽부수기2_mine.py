from collections import deque
import sys

input = sys.stdin.readline
R , C , K = map(int,input().split())

check = [[[0 for x in range(K+1)] for _ in range(C)] for __ in range(R)]

Map = []
for i in range(R):
    Map.append(list(map(int,(list(input().replace("\n",""))))))

queue = [[0,0,K]]
# r, c , 몇번 부숨? , 이동한 거리
move = [[0,1],[0,-1],[1,0],[-1,0]]

queue = deque(queue)
answer = -1
while queue:
    now = queue.popleft()

    if now[0] == R-1 and now[1] == C-1:
        answer = check[now[0]][now[1]][now[2]] + 1
        break

    for i in move:
        n_r = now[0] + i[0]
        n_c = now[1] + i[1]
        if n_r < 0 or n_r >=R or n_c < 0 or n_c >=C :
            continue
        if check[n_r][n_c][now[2]] != 0:
            continue

        # 벽이 있을때
        if Map[n_r][n_c] == 1 and now[2]>0  :
            check[n_r][n_c][now[2]-1] = check[now[0]][now[1]][now[2]]+1
            queue.append([n_r,n_c,now[2]-1])

        # 벽이 없을떄
        elif Map[n_r][n_c] == 0 :
            #print("더해짐?")
            check[n_r][n_c][now[2]] = check[now[0]][now[1]][now[2]]+1
            #print(check)
            queue.append([n_r, n_c,now[2]])
        elif Map[n_r][n_c] == 1 and now[2] == 0 :
            pass

print(answer)

