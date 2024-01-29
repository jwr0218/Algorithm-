from collections import deque



N  = int(input())

graph = [[] for i in range(N)]
queue = []
for i in range(N):
    node = list(map(int,input().split()))
    
    for n in range(len(node)):
        if node[n] == 1:
            graph[i].append(n)
            queue.append(i)




queue = deque(queue)
print(queue)
while len(queue) > 0 :
    now = queue.popleft()
    print(now)

print(graph)