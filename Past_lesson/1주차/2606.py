n = int(input())
c = int(input())
connect = [[] for _ in range(n)]
com = [0 for _ in range(n)]


for i in range(c):
    f , t = map(int,input().split(" "))
    connect[f-1].append(t-1)
    connect[t-1].append(f-1)


queue = []

for i in connect[0]:
    queue.append([0,i])

while len(queue) != 0:
    q = queue.pop(0)
    f = q[0]
    com[f] = 1
    t = q[1]
    #print("F :",f,'T : ',t)
    for i in connect[t]:
        if com[t] == 1:
            continue
        queue.append([t,i])

print(sum(com)-1)