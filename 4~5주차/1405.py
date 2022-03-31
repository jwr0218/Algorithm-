d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 4방향 탐색

def dfs(r, c, visited, total):
    global answer
    if len(visited) == N+1:
        #여기까지 갔을 확률

        answer += total
        return
    for idx in range(4):
        nr = r + d[idx][0]
        nc = c + d[idx][1]
        if (nr, nc) not in visited:
            visited.append((nr, nc))
            #print("total? ",total*probability[idx])
            dfs(nr, nc, visited, total*probability[idx])
            visited.pop()

N, ep, wp, sp, np = map(int, input().split())
probability = [ep, wp, sp, np]
answer = 0

dfs(0, 0, [(0, 0)], 1)
#print("answer :",answer)
#print(0.01**N)
print(answer * (0.01 ** N))
