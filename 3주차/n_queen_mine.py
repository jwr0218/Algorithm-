import sys

input = sys.stdin.readline

N = int(input())
queen_list = []
cnt = 0

def queen(Map,X,Y):

    lst = []
    for i in range(len(Map)**27):
        if i < len(Map):
            if Map[X][i] != 1:
                lst.append([X, i])
                Map[X][i] = 1
            if Map[i][Y] != 1:
                lst.append([i,Y])
                Map[i][Y] = 1

        if X-i >= 0 and Y-i >= 0 and Map[X-i][Y-i] != 1:
            lst.append([X-i,Y-i])
            Map[X-i][Y-i] = 1

        if X+i < len(Map) and Y+i < len(Map) and Map[X+i][Y+i] != 1:
            lst.append([X+i,Y+i])
            Map[X + i][Y + i] = 1

        if X-i >= 0 and Y+i <len(Map) and Map[X-i][Y+i] != 1:
            lst.append([X-i,Y+i])
            Map[X-i][Y+i] = 1

        if X+i < len(Map) and Y-i >=0 and Map[X+i][Y-i] != 1:
            lst.append([X+i,Y-i])
            Map[X + i][Y - i] = 1
    return lst



def re_queen(Map,lst):
    for l in lst:
        Map[l[0]][l[1]] = 0



def check(Map):
    s=0

    for i in Map:

        s+=sum(i)
    if s == len(Map)**2:
        return True

    return False


Map = [[0 for _ in range(N)] for i in range(N)]


def dfs():
    global cnt


    if check(Map):
        return

    for i in range(len(Map)):
        for j in range(len(Map)):

            if Map[i][j] == 0:
                if len(queen_list) == N:
                    cnt+=1

                queen_list.append(queen(Map,i,j))

                dfs()
                l = queen_list.pop()



                re_queen(Map,l)



dfs()



'''for i in Map:
    print(i)
re_queen(Map,l)
for i in Map:
    print(i)'''
print(cnt)