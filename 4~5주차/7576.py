import sys
from collections import deque

input = sys.stdin.readline

C , R = map(int,input().split())
lst = []
for i in range(R):
    lst.append(list(map(int,input().replace("\n","").split())))
answer = 0

def dfs(queue):
    global answer
    queue = deque(queue)
    move = [[-1,0],[1,0],[0,-1],[0,1]]
    while len(queue) != 0 :
        now = queue.popleft()

        answer = now[2]
        for i in move:
            n_r = now[0]+i[0]
            n_c = now[1] + i[1]
            if n_r >= R or n_c >= C or n_c < 0 or n_r < 0 :
                continue

            if lst[n_r][n_c] == 0 :
                lst[n_r][n_c] =1
                queue.append([n_r,n_c,now[2]+1])






b = False
li = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 1:
            li.append([i,j,0])

dfs(li)


for i in lst:
    for j in i:
        if j == 0:
            answer = -1
            b = True
            break
    if b :
        break
print(answer)