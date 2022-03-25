import sys
import heapq
input = sys.stdin.readline

N , M  = map(int,input().split())

chess_real = []
num = []

for i in range(N):

    chess_real.append(list(input().replace("\n","")))

# 얼마나 바꿔야 하는지 ?
def check_count(chess):

    cnt_1 = 0
    for i in range(8):
        for j in range(8):
            #짝수 행
            if i % 2 == 0:
                #짝수 열
                if j % 2 == 0:
                    if chess[i][j] != "W":
                        cnt_1 +=1
                #홀수 열
                else:
                    if chess[i][j] != "B":
                        cnt_1 +=1
            #홀수 행
            elif i % 2 == 1:
                #짝수 열
                if j % 2 == 0:

                    if chess[i][j] != "B":
                        cnt_1 += 1
                #홀수 열
                else:

                    if chess[i][j] != "W":
                        cnt_1 += 1
    #처음이 B일떄
    cnt_2 = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if chess[i][j] != "B":
                        cnt_2 +=1
                else:
                    if chess[i][j] != "W":
                        cnt_2 +=1
            elif i % 2 == 1:
                if j % 2 == 0:
                    if chess[i][j] != "W":
                        cnt_2 += 1
                else:
                    if chess[i][j] != "B":
                        cnt_2 += 1
    #print("CNT1 : {} CNT2 : {}".format(cnt_1,cnt_2))
    #print(chess[7][7])
    return min(cnt_1,cnt_2)

#다 확인하는 코드
min_lst = []
for r in range(0,N-7):


    for c in range(0,M-7):
        new_chess = []

        for i in range(8):

            new_chess.append(chess_real[r+i][c:c+8])

        min_lst.append(check_count(new_chess))

print(min(min_lst))

