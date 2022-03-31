from collections import deque
from sys import stdin as s

n, m, k=map(int, s.readline().split())
mp=[[int(i) for i in s.readline().strip()] for _ in range(n)]
t=10**9
dist=[[[t]*(k+1) for _ in range(m)] for _ in range(n)]
dx=[-1, 0, 0, 1]
dy=[0, -1, 1, 0]
dist[0][0][0]=1

q=deque()
q.append((0, 0, 0, 1, 0))

while q :
    x, y, z, d, night=q.popleft()
    if(dist[x][y][z]!=d) :
        continue
    for i in range(4) :
        nx, ny=x+dx[i], y+dy[i]
        if(0<=nx<n and 0<=ny<m) :
            if(mp[nx][ny]==0 and dist[nx][ny][z]>d+1) :
                dist[nx][ny][z]=d+1
                q.append((nx, ny, z, d+1, 1-night))
            elif(z<k and mp[nx][ny]==1) :
                if(night==0 and dist[nx][ny][z+1]>d+1) :
                    dist[nx][ny][z+1]=d+1
                    q.append((nx, ny, z+1, d+1, 1))
                elif(night==1 and dist[nx][ny][z+1]>d+2) :
                    dist[nx][ny][z+1]=d+2
                    q.append((nx, ny, z+1, d+2, 1))

ans=min(dist[-1][-1])
print(ans if ans!=t else -1)