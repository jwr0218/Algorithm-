import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
Map = []

for i in range(N):
    Map.append(list(map(int,input().split())))
s = 0
for i in Map:
    s_i = max(i)
    s = max(s,s_i)

queue = deque([])
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
final_answer = 0

for height in range(0,101):
    visited = [[0 for i in range(N)] for j in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):

            if Map[i][j] > height and visited[i][j] == 0 :
                answer +=1
                visited[i][j] = 1
                queue.append([i,j])

                while queue:
                    now = queue.popleft()

                    for m in move:
                        n_r = now[0]+m[0]
                        n_c = now[1]+m[1]
                        if n_c < 0 or n_c >= N or n_r < 0 or n_r >= N :
                            continue
                        if Map[n_r][n_c] > height and visited[n_r][n_c] == 0 :
                            visited[n_r][n_c] = 1
                            queue.append([n_r,n_c])
    final_answer = max(final_answer,answer)

print(final_answer)
