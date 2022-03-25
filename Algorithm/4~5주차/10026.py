import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
Map = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    Map[_] = list(input().replace("\n",""))
move = [[0,1],[0,-1],[1,0],[-1,0]]

def dfs(now,state):
    for i in move:
        x = now[0] + i[0]
        y = now[1] + i[1]
        if x >= n or x <0 or y >= n or y<0 :
            continue

        if  Map[x][y] in list(state) and check[x][y] == 0 :

            check[x][y] = 1
            dfs([x, y], state)

check = [[0 for _ in range(n)] for _ in range(n)]

cnt_RGB = 0
for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.

        if check[i][j]==0:
            check[i][j] = 1
            dfs([i,j],Map[i][j])
            cnt_RGB += 1


check = [[0 for _ in range(n)] for _ in range(n)]

cnt_RgB = 0
for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if check[i][j]==0:
            check[i][j] = 1

            st = ""
            if Map[i][j] in list("RG"):
                st = "RG"
            else:
                st = "B"
#            print(st)
            dfs([i,j],st)
            cnt_RgB += 1

print(cnt_RGB,cnt_RgB)

