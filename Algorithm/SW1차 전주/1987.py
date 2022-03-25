import sys
from collections import deque

input = sys.stdin.readline
R , C = map(int,input().split())

Map = []

for i in range(R):
    Map.append(list(input().replace("\n","")))
# r ,c , path , length
queue = [[0,0,[Map[0][0]]]]
queue = deque(queue)

move  = [[0,1],[0,-1],[1,0],[-1,0]]
answer = 0

def dfs(r,c,path):
    global answer
    if answer < len(path):
        answer = len(path)
    #print(r,c,path)

    for i in move:
        n_r = r + i[0]
        n_c = c + i[1]
        if n_r >= R or n_r < 0 or n_c >= C or n_c < 0 :
            continue
        if Map[n_r][n_c] not in path:
            path.add(Map[n_r][n_c])
            dfs(n_r,n_c,path)
            path.remove(Map[n_r][n_c])
        else:
            pass


dfs(0,0,set([Map[0][0]]))
print(answer)
