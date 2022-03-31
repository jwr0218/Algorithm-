import sys
input = sys.stdin.readline

N , M , K , X = map(int,input().split())
queue= []
for i in range(M):
    queue.append(list(map(int,input().split())))
Map = [[999999 for _ in range(N)] for _ in range(N)]
Map[0][0] = 0
while len(queue) != 0 :
    A , B = queue.pop(0)
    A -=1
    B -=1
    #print(A , B )

    Map[A][B] = 1
    for fr in range(len(Map)):

        cost = 1 + Map[fr][A]
        if cost < Map[fr][B]:
            Map[fr][B] = cost
            #양방향 만들땐 뒤 코드 더하기
            #queue.append([B+1,A+1])
final=Map[X-1]
answer = -1

test = [i for i, value in enumerate(final) if value == K]

for i in test:

    print(i+1)
    answer = i

if answer == -1:
    print(answer)
