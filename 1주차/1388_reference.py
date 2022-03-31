N,M = map(int,input().split())
# l[N][M]
l = []
for i in range(N):
    l.append(list(input()))
acount = 0
bcount = 0
def dfs1(l,x,y):
    if y >= M :
        return False
    if l[x][y] == '-':
        l[x][y] = 0
        ny = y+1
        dfs1(l,x,ny)
        return True
    return False
def dfs2(l,x,y):
    if x >=N :
        return False
    if l[x][y] == '|':
        l[x][y] = 0
        nx = x+1
        dfs2(l,nx,y)
        return True
    return False
for i in range(N):
    for j in range(M):
        if dfs1(l,i,j) == True:
            acount += 1
        if dfs2(l,i,j) == True:
            bcount += 1

print(acount+bcount)