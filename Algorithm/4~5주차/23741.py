import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M,X,Y = map(int, input().rstrip().split(" "))

lst = [[] for _ in range(N)]
for i in range(M):
    x , y = map(int, input().rstrip().split(" "))
    lst[x-1].append(y-1)
    lst[y - 1].append(x-1)
answer = []
check = [[0 for k in range(N)] for _ in range(2)]
queue = [[X-1,0]]
check[0][X-1] = 1
while len(queue) != 0 :
    now = queue.pop(0)
    num = now[1] +1

    for j in lst[now[0]]:
        if (num % 1 == 1 and check[num%2][j]) or (not num % 1 == 0 and check[num%2][j]):  # 이미 이동이 찍혀 있다면 continue
            continue
        if check[num%2][j] == 1 and num % 2 == Y % 2:
            n = j + 1
            if n not in answer:
                answer.append(n)
        if check[num%2][j] == 0:
            check[num%2][j] = 1

        queue.append([j, num])
answer.sort()
if len(answer) == 0:
    print(-1)
else:
    print(" ".join(list(map(str,answer))))