import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import random
Num , E , W , S , N = map(int,input().split())
east = E
west = E+W
south = E+W+S
north = 100

Map = [[0 for _ in range(29)] for i in range(29)]
Map[14][14] = 1
move = [[0,1],[0,-1],[-1,0],[1,0]]
answer = 0
def dfs(num,now):
    global Num
    global answer
    if num == Num:
        #print("RETURN VALUE 는 1입니다. ")
        answer +=1
        return

    else:
        number = random.randrange(0, 100)


        if number < east:
            now[0] +=move[0][0]
            now[1] += move[0][1]
            if Map[now[0]][now[1]] == 1:
                return 0
            else:
                Map[now[0]][now[1]] = 1
                dfs(num+1,now)
            #move east
        elif number < west:
            now[0] += move[1][0]
            now[1] += move[1][1]
            if Map[now[0]][now[1]] == 1:
                return 0
            else:
                Map[now[0]][now[1]] = 1
                dfs(num + 1, now)
            #move west
        elif number < south:
            now[0] += move[2][0]
            now[1] += move[2][1]
            if Map[now[0]][now[1]] == 1:
                return 0
            else:
                Map[now[0]][now[1]] = 1
                dfs(num + 1, now)
            # move south
        else:
            now[0] += move[3][0]
            now[1] += move[3][1]
            if Map[now[0]][now[1]] == 1:
                return 0
            else:
                Map[now[0]][now[1]] = 1
                dfs(num + 1, now)
            # move north
for i in range(20000):
    Map = [[0 for _ in range(29)] for i in range(29)]
    Map[14][14] = 1
    dfs(0,[14,14])
print('answer : ',answer)
print(answer/20000)




