import sys

input = sys.stdin.readline
N = int(input())
direction = [[1,0],[-1,0],[0,1],[0,-1]]

for _ in range(N):
    M , N , K = map(int,input().split())
    #print(M,N,K)

    Map = [[0 for i in range(M)] for j in range(N)]
    check = []
    for k in range(K):
        x, y = map(int, input().split())
        Map[y][x] = 1
        check.append([x,y])

    queue = []
    cnt = 0
    t = 0
    while len(check) != 0:
        ca = check.pop(0)
        queue.append(ca)
        cnt +=1
        #print(check)

        while len(queue)!=0:
            x,y = queue.pop(0)
            for di in direction:
                x_n = x+di[0]
                y_n = y+di[1]

                if y_n >= N or y_n < 0 or x_n >= M or x_n < 0:
                    continue

                if Map[y_n][x_n]==1 and [x_n,y_n] in check:
                    #print("X_N : {} , Y_N : {}".format(x_n,y_n))
                    check.remove([x_n,y_n])
                    queue.append([x_n,y_n])
        #print("중간단계 cnt : ",cnt)
        #print(check)



    print(cnt)

