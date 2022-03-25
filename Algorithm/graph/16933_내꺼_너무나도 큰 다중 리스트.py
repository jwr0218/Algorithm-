import sys
from collections import deque

input = sys.stdin.readline

N ,M , K = map(int,input().split())

Map = []
check = [[[[999999 for i in range(2)] for j in range(K+1)]for z in range(M)] for k in range(N)]



# 구성 check[낮밤][횟수][N행][M열]
for i in range(N):
    Map.append(list(map(int,list(input().replace("\n","")))))


            # 0번 , 낮
queue = [[0,0,0,0]]
queue = deque(queue)
move = [[1,0],[-1,0],[0,1],[0,-1],[0,0]]
check[0][0][0][0] = 1
answer= -1



#BFS로 낮, 밤 정보를 보내서 연산 과정을 생략할 수 있어야 한다...

#다른 답에서는 day / night를 구분해서 조금 더 간단하게 풀었다.

#한번 대기타는 것보단 +2 해서 넘어가면 더 빠르게 된다! 왜 이런 생각을 못했을까,,,,


while queue:
    now = queue.popleft()

    if now[0]== N-1 and now[1] == M-1:
        answer = check[now[0]][now[1]][now[2]][now[3]]
        break
    for i in move:
        n_r = now[0] + i[0]
        n_c = now[1] + i[1]
        if n_r >= N or n_c >= M or n_r < 0 or n_c < 0:
            continue

        if now[2] <= K :


            if Map[n_r][n_c] == 1 :



                if i[0] == 0 and i[1] == 0 :

                    if check[n_r][n_c][now[2]][(now[3] + 1) % 2] > check[now[0]][now[1]][now[2]][now[3]] + 1:

                        check[n_r][n_c][now[2]][(now[3] + 1) % 2] = check[now[0]][now[1]][now[2]][now[3]] + 1
                        queue.append([n_r, n_c, now[2], (now[3] + 1) % 2])
                        #이동하지 않고 밤낮만 바뀌기

                if now[3] == 1:
                    continue
                # 낮 밤 바뀌는거 해결해야함
                if now[2] == K:
                    continue
                if check[n_r][n_c][now[2]+1][(now[3]+1)%2] > check[now[0]][now[1]][now[2]][now[3]] +1:
                    check[n_r][n_c][now[2] + 1][(now[3] + 1) % 2] = check[now[0]][now[1]][now[2]][now[3]] + 1
                    queue.append([n_r,n_c,now[2]+1,(now[3] + 1) % 2])
            else:


                if check[n_r][n_c][now[2]][(now[3] + 1) % 2] > check[now[0]][now[1]][now[2]][now[3]] + 1:

                    check[n_r][n_c][now[2]][(now[3] + 1) % 2] = check[now[0]][now[1]][now[2]][now[3]] + 1
                    queue.append([n_r,n_c,now[2],(now[3] + 1) % 2])

print(answer)