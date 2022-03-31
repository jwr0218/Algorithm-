import sys
input = sys.stdin.readline
n  = int(input())

check = []
Map = []

for i in range(n):
    s = input()
    a = list(s)[:-1]
    a = list(map(int,a))

    Map.append(a)

    check.append([0 for _ in range(n)])
queue = [[0,0]]
di = [[-1,0],[1,0],[0,-1],[0,1]]
answer = []

#집에 들어왔을때 bfs
def dfs(r,c,cnt):
    check[r][c] = 1
    #print("count :",cnt)

    for i in di:

        r_n = r + i[0]
        c_n = c + i[1]
        if r_n <0 or r_n >= len(Map):
            continue
        if c_n <0 or c_n >= len(Map):
            continue
        if Map[r_n][c_n] == 1 and check[r_n][c_n]!= 1 :

            cnt += 1

            cnt = dfs(r_n,c_n,cnt)
    return cnt



while len(queue) != 0:
    br = queue.pop(0)

    for i in di:
        r = br[0] + i[0]
        c = br[1] + i[1]

        if r <0 or r >= len(Map):
            continue
        if c <0 or c >= len(Map):
            continue



        if Map[r][c] == 1 and check[r][c] ==0 :
            cnt = 1
            cnt =dfs(r,c,cnt)
            answer.append(cnt)

        elif check[r][c] != 2 :
            check[r][c] = 2
            queue.append([r,c])


answer.sort()
print(len(answer))

for i in answer:
    print(i)
